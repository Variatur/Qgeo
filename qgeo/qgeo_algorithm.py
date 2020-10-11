# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Qgeo
                                 A QGIS plugin
 Loads Queensland geoscience data from the Queensland government feature server.
                              -------------------
        begin                : 2020-10-07
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
__date__ = '2020-05-06'
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
#
def resolve(name, basepath=None):
    if not basepath:
      basepath = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(basepath, name)

class QgeoAlgorithm(QgsProcessingAlgorithm):
    INPUT = 'INPUT'
    OUTPUTDIR = 'OUTPUTDIR'
    LOADTENURE = "LOADTENURE"
    LOADDSURFG = "LOADDSURFG"
    LOADDSOLG = "LOADDSOLG"
    #LOADDSTRUCT = "LOADDSTRUCT"
    LOADRGSURF = "LOADRGSURF"
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
                self.LOADDSURFG,
                self.tr('Detailed surface geology (1:100k) - not available in all areas'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADDSOLG,
                self.tr('Detailed solid geology (1:100k) - not available in all areas'),
                False
            )
        )
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADDSTRUCT,
        #        self.tr('Detailed geologic structure (1:100k) - not available in all areas'),
        #        False
        #    )
        #)
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADRGSURF,
                self.tr('Regional surface geology (1:500k or 1:1M)'),
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
        objectIds = post.get('objectIDs', '')
        print(objectIds)
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
        print(queryURL)
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
    def LoadPropertyLayer(self,layerInfo,context,feedback):
        LotPlans = layerInfo['lots']
        standardCRS = layerInfo['standardCRS']
        layername = layerInfo['layername']
        layerstyle = layerInfo['layerstyle']
        outputDIR = layerInfo['outputDIR']
        #make short form of CRS for web query
        standardCRSshort = standardCRS[len("EPSG:"):]
        #
        #Build SQL query for server: LOTPLAN LIKE x OR LOTPLAN LIKE y
        LotPlansSQLQuery = "LOTPLAN+LIKE+'"+LotPlans[0] + "'"
        for lotplan in LotPlans[1:]:
            LotPlansSQLQuery = LotPlansSQLQuery + "+OR+LOTPLAN+LIKE+" + "'"+lotplan+"'"
        # Get list of polygon IDs
        post = None
        post = dict(    service1 = "PlanningCadastre/", 
                        service2 = "LandParcelPropertyFramework/",
                        serviceType = "MapServer/",
                        serviceNumber = str(4),
                        returnIdsOnly = "true",
                        f = 'json',
                        where = LotPlansSQLQuery,
                        returnGeometry = 'false'
                        )
        objectIDs = self.GetGEOJSON(self.BuildQuery(post,context,feedback),context,feedback)
        if objectIDs == None:
            return None
        objectID_list = json.loads(objectIDs)["objectIds"]
        print(objectID_list)
        # Get feature count
        if objectID_list == None:
            feedback.reportError("No objects to retrieve. Was the Lot/Plan valid? Exiting...")
            return None
        objectCount = len(objectID_list)
        feedback.setProgressText("Getting "+str(objectCount)+" polygons")
        #Get property polygon(s)
        post = dict(    service1 = "PlanningCadastre/", 
                        service2 = "LandParcelPropertyFramework/",
                        serviceType = "MapServer/",
                        serviceNumber = str(4),
                        returnIdsOnly = "false",
                        f = 'geojson',
                        where = '',
                        objectIDs = ",".join(str(i) for i in objectID_list),
                        returnGeometry = 'true',
                        outSR = standardCRSshort
                        )
        print(post.get('objectIDs'))
        PropertyLayer = QgsVectorLayer(self.GetGEOJSON(self.BuildQuery(post,context,feedback),context,feedback), layername, "ogr")
        #Ensure the created layer is valid
        if not PropertyLayer.isValid() or PropertyLayer.featureCount() < 1:
            #QgsMessageLog.logMessage("Failed to load property boundary! Invalid lot/plan?")
            feedback.reportError("Failed to load property boundary! Invalid lot/plan? [code B2]", True)
            return None
        #
        #Buffer layer to clean-up inconsistencies in returned vector info -- uses buffer distance = 0
        params = {
            'INPUT' : PropertyLayer,
            'DISTANCE' : 0,
            'OUTPUT' : "memory:"
        }
        PropertyLayer = processing.run(
            'native:buffer', 
            params,
            #is_child_algorithm=True,
            context=context,
            feedback=feedback)["OUTPUT"]
        if feedback.isCanceled():
            return None
        #
        #Write layer to shape file and reload layer from shapefile
        TimeString = str(datetime.datetime.now()).replace(':','-').replace(':','-').replace('.','-').replace(' ','-')
        #Save as GeoPackage
        QgsVectorFileWriter.writeAsVectorFormat(PropertyLayer,outputDIR+"/Property"+TimeString+".gpkg",'utf-8',QgsCoordinateReferenceSystem(standardCRS))
        #Save as shapefile 
        #QgsVectorFileWriter.writeAsVectorFormat(PropertyLayer,outputDIR+"/Property"+TimeString+".shp",'utf-8',QgsCoordinateReferenceSystem(standardCRS),driverName="ESRI Shapefile")
        # Reload layer
        PropertyLayer = QgsVectorLayer(outputDIR+"/Property"+TimeString+".gpkg","Property Boundary","ogr")
        if not PropertyLayer.isValid():
                feedback.reportError("Layer failed to load! [code B3]", True)
                return None
        #
        PropertyLayer.setName(layername)
        # Add styling
        PropertyLayer.loadNamedStyle(resolve(layerstyle))
        PropertyLayer.triggerRepaint()
        return PropertyLayer

    def LoadNaturalResourceLayer(self,post,layerInfo,context,feedback):
        #list layerInfo
        standardCRS = layerInfo['standardCRS']
        layername = layerInfo['layername']
        PropertyVlayer = layerInfo['vlayer']
        layerstyle = layerInfo['layerstyle']
        outputDIR = layerInfo['outputDIR']
        geomtype = layerInfo['geomtype']
        #
        standardCRSshort = standardCRS[len("EPSG:"):]
        NRdata = QgsVectorLayer(geomtype, layername, "memory")
        if not NRdata.isValid():
                feedback.reportError("Layer failed to load! [code A1]", True)
                return
        #
        #Looping through data collection from server for every property polygon
        #for objectid in PropertyVlayer.fields("OBJECTID"): print(objectid)
        for i in PropertyVlayer.getFeatures():
            #
            # Make single polygon vector layer for each object ID
            params = {
                    'INPUT' : PropertyVlayer,
                    'OPERATOR' : 0,
                    'FIELD' : "OBJECTID",
                    'VALUE' : i.attribute("OBJECTID"),
                    'OUTPUT' : "memory:"
                }
            Psubset = processing.run(
                'native:extractbyattribute', 
                params,
                #is_child_algorithm=True,
                context=context,
                feedback=feedback)["OUTPUT"]
            if feedback.isCanceled():
                return
            #
            #Get extent of each property polygon
            PolygonExtent = i.geometry().boundingBox()
            xmin = str(PolygonExtent.xMinimum()-0.01)
            ymin = str(PolygonExtent.yMinimum()-0.01)
            xmax = str(PolygonExtent.xMaximum()+0.01)
            ymax = str(PolygonExtent.yMaximum()+0.01)
            ExtentString = xmin+","+ymin+","+xmax+","+ymax
            #Set data source (server query)
            post.update(dict(geometry = ExtentString))
            #
            #Get data
            tempLayer = QgsVectorLayer(self.GetGEOJSON(self.BuildQuery(post,context,feedback),context,feedback), "temp "+layername, "ogr")
            if not tempLayer.isValid():
                feedback.reportError("Layer failed to load! [code A2]", True)
                return
            #
            #Check if valid geometry is returned
            ValidGeometry = True
            if tempLayer.featureCount() < 1:
                ValidGeometry = False
            else:
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
                        return
                #
                #Clip layer to polygon
                params = {
                    'INPUT' : tempLayer,
                    'OVERLAY' : Psubset,
                    'OUTPUT' : "memory:"
                }
                tempLayer = processing.run(
                    'native:clip', 
                    params,
                    #is_child_algorithm=True,
                    context=context,
                    feedback=feedback)["OUTPUT"]
                if feedback.isCanceled():
                    return
                #
                # Merging layer with Master copy if the clipped layer still has features
                if tempLayer.featureCount() > 0:
                    params = {
                        'LAYERS' : [tempLayer,NRdata],
                        'OUTPUT' : "memory:"
                    }
                    NRdata = processing.run(
                        'native:mergevectorlayers', 
                        params,
                        #is_child_algorithm=True,
                        context=context,
                        feedback=feedback)["OUTPUT"]
                    if feedback.isCanceled():
                        return
            #End Loop
        if not NRdata.isValid():
                feedback.reportError("Layer failed to load! [code A3]", True)
                return
        if NRdata.featureCount() > 0:
            NRdata.setName(layername)
            #
            #Write layer to shape file and reload layer from shapefile
            TimeString = str(datetime.datetime.now()).replace(':','-').replace(':','-').replace('.','-').replace(' ','-')
            #Save as GeoPackage
            QgsVectorFileWriter.writeAsVectorFormat(NRdata,outputDIR+"/"+layername+TimeString+".gpkg",'utf-8',QgsCoordinateReferenceSystem(standardCRS))
            #Save as Shapefile
            #QgsVectorFileWriter.writeAsVectorFormat(NRdata,outputDIR+"/"+layername+TimeString+".shp",'utf-8',QgsCoordinateReferenceSystem(standardCRS),driverName="ESRI Shapefile")
            #Reload layer
            NRdata = QgsVectorLayer(outputDIR+"/"+layername+TimeString+".gpkg",layername,"ogr")
            if not NRdata.isValid():
                feedback.reportError("Layer failed to load! [code A4]", True)
                return
            # Add styling for NRdata
            NRdata.loadNamedStyle(resolve(layerstyle))
            #
            #Add layer to canvas
            project = QgsProject.instance()
            project.addMapLayer(NRdata, False)
            layerTree = iface.layerTreeCanvasBridge().rootGroup()
            layerTree.insertChildNode(1, QgsLayerTreeLayer(NRdata))
            feedback.setProgressText("OK")
        else:
            feedback.setProgressText("-no data-")
        #
        return


    def processAlgorithm(self, parameters, context, feedback):
        # Set the standard CRS to GDA2020 (EPSG:7844)
        standardCRS = "EPSG:7844"
        #Parse the lot plan numbers
        lots = re.sub('[^0-9a-zA-Z]+', ',', self.parameterAsString(parameters,self.INPUT,context).upper()).split(',')
        #
        #
        lotplans_message = "Lot/Plan(s): "+", ".join(lots)
        feedback.setProgressText(lotplans_message)
        #  
        loadTenure = self.parameterAsBool(parameters,self.LOADTENURE,context)
        loadDSurfG = self.parameterAsBool(parameters,self.LOADDSURFG,context)
        loadDSolG = self.parameterAsBool(parameters,self.LOADDSOLG,context)
        #loadDStruct = self.parameterAsBool(parameters,self.LOADDSTRUCT,context)
        loadRGsurf = self.parameterAsBool(parameters,self.LOADRGSURF,context)
        outputDIR = self.parameterAsFileOutput(parameters,self.OUTPUTDIR,context)
        feedback.setProgress(1)
        # The following lines workaround an apparent QGIS bug where a temporary directory isn't actually made.
        try:
            os.mkdir(outputDIR)
        except FileExistsError as e:
            pass
        layerInfo = dict(   lots = lots,
                            layername = 'Property Boundary',
                            layerstyle = 'LayerStyles/Property.qml',
                            outputDIR = outputDIR,
                            standardCRS = standardCRS,
                            )
        #Get property polygon(s)
        PropertyVlayer = self.LoadPropertyLayer(layerInfo,context,feedback)
        if PropertyVlayer == None or not PropertyVlayer.isValid() or PropertyVlayer.featureCount() < 1:
            feedback.reportError("Failed to load property boundary! Invalid lot/plan? Network or server problems?", True)
            return {}
        #
        feedback.setProgress(3)
        feedback.setProgressText("Property polygon(s) loaded")  
        # Load property layer to canvas
        project = QgsProject.instance()
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
        # Initialise dictionaries
        post = dict(serviceType = "MapServer/",
                    f = 'geojson'
                    )
        layerInfo = dict(   vlayer = PropertyVlayer,
                            outputDIR = outputDIR,
                            standardCRS = standardCRS
                            )
        #
        ################################
        # Get Tenure                   #
        ################################
        if loadTenure:
            feedback.setProgressText("Getting tenure map...")
            post.update(dict(   service1 = "PlanningCadastre/", 
                                service2 = "LandParcelPropertyFramework/",
                                serviceNumber = str(13),
                                serviceType = "MapServer/",
                                f = 'geojson'
                                ))
            layerInfo.update(dict(  layername = "Tenure",
                                    layerstyle = "LayerStyles/QldPropertyTenure.qml",
                                    geomtype = "MultiPolygon"
                                    ))
            self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
            feedback.setProgress(6)
        ################################
        # Get Detailed Surface Geology #
        ################################
        if loadDSurfG:
            post.update(dict(   service1 = "GeoscientificInformation/", 
                                service2 = "GeologyDetailed/",
                                serviceNumber = str(14),
                                geometry = '*',
                                serviceType = "MapServer/",
                                f = 'geojson'
                                ))
            feedback.setProgressText("Getting Detailed surface geology extent...")
            tempLayer = QgsVectorLayer(self.GetGEOJSON(self.BuildQuery(post,context,feedback),context,feedback), "tempLayer", "ogr")
            if not tempLayer.isValid():
                feedback.reportError("Layer failed to load! [code M1]", True)
                return
            #Check if property boundary intersects with Detailed Geology Extent
            params = {
                'INPUT' : tempLayer,
                'OVERLAY' : PropertyVlayer,
                'OUTPUT' : "memory:"
            }
            tempLayer = processing.run(
                'native:intersection', 
                params,
                #is_child_algorithm=True,
                context=context,
                feedback=feedback)["OUTPUT"]
            if feedback.isCanceled():
                return
            #
            if tempLayer.featureCount()!=0:
                feedback.setProgressText("Getting detailed surface geology...")
                post.update(dict(serviceNumber = str(15)))
                LayerName=json.loads(self.GetGEOJSON(self.ItemInfo(post,context,feedback),context,feedback))
                DefaultLayerName = 'Surface geology (1:100k)'
                LayerName=LayerName.get('title',DefaultLayerName)
                layerInfo.update(dict(  layername = LayerName,
                                        layerstyle = "LayerStyles/GeologyDetailedSurface.qml",
                                        geomtype = "MultiPolygon"
                                        ))
                self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
                feedback.setProgress(8)
            else: feedback.reportError("Property outside extent of Detailed Solid Geology mapping",True)
        ##############################
        # Get Detailed Solid Geology #
        ##############################
        if loadDSolG:
            post.update(dict(   service1 = "GeoscientificInformation/", 
                                service2 = "GeologyDetailed/",
                                serviceNumber = str(16),
                                geometry = '*',
                                serviceType = "MapServer/",
                                f = 'geojson'
                                ))
            feedback.setProgressText("Getting detailed solid geology extent...")
            post.update(dict(serviceNumber = str(16)))
            tempLayer = QgsVectorLayer(self.GetGEOJSON(self.BuildQuery(post,context,feedback),context,feedback), "tempLayer", "ogr")
            if not tempLayer.isValid():
                feedback.reportError("Layer failed to load! [code M2]", True)
                return
            #Check if property boundary intersects with Detailed Geology Extent
            params = {
                'INPUT' : tempLayer,
                'OVERLAY' : PropertyVlayer,
                'OUTPUT' : "memory:"
            }
            tempLayer = processing.run(
                'native:intersection', 
                params,
                #is_child_algorithm=True,
                context=context,
                feedback=feedback)["OUTPUT"]
            if feedback.isCanceled():
                return
            #
            if tempLayer.featureCount()!=0:
                feedback.setProgressText("Getting detailed solid geology...")
                post.update(dict(serviceNumber = str(17)))
                LayerName=json.loads(self.GetGEOJSON(self.ItemInfo(post,context,feedback),context,feedback))
                DefaultLayerName = 'Solid geology (1:100k)'
                LayerName=LayerName.get('title',DefaultLayerName)
                layerInfo.update(dict(  layername = LayerName,
                                        layerstyle = "LayerStyles/GeologyDetailedSolid.qml",
                                        geomtype = "MultiPolygon"
                                        ))
                self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
                feedback.setProgress(10)
            else: feedback.reportError("Property outside extent of detailed solid geology mapping",True)
        ###############################
        # Get Regional Geology Extent #
        ###############################
        if loadRGsurf:
            post.update(dict(   service1 = "GeoscientificInformation/", 
                                service2 = "GeologyRegional/",
                                geometry = '*',
                                serviceType = "MapServer/",
                                f = 'geojson'
                                ))
            for i in range(2,16):
                feedback.setProgressText("Getting regional geology extent...")
                post.update(dict(   serviceNumber = str(i),
                                    geometry = '*'
                                    ))
                tempLayer = QgsVectorLayer(self.GetGEOJSON(self.BuildQuery(post,context,feedback),context,feedback), "tempLayer", "ogr")
                if not tempLayer.isValid():
                    feedback.reportError("Layer failed to load! [code M3]", True)
                    return
                #Check if property boundary intersects with Detailed Geology Extent
                params = {
                    'INPUT' : tempLayer,
                    'OVERLAY' : PropertyVlayer,
                    'OUTPUT' : "memory:"
                }
                tempLayer = processing.run(
                    'native:intersection', 
                    params,
                    #is_child_algorithm=True,
                    context=context,
                    feedback=feedback)["OUTPUT"]
                if feedback.isCanceled():
                    return
                #
                feedback.setProgress(12+2*i)
                if tempLayer.featureCount()!=0:
                    for j in range (0,2):
                        k=12+2*i+j
                        feedback.setProgressText("Getting regional geology...")
                        post.update(dict(serviceNumber = str(k)))
                        LayerName=json.loads(self.GetGEOJSON(self.ItemInfo(post,context,feedback),context,feedback))
                        DefaultLayerName = 'RegionalGeology-'+str(k)
                        LayerName=LayerName.get('title',DefaultLayerName)
                        layerInfo.update(dict(  layername = LayerName,
                                                layerstyle = "LayerStyles/RegionalGeology"+str(k)+".qml",
                                                geomtype = "MultiPolygon"
                                                ))
                        if j==0: layerInfo.update(dict(  geomtype = "MultiLineString"))
                        self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
                else: feedback.pushInfo("Property outside extent of regional geology mapping extent ID:"+str(i))
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