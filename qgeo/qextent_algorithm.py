# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Qgeo
                                 A QGIS plugin
 Loads Queensland geoscience map data from the Queensland government feature server based on a property (lot plan) search.

                              -------------------
        begin                : 2020-05-06
        copyright            : (C) 2020 by Otto and Gary Pattemore
        email                : g .dot. pattemore .at. gmail .dot. com
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

__author__ = 'Otto and Gary Pattemore'
__date__ = '2020-10-12'
__copyright__ = '(C) 2020 by Otto and Gary Pattemore'

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
#
def resolve(name, basepath=None):
    if not basepath:
      basepath = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(basepath, name)
class QextentAlgorithm(QgsProcessingAlgorithm):
    #INPUT = 'INPUT'
    OUTPUTDIR = 'OUTPUTDIR'
    LOADTENURE = "LOADTENURE"
    LOADDSURFG = "LOADDSURFG"
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
                self.LOADDSURFG,
                self.tr('Detailed surface geology (1:100k)'),
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
    def GetGEOJSON(self,URL,context,feedback):
        #This method of server access avoids firewall problems
        params = {
            'URL' : URL,
            'OUTPUT' : "TEMPORARY_OUTPUT"
        }
        tempLayer = processing.run(
            'native:filedownloader',
            params,
            is_child_algorithm=True,
            context=context,
            feedback=feedback)["OUTPUT"]
        if feedback.isCanceled():
            return None
        file = open(tempLayer)
        return_string = file.read()
        file.close()
        return return_string
    #def SetQueryDefaults(self,post,context,feedback):
    #    post.update(dict(   service1 = "",
    #                        service2 = "",
    #                        serviceNumber = "",
    #                        f = "json",
    #                        serviceType = "MapServer/",
    #                        returnCountOnly = "false",
    #                        returnGeometry = "true",
    #                        returnIdsOnly = "false",
    #                        outFields = "*",
    #                        outSR = "7844",
    #                        inSR = "7844",
    #                        geometryType = "esriGeometryEnvelope",
    #                        where = "",
    #                        objectIds = "",
    #                        geometry = ""
    #                        ))
    #    return post
    def BuildQuery(self,post,context,feedback):
        # 
        # Mandatory query parameters
        service1 = post.get('service1', '')
        service2 = post.get('service2', '')
        serviceNumber = post.get('serviceNumber', '')
        #
        # Optional query parameters with defaults
        f = post.get('f', 'json')
        serviceType = post.get('serviceType', "MapServer/")
        returnCountOnly = post.get('returnCountOnly', "false")
        returnGeometry = post.get('returnGeometry',"true")
        returnIdsOnly = post.get('returnIdsOnly', "false")
        outFields = post.get('outFields', '*')
        outSR = post.get('outSR', '7844')
        inSR = post.get('inSR', '7844')
        geometryType = post.get('geometryType', "esriGeometryEnvelope")
        #
        # Optional query parameters with empty string defaults
        where = post.get('where', '')
        objectIds = post.get('objectIds', '')
        geometry = post.get('geometry', '')
        # Build
        baseURL = "https://gisservices.information.qld.gov.au/arcgis/rest/"
        serviceURL = "services/"+service1+service2+serviceType
        whereURL = serviceNumber+"/query?where="+where+"&objectIds="+objectIds+"&time="
        geomURL = "&geometry="+geometry+"&geometryType="+geometryType+"&inSR="+inSR+"&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Meter&relationParam="
        out1URL = "&outFields="+outFields+"&returnGeometry="+returnGeometry+"&maxAllowableOffset=&geometryPrecision=&outSR="+outSR+"&having=&gdbVersion=&historicMoment=&returnDistinctValues=false"
        out2URL = "&returnIdsOnly="+returnIdsOnly+"&returnCountOnly="+returnCountOnly+"&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics="
        out3URL = "&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnExceededLimitFeatures=false"
        out4URL = "&quantizationParameters=&returnCentroid=false&sqlFormat=none&resultType=&featureEncoding=esriDefault&f="+f
        queryURL = baseURL+serviceURL+whereURL+geomURL+out1URL+out2URL+out3URL+out4URL
        # --following line to be deleted
        #print(queryURL)
        return queryURL
    def ItemInfo(self,post,context,feedback):
        baseURL = "https://gisservices.information.qld.gov.au/arcgis/rest/"
        # Mandatory query parameters
        service1 = post.get('service1', '')
        service2 = post.get('service2', '')
        serviceNumber = post.get('serviceNumber', '')
        #
        # Optional query parameters with defaults
        f = "json"
        serviceType = post.get('serviceType', "MapServer/")
        # Build
        serviceURL = "services/"+service1+service2+serviceType
        whereURL = serviceNumber+"/iteminfo?f="+f
        queryURL = baseURL+serviceURL+whereURL
        return queryURL
        #
    def LoadNaturalResourceLoader(self,post,layerInfo,context,feedback,RC):
        #list layerInfo
        standardCRS = layerInfo['standardCRS']
        canvasCRS = layerInfo['canvasCRS']
        layername = layerInfo['layername']
        layerstyle = layerInfo['layerstyle']
        outputDIR = layerInfo['outputDIR']
        geomtype = layerInfo['geomtype']
        gpkg_basename = layerInfo['gpkg_basename']
        service1 = post['service1']
        #
        standardCRSshort = standardCRS[len("EPSG:"):]
        post.update(dict(outSR = standardCRSshort))
        canvasCRSshort = canvasCRS[len("EPSG:"):]
        post.update(dict(inSR = canvasCRSshort))
        # make empty vector layer
        VMlayer = QgsVectorLayer(geomtype, layername, "memory")
        if not VMlayer.isValid():
                feedback.reportError("Layer failed to load! [code A1]", True)
                return 0
        #
        #Get data
        post.update(dict(   returnCountOnly = "true",
                            f = 'geojson',
                            geometry = layerInfo['extent']
                            ))
        #print(self.BuildQuery(post,context,feedback))
        queryResult = self.GetGEOJSON(self.BuildQuery(post,context,feedback),context,feedback)
        if queryResult == None:
            feedback.reportError("Problem communicating with server [code A1.2]", True)
            return -1
        if RC == 0:
            objectCount = json.loads(queryResult)["count"]
            feedback.setProgressText("Object count = "+str(objectCount))
            return objectCount
        else:
            post.update(dict(   returnCountOnly = "false",
                                returnIdsOnly = "true",
                                f = 'json',
                                objectIds = ''
                                ))
            objects = self.GetGEOJSON(self.BuildQuery(post,context,feedback),context,feedback)
            if objects == None:
                feedback.reportError("Problem communicating with server [code A1.3]", True)
                return -1
            post.update(dict(geometry = ''))
            objectID_list = json.loads(objects)["objectIds"]
            if objectID_list == None:
                feedback.setProgressText("No objects to retrieve...skipping")
                return 0
            objectCount = len(objectID_list)
            feedback.setProgressText("Getting "+str(objectCount)+" objects")
            #
            #Get 1000 features at a time - server limit is 2000 per query
            bundleSize = 1000
            position=0
            post.update(dict(   f = 'geojson',
                                returnIdsOnly = "false"
                                ))
            TimeString = str(datetime.datetime.now()).replace(':','-').replace(':','-').replace('.','-').replace(' ','-')
            while position*bundleSize < objectCount:
                sublist = objectID_list[position*bundleSize:position * bundleSize + (bundleSize-1)]
                sublist = ",".join(map(str,sublist))
                post.update(dict(objectIds = sublist))
                sublistQueryResult = self.GetGEOJSON(self.BuildQuery(post,context,feedback),context,feedback)
                if sublistQueryResult == None:
                    feedback.reportError("Problem communicating with server [code A1.4]", True)
                    return -1
                tempLayer = QgsVectorLayer(sublistQueryResult, layername, "ogr")
                #
                #Check if valid geometry is returned
                if tempLayer.featureCount() > 0:
                    #Buffer layer to clean-up inconsistencies in returned vector info -- uses buffer distance = 0
                    if QgsWkbTypes.geometryDisplayString(tempLayer.geometryType()) == "Polygon":
                        params = {
                            'INPUT' : tempLayer,
                            'DISTANCE' : 0,
                            'OUTPUT' : "memory:"
                        }
                        tempLayer = processing.run(
                            'native:buffer', 
                            params,
                            #is_child_algorithm=True,
                            context=context,
                            feedback=feedback)["OUTPUT"]
                        if feedback.isCanceled():
                            return -1
                    #
                    # Merging layer with Master copy if the clipped layer still has features
                    if tempLayer.featureCount() > 0:
                        params = {
                            'LAYERS' : [tempLayer,VMlayer],
                            'OUTPUT' : "memory:"
                        }
                        VMlayer = processing.run(
                            'native:mergevectorlayers', 
                            params,
                            #is_child_algorithm=True,
                            context=context,
                            feedback=feedback)["OUTPUT"]
                        if feedback.isCanceled():
                            return -1
                feedback.setProgress(25+round(position*bundleSize/objectCount*50))
                position = position + 1
                if position*bundleSize < objectCount: feedback.setProgressText("Got "+str(position*bundleSize)+" of "+str(objectCount)+" polygons")
            #Write layer to file and reload layer
            #Save as GeoPackage
            QgsVectorFileWriter.writeAsVectorFormat(VMlayer,outputDIR+'/'+layername+'_'+TimeString+".gpkg",'utf-8',QgsCoordinateReferenceSystem(standardCRS))
            # Reload layer
            VMlayer = QgsVectorLayer(outputDIR+'/'+layername+'_'+TimeString+".gpkg",layername,"ogr")
            if not VMlayer.isValid():
                    feedback.reportError("Failed to load layer "+layername, True)
                    return -1
            #
            VMlayer.loadNamedStyle(resolve(layerInfo['layerstyle']))
            #write style to geopackage
            VMlayer.saveStyleToDatabase(name="Qgeo-default",description=layerInfo['layerstyle'],useAsDefault=True, uiFileContent="")
            #
            #Add layer to canvas
            project = QgsProject.instance()
            project.addMapLayer(VMlayer, False)
            layerTree = iface.layerTreeCanvasBridge().rootGroup()
            layerTree.insertChildNode(1, QgsLayerTreeLayer(VMlayer))
            #VMlayer.triggerRepaint()
            feedback.setProgress(90)
            return 0
    def processAlgorithm(self, parameters, context, feedback):
        # Set the standard CRS to GDA2020 (EPSG:7844)
        standardCRS = "EPSG:7844"
        #  
        loadTenure = self.parameterAsBool(parameters,self.LOADTENURE,context)
        loadDSurfG = self.parameterAsBool(parameters,self.LOADDSURFG,context)
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
        project = QgsProject.instance()
        canvas = iface.mapCanvas()
        canvasExtent = canvas.extent()
        tempV = QgsGeometry().fromRect(canvasExtent)
        measure = QgsDistanceArea()
        tc= project.transformContext()
        canvasCRS = QgsCoordinateReferenceSystem(canvas.mapSettings().destinationCrs().authid())
        measure.setSourceCrs(canvasCRS,tc)
        measure.setEllipsoid(project.ellipsoid())
        area = measure.measureArea(tempV)
        # Exit if too large
        if area/10000 > 30000000:
            feedback.reportError("Extent is too large ("+str(round(area/10000))+" ha) - exiting...", True)
            return {}
        #
        #Convert canvas extent to standard CRS
        xform = QgsCoordinateTransform(canvasCRS, QgsCoordinateReferenceSystem(standardCRS), project)
        canvasExtent = xform.transform(canvasExtent)
        # Get canvas CRS in plain english - actually, this is only used for server query and should be in standardCRS
        #NEEDS RENAMING
        #canvasCRS = QgsCoordinateReferenceSystem(canvas.mapSettings().destinationCrs()).authid()
        canvasCRS = standardCRS
        #
        # Build geometry query string
        xmin = str(canvasExtent.xMinimum())
        ymin = str(canvasExtent.yMinimum())
        xmax = str(canvasExtent.xMaximum())
        ymax = str(canvasExtent.yMaximum())
        CanvasExtentString = xmin+","+ymin+","+xmax+","+ymax
        TimeString = str(datetime.datetime.now()).replace(':','-').replace(':','-').replace('.','-').replace(' ','-')
        # Initialise dictionaries
        post = {}
        layerInfo = dict(   outputDIR = outputDIR,
                            standardCRS = standardCRS,
                            canvasCRS = canvasCRS,
                            gpkg_basename = 'Qveg-ExtentSearch_'+TimeString,
                            extent = CanvasExtentString
                            )
        # Set object count warning value
        MaxObjects = 20000
        GrandTotal = 0
        #QT messagebox return values
        no = 65536
        yes = 16384
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
                feedback.setProgressText("Working on tenure map...")
                post = dict(        service1 = "PlanningCadastre/", 
                                    service2 = "LandParcelPropertyFramework/",
                                    serviceNumber = str(13)
                                    )
                layerInfo.update(dict(  layername = "Tenure",
                                        layerstyle = "LayerStyles/QldPropertyTenure.qml",
                                        geomtype = "MultiPolygon"
                                        ))
                value = self.LoadNaturalResourceLoader(post,layerInfo,context,feedback,RC)
                if value >= 0:
                    GrandTotal = GrandTotal + value 
            ###############################
            # Get Detailed Geology        #
            ###############################
            if loadDSurfG:
                feedback.setProgressText("Working on detailed surface geology map...")
                post = dict(        service1 = "GeoscientificInformation/", 
                                    service2 = "GeologyDetailed/",
                                    serviceNumber = str(15)
                                    )
                layerInfo.update(dict(  layername = "Detailed surface geology (1:100k)",
                                        layerstyle = "LayerStyles/GeologyDetailedSurface.qml",
                                        geomtype = "MultiPolygon"
                                        ))
                value = self.LoadNaturalResourceLoader(post,layerInfo,context,feedback,RC)
                if value >= 0:
                    GrandTotal = GrandTotal + value 
            ###############################
            # Get Regional Geology        #
            ###############################
            if loadRegional:
                for i in range(2,16):
                    feedback.setProgressText("Getting regional geology extent...")
                    post = dict(        service1 = "GeoscientificInformation/", 
                                        service2 = "GeologyRegional/",
                                        f = 'geojson',
                                        serviceNumber = str(i),
                                        geometry = CanvasExtentString
                                        )
                    # Get intersection with extent polygon of layer i
                    tempLayer = QgsVectorLayer(self.GetGEOJSON(self.BuildQuery(post,context,feedback),context,feedback), "tempLayer", "ogr")
                    if not tempLayer.isValid():
                        feedback.reportError("Layer failed to load! [code M3]", True)
                        return {}
                    # If there is an intersection then get geology
                    if tempLayer.featureCount()>0:
                        for j in range (0,2):
                            k=12+2*i+j
                            feedback.setProgressText("Getting regional geology...")
                            post = dict(        service1 = "GeoscientificInformation/", 
                                                service2 = "GeologyRegional/",
                                                geometry = CanvasExtentString,
                                                serviceNumber = str(k)
                                                )
                            LayerName=json.loads(self.GetGEOJSON(self.ItemInfo(post,context,feedback),context,feedback))
                            DefaultLayerName = 'RegionalGeology-'+str(k)
                            LayerName=LayerName.get('title',DefaultLayerName)
                            layerInfo.update(dict(  layername = LayerName,
                                                    layerstyle = "LayerStyles/RegionalGeology"+str(k)+".qml",
                                                    geomtype = "MultiPolygon"
                                                    ))
                            if j==0: layerInfo.update(dict(  geomtype = "MultiLineString"))
                            value = self.LoadNaturalResourceLoader(post,layerInfo,context,feedback,RC)
                            if value >= 0:
                                GrandTotal = GrandTotal + value
                    else: feedback.pushInfo("Property outside extent of regional geology mapping extent ID:"+str(i))
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