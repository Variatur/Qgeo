# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Qgeo
                                 A QGIS plugin
 Loads Queensland geoscience data from the Queensland government feature server.
                              -------------------
        begin                : 2020-11-07
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
from .nr_collector import *
from .query import *
from .cadastral import *
#
class QgeoAlgorithm(QgsProcessingAlgorithm):
    INPUT = 'INPUT'
    OUTPUTDIR = 'OUTPUTDIR'
    LOADTENURE = "LOADTENURE"
    LOADDSURFG = "LOADDSURFG"
    LOADDSOLG = "LOADDSOLG"
    LOADDETAILED = "LOADDETAILED"
    LOADREGIONAL = "LOADREGIONAL"
    #
    def initAlgorithm(self, config):
        self.addParameter(
            QgsProcessingParameterString(
                self.INPUT,
                self.tr('Search LotPlan number(s) e.g. 53SP253460 92OR290 67OR337  [will ignore invalid Lot/Plans]')
            )
        )
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
                self.tr('Detailed geology (1:100k) - not available in all areas'),
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
        project = QgsProject.instance()
        projectCRS=project.crs()
        standardCRS = "EPSG:7844"
        #Parse the lot plan numbers
        lots = re.sub('[^0-9a-zA-Z]+', ',', self.parameterAsString(parameters,self.INPUT,context).upper()).split(',')
        #
        #
        lotplans_message = "Lot/Plan(s): "+", ".join(lots)
        feedback.setProgressText(lotplans_message)
        #  
        loadTenure = self.parameterAsBool(parameters,self.LOADTENURE,context)
        #loadDSurfG = self.parameterAsBool(parameters,self.LOADDSURFG,context)
        #loadDSolG = self.parameterAsBool(parameters,self.LOADDSOLG,context)
        loadDetailed = self.parameterAsBool(parameters,self.LOADDETAILED,context)
        loadRegional = self.parameterAsBool(parameters,self.LOADREGIONAL,context)
        outputDIR = self.parameterAsFileOutput(parameters,self.OUTPUTDIR,context)
        feedback.setProgress(1)
        # The following lines workaround an apparent QGIS bug where a temporary directory isn't actually made.
        try:
            os.mkdir(outputDIR)
        except FileExistsError as e:
            pass
        ##########################
        # Get property polygon(s)
        ##########################
        feedback.setProgressText("Getting property polygon(s)...")  
        layerInfo = dict(   lots = lots,
                            layername = 'Property Boundary',
                            layerstyle = 'LayerStyles/Property.qml',
                            projectCRS = projectCRS,
                            outputDIR = outputDIR,
                            standardCRS = standardCRS
                            )
        PropertyVlayer = LoadPropertyLayer(layerInfo,context,feedback)
        if PropertyVlayer == None or not PropertyVlayer.isValid() or PropertyVlayer.featureCount() < 1:
            feedback.reportError("Failed to load property boundary! Invalid lot/plan? Network or server problems?", True)
            return {}
        #
        feedback.setProgress(3)
        feedback.setProgressText("Property polygon(s) loaded")  
        # Load property layer to canvas
        project.addMapLayer(PropertyVlayer, False)
        layerTree = iface.layerTreeCanvasBridge().rootGroup()
        layerTree.insertChildNode(0, QgsLayerTreeLayer(PropertyVlayer))
        feedback.setProgress(4)
        #
        #Zoom to extent
        canvas = iface.mapCanvas()
        canvasCRS = QgsCoordinateReferenceSystem(canvas.mapSettings().destinationCrs().authid())
        PropertyCRS = QgsCoordinateReferenceSystem(PropertyVlayer.crs())
        xform = QgsCoordinateTransform(PropertyCRS, canvasCRS, project)
        canvas.setExtent(xform.transform(PropertyVlayer.extent()))
        #
        # Initialise
        layerInfo = dict(   vlayer = PropertyVlayer,
                            outputDIR = outputDIR,
                            standardCRS = standardCRS,
                            searchType = 'lotplan'
                            )
        #
        ################################
        # Get Tenure                   #
        ################################
        if loadTenure:
            feedback.setProgressText("**********") 
            post = dict(        service1 = "PlanningCadastre/", 
                                service2 = "LandParcelPropertyFramework/",
                                serviceNumber = str(13)
                                )
            layerInfo.update(dict(  layername = "Tenure",
                                    layerstyle = "LayerStyles/QldPropertyTenure.qml",
                                    geomtype = "MultiPolygon"
                                    ))
            LayerName = layerInfo['layername']
            feedback.setProgressText(LayerName+" - checking...")
            fc = LoadNaturalResourceLayer(post,layerInfo,context,feedback)  # fc = feature count
            if fc > 1: feedback.setProgressText(LayerName+" - loaded "+str(fc)+" objects")
            if fc == 1: feedback.setProgressText(LayerName+" - loaded "+str(fc)+" object")
            if fc == 0: feedback.setProgressText("  -- No objects found --")
            feedback.setProgress(6)
        ################################
        # Detailed Geology             #
        ################################
        if loadDetailed:
            feedback.setProgressText("**********") 
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
                fc = LoadNaturalResourceLayer(post,layerInfo,context,feedback)
                if fc > 1: feedback.setProgressText(LayerName+" - loaded "+str(fc)+" objects")
                if fc == 1: feedback.setProgressText(LayerName+" - loaded "+str(fc)+" object")
                if fc == 0: feedback.setProgressText("  -- No objects found --")
                feedback.setProgress(8)
        #
        ###############################
        # Get Regional Geology        #
        ###############################
        if loadRegional:
            feedback.setProgressText("**********") 
            feedback.setProgressText("Regional geology - checking...")
            for i in range(2,16):
                post = dict(        service1 = "GeoscientificInformation/", 
                                    service2 = "GeologyRegional/"
                                    )
                feedback.setProgress(12+2*i)
                for j in range (0,2):
                    k=12+2*i+j
                    post.update(dict(serviceNumber = str(k)))
                    LayerName=json.loads(GetGEOJSON(ItemInfo(post,context,feedback),context,feedback))
                    DefaultLayerName = 'RegionalGeology-'+str(k)
                    LayerName=LayerName.get('title',DefaultLayerName)
                    feedback.setProgressText(LayerName+" - checking...")
                    layerInfo.update(dict(  layername = LayerName,
                                            layerstyle = "LayerStyles/RegionalGeology"+str(k)+".qml",
                                            geomtype = "MultiPolygon"
                                            ))
                    if j==0: layerInfo.update(dict(  geomtype = "MultiLineString"))
                    fc = LoadNaturalResourceLayer(post,layerInfo,context,feedback)
                    if fc > 0:
                        if fc > 1: feedback.setProgressText(LayerName+" - loaded "+str(fc)+" objects")
                        if fc == 1: feedback.setProgressText(LayerName+" - loaded "+str(fc)+" object")
                    if fc == 0: feedback.setProgressText("  -- No objects found --")
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
        return 'Lot Plan search'

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
        return QgeoAlgorithm()
    
    def icon(self):
        return QIcon(resolve("search.png"))
    
    def flags(self):
        return super().flags() | QgsProcessingAlgorithm.FlagNoThreading
    #