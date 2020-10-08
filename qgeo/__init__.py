# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Qgeo
                                 A QGIS plugin
 Loads Queensland geoscience data from the Queensland government feature server.
                              -------------------
        begin                : 2020-10-08
        copyright            : (C) 2020 by Otto and Gary Pattemore
        email                : g .dot. pattemore .at. gmail .dot. com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Otto and Gary Pattemore'
__date__ = '2020-05-06'
__copyright__ = '(C) 2020 by Otto and Gary Pattemore'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Qgeo class from file Qgeo.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgeo import QgeoPlugin
    return QgeoPlugin()
