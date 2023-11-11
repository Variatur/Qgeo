# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Qgeo
                                 A QGIS plugin
 Loads Queensland geoscience map data from the Queensland government feature server based on a property (lot plan) search.

                              -------------------
        begin                : 2020-05-06
        updated              : 2021-04-25
        updated              : 2023-04-11
        updated              : 2023-07-15
        updated              : 2023-11-12
        copyright            : (C) 2023 by Otto Pattemore and Gary Pattemore
        email                : variatursoftware .at. gmail .dot. com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This work is licensed under the Creative Commons Attribution 4.0      *
 *   International License. To view a copy of this license,                *
 *   visit http://creativecommons.org/licenses/by/4.0/ or                  *
 *   send a letter to Creative Commons,                                    *
 *   PO Box 1866, Mountain View, CA 94042, USA.                            *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Otto Pattemore and Gary Pattemore'
__date__ = '2023-11-12'
__copyright__ = '(C) 2023 by Otto Pattemore and Gary Pattemore'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import *
from qgis.utils import iface
import re
import os
import processing
from PyQt5.QtGui import QIcon
import time
import datetime
import json
from PyQt5.QtWidgets import QMessageBox
from .cadastral import *
from .nr_collector import *
from .query import *
#
class QextentAlgorithm(QgsProcessingAlgorithm):
    #INPUT = 'INPUT'
    OUTPUTDIR = 'OUTPUTDIR'
    LOADTENURE = "LOADTENURE"
    LOADDETAILED = "LOADDETAILED"
    LOADREGIONAL = "LOADREGIONAL"
    def initAlgorithm(self, config):
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADTENURE,
                self.tr('Tenure'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADDETAILED,
                self.tr('Detailed geology (1:100k)'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADREGIONAL,
                self.tr('Regional geology (1:500k or 1:1M)'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterFolderDestination(
                self.OUTPUTDIR,
                self.tr("Directory to save output files")
            )
        )
        #
    def processAlgorithm(self, parameters, context, feedback):
        # Set the standard CRS to GDA2020 (EPSG:7844)
        standardCRS = "EPSG:7844"
        #  
        loadTenure = self.parameterAsBool(parameters,self.LOADTENURE,context)
        loadDetailed = self.parameterAsBool(parameters,self.LOADDETAILED,context)
        loadRegional = self.parameterAsBool(parameters,self.LOADREGIONAL,context)
        outputDIR = self.parameterAsFileOutput(parameters,self.OUTPUTDIR,context)
        feedback.setProgress(1)
        # The following lines workaround an apparent QGIS bug where a temporary directory isn't actually made.
        try:
            os.mkdir(outputDIR)
        except FileExistsError as e:
            pass
        #
        feedback.setProgress(5)
        #
        # Calculate area of extent
        #
        project = QgsProject.instance()
        canvas = iface.mapCanvas()
        canvasCRS = QgsCoordinateReferenceSystem(canvas.mapSettings().destinationCrs().authid())
        #print("canvasCRS : ",canvasCRS)

        # get canvas extent
        canvasExtent = canvas.extent() # a QgsRectangle 
        #print("canvasExtent : ",canvasExtent)

        # convert to geometry
        canvasBorder = QgsGeometry().fromRect(canvasExtent)  # a QgsGeometry
        #print("canvasBorder : ",canvasBorder)

        #Transform CRS to standard CRS
        xform = QgsCoordinateTransform(canvasCRS, QgsCoordinateReferenceSystem(standardCRS), project)
        canvasBorder.transform(xform)
        extent_in_standardCRS= canvasBorder.boundingBox()

        #measure area
        QgsDistanceArea().setSourceCrs(QgsCoordinateReferenceSystem(standardCRS),project.transformContext())
        QgsDistanceArea().setEllipsoid(project.ellipsoid())
        area = QgsDistanceArea().measureArea(canvasBorder)
        area_in_hectares = QgsDistanceArea().convertAreaMeasurement(area,QgsUnitTypes.AreaHectares)
        #print("canvasBorder area : ",area)
        #print("Hectares : ",area_in_hectares)
        #print("Area units",QgsUnitTypes().encodeUnit(QgsDistanceArea().areaUnits()))

        # Build geometry query string
        xmin = str(extent_in_standardCRS.xMinimum())
        ymin = str(extent_in_standardCRS.yMinimum())
        xmax = str(extent_in_standardCRS.xMaximum())
        ymax = str(extent_in_standardCRS.yMaximum())
        CanvasExtentString = xmin+","+ymin+","+xmax+","+ymax
        print("Extent in stdCRS",CanvasExtentString)
        #
        #project = QgsProject.instance()
        #canvas = iface.mapCanvas()
        #canvasExtent = canvas.extent()
        #tempV = QgsGeometry().fromRect(canvasExtent)
        #measure = QgsDistanceArea()
        #tc= project.transformContext()
        #canvasCRS = QgsCoordinateReferenceSystem(canvas.mapSettings().destinationCrs().authid())
        #measure.setSourceCrs(canvasCRS,tc)
        #measure.setEllipsoid(project.ellipsoid())
        #area = measure.measureArea(tempV)
        # Exit if too large
        if area_in_hectares > 30000000:
            feedback.reportError("Extent is too large ("+str(round(area_in_hectares))+" ha) - exiting...", True)
            return {}
        #
        ##Convert canvas extent to standard CRS
        #xform = QgsCoordinateTransform(canvasCRS, QgsCoordinateReferenceSystem(standardCRS), project)
        #canvasExtent = xform.transform(canvasExtent)
        ## Get canvas CRS in plain english - actually, this is only used for server query and should be in standardCRS
        ##NEEDS RENAMING
        ##canvasCRS = QgsCoordinateReferenceSystem(canvas.mapSettings().destinationCrs()).authid()
        #canvasCRS = standardCRS
        ##
        ## Build geometry query string
        #xmin = str(canvasExtent.xMinimum())
        #ymin = str(canvasExtent.yMinimum())
        #xmax = str(canvasExtent.xMaximum())
        #ymax = str(canvasExtent.yMaximum())
        #CanvasExtentString = xmin+","+ymin+","+xmax+","+ymax
        TimeString = str(datetime.datetime.now()).replace(':','-').replace(':','-').replace('.','-').replace(' ','-')
        # Initialise dictionaries
        post = {}
        layerInfo = dict(   outputDIR = outputDIR,
                            standardCRS = standardCRS,
                            canvasCRS = canvasCRS,
                            gpkg_basename = 'Qgeo-ExtentSearch_'+TimeString,
                            extent = CanvasExtentString,
                            searchType = 'extentstring'
                            )
        # Set object count warning value
        MaxObjects = 20000
        GrandTotal = 0
        #QT messagebox return values
        no = 65536
        yes = 16384
        # initialise variable to record regional geology datasets with feature counts > 0
        regionalHits = []
        # set to first return count of object only 
        #
        for RC in range (2): # RC= Return Count --- if RC=0 loop will count the required objects only -- to test if query is reasonable. 
            if GrandTotal > MaxObjects:
                response = QMessageBox.question(None, "Large download warning", "The chosen extent and layers have resulted in a request for "+str(GrandTotal)+" objects.\n\n"+
                "As a rough guide 100,000 objects may take 10 minutes on faster connections but a few hours on slower connections.\n\n"+
                "Recommendation: try a smaller extent or download the dataset directly from http://qldspatial.information.qld.gov.au \n\n"+
                "Do you want to proceed this the current request ?")
                if response == no: 
                    feedback.reportError("Request terminated by user", True)
                    return {}
            #Load Natural Resource layers
            #
            ###############################
            # Get Tenure                  #
            ###############################
            if loadTenure:
                if RC == 0: feedback.setProgressText("Tenure map - calculating size...")
                else: feedback.setProgressText("Tenure map - loading spatial data...")
                post = dict(        service1 = "PlanningCadastre/", 
                                    service2 = "LandParcelPropertyFramework/",
                                    serviceNumber = str(13)
                                    )
                layerInfo.update(dict(  layername = "Tenure",
                                        layerstyle = "LayerStyles/QldPropertyTenure.qml",
                                        geomtype = "MultiPolygon"
                                        ))
                if RC == 0:
                    post.update(dict(   geometry = layerInfo['extent'],
                                        objectIds = ''
                                        ))
                    objectCount = GetObjectCount(post,layerInfo,context,feedback)
                    if objectCount > 0:
                        feedback.setProgressText("Object count = "+str(objectCount))
                        GrandTotal = GrandTotal + objectCount
                else: 
                    LoadNaturalResourceLayer(post,layerInfo,context,feedback)
            ###############################
            # Get Detailed Geology        #
            ###############################
            if loadDetailed:
                post = dict(        service1 = "GeoscientificInformation/", 
                                    service2 = "GeologyDetailed/"
                                    )
                for i in range(3,18):
                    if i == 14 or i == 16: continue
                    post.update(dict(serviceNumber = str(i)))
                    LayerName=json.loads(GetGEOJSON(ItemInfo(post,context,feedback),context,feedback))
                    DefaultLayerName = 'Detailed geology (1:100k)-'+str(i)
                    LayerName=LayerName.get('title',DefaultLayerName)
                    feedback.setProgressText(LayerName+" - checking...")
                    layerInfo.update(dict(  layername = LayerName,
                                            layerstyle = "LayerStyles/GeologyDetailed"+str(i)+".qml",
                                            geomtype = "MultiPolygon"
                                            ))
                    if i<14: layerInfo.update(dict(  geomtype = "MultiLineString"))
                    if RC == 0:
                        post.update(dict(   geometry = layerInfo['extent'],
                                            objectIds = ''
                                            ))
                        objectCount = GetObjectCount(post,layerInfo,context,feedback)
                        if objectCount > 0:
                            feedback.setProgressText("Object count = "+str(objectCount))
                            GrandTotal = GrandTotal + objectCount
                    else:
                        fc = LoadNaturalResourceLayer(post,layerInfo,context,feedback)
                        if fc > 1: feedback.setProgressText(LayerName+" - loaded "+str(fc)+" objects")
                        if fc == 1: feedback.setProgressText(LayerName+" - loaded "+str(fc)+" object")
            ###############################
            # Get Regional Geology        #
            ###############################
            if loadRegional:
                if RC == 0: feedback.setProgressText("Regional geology - calculating size...")
                else: feedback.setProgressText("Regional geology - loading spatial data...")
                post = dict(        service1 = "GeoscientificInformation/", 
                                    service2 = "GeologyRegional/"
                                    )
                for i in range(2,16):
                    for j in range (0,2):
                        k=12+2*i+j
                        if RC == 0:
                            post.update(dict(   serviceNumber = str(k),
                                                geometry = layerInfo['extent'],
                                                objectIds = ''
                                                ))
                            objectCount = GetObjectCount(post,layerInfo,context,feedback)
                            if objectCount>0:
                                feedback.setProgressText("Object count = "+str(objectCount))
                                GrandTotal = GrandTotal + objectCount
                                regionalHits.append(k)
                        else:
                            if k in regionalHits:
                                post.update(dict(   serviceNumber = str(k)))
                                LayerName=json.loads(GetGEOJSON(ItemInfo(post,context,feedback),context,feedback))
                                DefaultLayerName = 'RegionalGeology-'+str(k)
                                LayerName=LayerName.get('title',DefaultLayerName)
                                feedback.setProgressText("Regional geology - loading "+LayerName)
                                layerInfo.update(dict(  layername = LayerName,
                                                        layerstyle = "LayerStyles/RegionalGeology"+str(k)+".qml",
                                                        geomtype = "MultiPolygon"
                                                        ))
                                if j==0: layerInfo.update(dict(  geomtype = "MultiLineString"))
                                LoadNaturalResourceLayer(post,layerInfo,context,feedback)
            #
        #
        #
        feedback.setProgress(100)
        #
        return {}
    
    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Search by extent'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Geoscience'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return QextentAlgorithm()
    
    def icon(self):
        return QIcon(resolve("SearchByExtent.png"))
    
    def flags(self):
        return super().flags() | QgsProcessingAlgorithm.FlagNoThreading
    #