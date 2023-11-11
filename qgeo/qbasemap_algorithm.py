# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Qbasemap
                                 A QGIS plugin
 Load basemaps from the Queensland governments feature and map servers
                              -------------------
        begin                : 2020-05-06
        updated              : 2021-04-25
        updated              : 2023-04-11
        updated              : 2023-07-15
        updated              : 2023-11-12
        copyright            : (C) 2023 by Gary Pattemore and Otto Pattemore
        email                : variatursoftware .at. gmail .dot. com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Gary Pattemore and Otto Pattemore'
__date__ = '2023-11-12'
__copyright__ = '(C) 2023 by Gary Pattemore and Otto Pattemore'

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
from .query import resolve
#

class QbasemapAlgorithm(QgsProcessingAlgorithm):
    #INPUT = 'INPUT'
    #OUTPUTDIR = 'OUTPUTDIR'
    LOADSATHR = "LOADSATHR"
    LOADGOOGLE = "LOADGOOGLE"
    LOADOSM = "LOADOSM"
    LOADESRIHR = "LOADESRIHR"
    LOADBASECOLOUR = "LOADBASECOLOUR"
    LOADSTATEBORDER = "LOADSTATEBORDER"
    LOADMAPLABELS = "LOADMAPLABELS"
    LOADKOALAPA = "LOADKOALAPA"
    LOADLGA = "LOADLGA"
    LOADDSGE = "LOADDSGE"
    LOADDSOLIDGE = "LOADDSOLIDGE"
    def initAlgorithm(self, config):
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADSATHR,
                self.tr('Imagery -QSat- Planet 2017, 3rd quarter'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADGOOGLE,
                self.tr('Imagery -Google- high resolution'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADESRIHR,
                self.tr('Imagery -ESRI- high resolution'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADOSM,
                self.tr('Basemap -Open Street Map'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADBASECOLOUR,
                self.tr('Basemap - colour, updated May and November each year')
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADSTATEBORDER,
                self.tr('Overlay - state border')
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADMAPLABELS,
                self.tr('Overlay - map labels (useful over imagery)'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADLGA,
                self.tr('Overlay - Local government areas'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADDSGE,
                self.tr('Extent of Detailed Surface Geology mapping (1:100,000)'),
                False
            )
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                self.LOADDSOLIDGE,
                self.tr('Extent of Detailed Solid Geology mapping (1:100,000)'),
                False
            )
        )
    #
    def processAlgorithm(self, parameters, context, feedback):
        loadSatHR = self.parameterAsBool(parameters,self.LOADSATHR,context)
        loadGoogle = self.parameterAsBool(parameters,self.LOADGOOGLE,context)
        loadESRIHR = self.parameterAsBool(parameters,self.LOADESRIHR,context)
        loadOSM = self.parameterAsBool(parameters,self.LOADOSM,context)
        loadBaseColour = self.parameterAsBool(parameters,self.LOADBASECOLOUR,context)
        loadMapLabels = self.parameterAsBool(parameters,self.LOADMAPLABELS,context)
        loadStateBorder = self.parameterAsBool(parameters,self.LOADSTATEBORDER,context)
        loadLocalGovBoundaries = self.parameterAsBool(parameters,self.LOADLGA,context)
        loadDSGE = self.parameterAsBool(parameters,self.LOADDSGE,context)
        loadDSOLIDGE = self.parameterAsBool(parameters,self.LOADDSOLIDGE,context)
        #
        # Set up some layer rendering basics
        project = QgsProject.instance()
        root = project.layerTreeRoot()
        feedback.setProgress(10)
        #
        if loadLocalGovBoundaries:
            feedback.setProgressText("Getting local government boundaries...")
            QgsLayerDefinition().loadLayerDefinition(resolve('LayerDefinitions/LocalGovBoundaries.qlr'), project, root)
            feedback.setProgress(15)
        if loadDSGE:
            feedback.setProgressText("Getting Extent of Detailed Surface Geology mapping...")
            QgsLayerDefinition().loadLayerDefinition(resolve('LayerDefinitions/DetailedSurfaceGeologyExtent.qlr'), project, root)
            feedback.setProgress(16)
        if loadDSOLIDGE:
            feedback.setProgressText("Getting Extent of Detailed Solid Geology mapping...")
            QgsLayerDefinition().loadLayerDefinition(resolve('LayerDefinitions/DetailedSolidGeologyExtent.qlr'), project, root)
            feedback.setProgress(17)
        if loadStateBorder:
            feedback.setProgressText("Getting state border overlay...")
            QgsLayerDefinition().loadLayerDefinition(resolve('LayerDefinitions/QldStateBorder.qlr'), project, root)
            feedback.setProgress(20)
        if loadMapLabels:
            feedback.setProgressText("Getting label overlay...")
            QgsLayerDefinition().loadLayerDefinition(resolve('LayerDefinitions/QldMapLabels.qlr'), project, root)
            feedback.setProgress(30)
        if loadSatHR:
            feedback.setProgressText("Getting Qld government HiRes imagery...")
            QgsLayerDefinition().loadLayerDefinition(resolve('LayerDefinitions/Qsat.qlr'), project, root)
            feedback.setProgress(50)
        if loadGoogle:
            feedback.setProgressText("Getting Google Hybrid imagery...")
            QgsLayerDefinition().loadLayerDefinition(resolve('LayerDefinitions/GoogleHybrid.qlr'), project, root)
            feedback.setProgress(55)
        if loadESRIHR:
            feedback.setProgressText("Getting ESRI HiRes imagery...")
            QgsLayerDefinition().loadLayerDefinition(resolve('LayerDefinitions/ESRI_30cm_satellite.qlr'), project, root)
            feedback.setProgress(60)
        if loadBaseColour:
            feedback.setProgressText("Getting colour basemap...")
            QgsLayerDefinition().loadLayerDefinition(resolve('LayerDefinitions/QldColourBasemap.qlr'), project, root)
            feedback.setProgress(70)
        if loadOSM:
            feedback.setProgressText("Getting Open Street Map...")
            QgsLayerDefinition().loadLayerDefinition(resolve('LayerDefinitions/OSM.qlr'), project, root)
            feedback.setProgress(80)
        feedback.setProgress(100)
        return {}
    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Basemaps'

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
        return 'Imagery and basemaps'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return QbasemapAlgorithm()
    
    def icon(self):
        return QIcon(resolve("basemap.png"))
    
    def flags(self):
        return super().flags() | QgsProcessingAlgorithm.FlagNoThreading

