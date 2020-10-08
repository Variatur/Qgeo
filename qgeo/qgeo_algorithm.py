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
    #LOADSUPPORTINGMAP = "LOADSUPPORTINGMAP"
    #LOADPRECLEARMAP = "LOADPRECLEARMAP"
    LOADDSG = "LOADDSG"
    #LOADPMAV = "LOADPMAV"
    #LOADESSHAB = "LOADESSHAB"
    #LOADWETLANDS = "LOADWETLANDS"
    #LOADVMWATER8 = "LOADVMWATER8"
    #LOADVMWATER7 = "LOADVMWATER7"
    #LOADPPTM = "LOADPPTM"
    #LOADKPA = "LOADKPA"
    #LOADKHA = "LOADKHA"
    #LOADKHAL = "LOADKHAL"
    #LOADKRA = "LOADKRA"
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
                self.LOADDSG,
                self.tr('Detailed surface geology (1:100,000) - not available in all areas'),
                False
            )
        )
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADPRECLEARMAP,
        #        self.tr('Pre-clear regional ecosystem map, using RE classes of VMA s22LA-LC (used for VM purposes, eg. determining exchange areas)'),
        #        False
        #    )
        #)
        self.addParameter(
            QgsProcessingParameterFolderDestination(
                self.OUTPUTDIR,
                self.tr("Directory to save output files")
            )
        )
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADRVM,
        #        self.tr('RVM map (Regulated Vegetation Management map, VMA s20A)'),
        #        False
        #    )
        #)
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADPMAV,
        #        self.tr('PMAV (Property Map of Assessable Vegetation, VMA s20AK)'),
        #        False
        #    )
        #)
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADESSHAB,
        #        self.tr('Essential Habitat (VMA s20AC)'),
        #        False
        #    )
        #)
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADWETLANDS,
        #        self.tr('Wetlands (VMA, s20AA)'),
        #        False
        #    )
        #)
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADVMWATER8,
        #        self.tr('VM Water courses 1:25000 SEQ (VMA s20AB)'),
        #        False
        #    )
        #)
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADVMWATER7,
        #        self.tr('VM Water courses 1:100,000 or 1:250,000 (VMA s20AB)'),
        #        False
        #    )
        #)           
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADPPTM,
        #        self.tr('Protected Plant Trigger Map'),
        #        False
        #    )
        #)
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADKPA,
        #        self.tr('Koala Priority Area'),
        #        False
        #    )
        #)
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADKHA,
        #        self.tr('Core Koala Habitat Area'),
        #        False
        #    )
        #)
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADKHAL,
        #        self.tr('Locally refined Koala Habitat Area - used by local govt'),
        #        False
        #    )
        #)
        #self.addParameter(
        #    QgsProcessingParameterBoolean(
        #        self.LOADKRA,
        #        self.tr('Koala Restoration Area'),
        #        False
        #    )
        #)
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
        baseURL = "https://gisservices.information.qld.gov.au/arcgis/rest/"
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
        geometry = post.get('geometry', '')
        # Build
        serviceURL = "services/"+service1+service2+serviceType
        whereURL = serviceNumber+"/query?where="+where+"&objectIds="+objectIds+"&time="
        geomURL = "&geometry="+geometry+"&geometryType="+geometryType+"&inSR="+inSR+"&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Meter&relationParam="
        out1URL = "&outFields="+outFields+"&returnGeometry="+returnGeometry+"&maxAllowableOffset=&geometryPrecision=&outSR="+outSR+"&having=&gdbVersion=&historicMoment=&returnDistinctValues=false"
        out2URL = "&returnIdsOnly="+returnIdsOnly+"&returnCountOnly="+returnCountOnly+"&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics="
        out3URL = "&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnExceededLimitFeatures=false"
        out4URL = "&quantizationParameters=&returnCentroid=false&sqlFormat=none&resultType=&featureEncoding=esriDefault&f="+f
        queryURL = baseURL+serviceURL+whereURL+serviceNumber+geomURL+out1URL+out2URL+out3URL+out4URL
        # --following line to be deleted
        #print(queryURL)
        return queryURL
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
        print(PropertyLayer)
        QgsVectorFileWriter.writeAsVectorFormat(PropertyLayer,outputDIR+"/Property"+TimeString+".gpkg",'utf-8',QgsCoordinateReferenceSystem(standardCRS))
        #Save as shapefile 
        QgsVectorFileWriter.writeAsVectorFormat(PropertyLayer,outputDIR+"/Property"+TimeString+".shp",'utf-8',QgsCoordinateReferenceSystem(standardCRS),driverName="ESRI Shapefile")
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
        loadDSG = self.parameterAsBool(parameters,self.LOADDSG,context)
        #loadPreClearMap = self.parameterAsBool(parameters,self.LOADPRECLEARMAP,context)
        #loadRVM = self.parameterAsBool(parameters,self.LOADRVM,context)
        #loadPMAV = self.parameterAsBool(parameters,self.LOADPMAV,context)
        #loadEssHab = self.parameterAsBool(parameters,self.LOADESSHAB,context)
        #loadPPTM = self.parameterAsBool(parameters,self.LOADPPTM,context)
        #loadWetlands = self.parameterAsBool(parameters,self.LOADWETLANDS,context)
        #loadVMWater8 = self.parameterAsBool(parameters,self.LOADVMWATER8,context)
        #loadVMWater7 = self.parameterAsBool(parameters,self.LOADVMWATER7,context)
        #loadKoalaPA = self.parameterAsBool(parameters,self.LOADKPA,context)
        #loadKoalaHA = self.parameterAsBool(parameters,self.LOADKHA,context)
        #loadKoalaRA = self.parameterAsBool(parameters,self.LOADKRA,context)
        #loadKoalaHAL = self.parameterAsBool(parameters,self.LOADKHAL,context)
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
        feedback.setProgress(15)
        feedback.setProgressText("Property polygon(s) loaded")  
        # Load property layer to canvas
        project = QgsProject.instance()
        project.addMapLayer(PropertyVlayer, False)
        layerTree = iface.layerTreeCanvasBridge().rootGroup()
        layerTree.insertChildNode(0, QgsLayerTreeLayer(PropertyVlayer))
        feedback.setProgress(20)
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
        #Load Natural Resource layers
        if loadTenure:
            feedback.setProgressText("Getting tenure map...")
            post.update(dict(   service1 = "PlanningCadastre/", 
                                service2 = "LandParcelPropertyFramework/",
                                serviceNumber = str(13)
                                ))
            layerInfo.update(dict(  layername = "Tenure",
                                    layerstyle = "LayerStyles/QldPropertyTenure.qml",
                                    geomtype = "MultiPolygon"
                                    ))
            self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
            feedback.setProgress(25)
        # Update server details
        post.update(dict(   service1 = "GeoscientificInformation/", 
                            service2 = "GeologyDetailed/"
                            ))
        #Get Detailed Geology Extent
        feedback.setProgressText("Getting Detailed geology extent...")
        post.update(dict(serviceNumber = str(14)))
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
        #
        if loadDSG & tempLayer.featureCount()!=0:
            feedback.setProgressText("Getting detailed surface geology...")
            post.update(dict(serviceNumber = str(15)))
            layerInfo.update(dict(  layername = "Geology Detailed",
                                    layerstyle = "LayerStyles/GeologyDetailed.qml",
                                    geomtype = "MultiPolygon"
                                    ))
            self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
            feedback.setProgress(30)
        else: feedback.reportError("Property outside extent of Detailed Geology mapping",True)
        #if loadPreClearMap:
        #    feedback.setProgressText("Getting pre-clear regional ecosystem map...")
        #    post.update(dict(serviceNumber = str(15)))
        #    layerInfo.update(dict(  layername = "Pre-clear RE map (VM edition)",
        #                            layerstyle = "LayerStyles/PreClearMap.qml",
        #                            geomtype = "MultiPolygon"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(35)
        #if loadRVM:
        #    feedback.setProgressText("Getting RVM...")
        #    post.update(dict(serviceNumber = str(109)))
        #    layerInfo.update(dict(  layername = "RVM",
        #                            layerstyle = "LayerStyles/RVM.qml",
        #                            geomtype = "MultiPolygon"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(40)
        #if loadPMAV:
        #    feedback.setProgressText("Getting PMAV...")
        #    post.update(dict(serviceNumber = str(146)))
        #    layerInfo.update(dict(  layername = "PMAV",
        #                            layerstyle = "LayerStyles/PMAV.qml",
        #                            geomtype = "MultiPolygon"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(50)
        #if loadEssHab:
        #    feedback.setProgressText("Getting Essential Habitat map...")
        #    post.update(dict(serviceNumber = str(5)))
        #    layerInfo.update(dict(  layername = "Essential Habitat",
        #                            layerstyle = "LayerStyles/EssentialHabitat.qml",
        #                            geomtype = "MultiPolygon"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(60)
        #if loadWetlands:
        #    feedback.setProgressText("Getting Wetlands map...")
        #    post.update(dict(serviceNumber = str(4)))
        #    layerInfo.update(dict(  layername = "Wetlands",
        #                            layerstyle = "LayerStyles/Wetlands.qml",
        #                            geomtype = "MultiPolygon"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(70)
        #if loadVMWater8:
        #    feedback.setProgressText("Getting 1:25000 (SEQ) Watercourse map...")
        #    post.update(dict(serviceNumber = str(8)))
        #    layerInfo.update(dict(  layername = "VM Watercourses-SEQ)",
        #                            layerstyle = "LayerStyles/VMWaterCourse.qml",
        #                            geomtype = "MultiLineString"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(80)
        #if loadVMWater7:
        #    feedback.setProgressText("Getting Qld Watercourse map...")
        #    post.update(dict(serviceNumber = str(7)))
        #    layerInfo.update(dict(  layername = "VM Watercourses QLD",
        #                            layerstyle = "LayerStyles/VMWaterCourse.qml",
        #                            geomtype = "MultiLineString"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(90)    
        #if loadPPTM:
        #    feedback.setProgressText("Getting Protected Plant Trigger Map...")
        #    post.update(dict(serviceNumber = str(201)))
        #    layerInfo.update(dict(  layername = "Protected Plant Trigger Map",
        #                            layerstyle = "LayerStyles/PPTM.qml",
        #                            geomtype = "MultiPolygon"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(94)
        ## Update server details
        #post.update(dict(   service1 = "Environment/", 
        #                    service2 = "KoalaPlan/"
        #                    ))
        #if loadKoalaPA:
        #    feedback.setProgressText("Getting Koala Priority Area...")
        #    post.update(dict(serviceNumber = str(1)))
        #    layerInfo.update(dict(  layername = "Koala Priority Area",
        #                            layerstyle = "LayerStyles/KoalaPriorityArea.qml",
        #                            geomtype = "MultiPolygon"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(95)
        #if loadKoalaHA:
        #    feedback.setProgressText("Getting Koala Habitat Area-core...")
        #    post.update(dict(serviceNumber = str(3)))
        #    layerInfo.update(dict(  layername = "Koala Habitat Area-core",
        #                            layerstyle = "LayerStyles/KoalaHabitatArea-core.qml",
        #                            geomtype = "MultiPolygon"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(96)
        #if loadKoalaRA:
        #    feedback.setProgressText("Getting Koala Restoration Area...")
        #    post.update(dict(serviceNumber = str(6)))
        #    layerInfo.update(dict(  layername = "Koala Restoration Area",
        #                            layerstyle = "LayerStyles/KoalaHabitatRestorationArea.qml",
        #                            geomtype = "MultiPolygon"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(97)
        #if loadKoalaHAL:
        #    feedback.setProgressText("Getting Koala Habitat Area-locally refined...")
        #    post.update(dict(serviceNumber = str(5)))
        #    layerInfo.update(dict(  layername = "Koala Habitat Area-locally refined",
        #                            layerstyle = "LayerStyles/KoalaHabitatArea-LocallyRefined.qml",
        #                            geomtype = "MultiPolygon"
        #                            ))
        #    self.LoadNaturalResourceLayer(post,layerInfo,context,feedback)
        #    feedback.setProgress(98)
        ##
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