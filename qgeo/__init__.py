# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Qgeo
                                 A QGIS plugin
 Loads Queensland geoscience data from the Queensland government feature server.
                              -------------------
        begin                : 2020-10-08
        copyright            : (C) 2020 by Otto Pattemore and Gary Pattemore
        email                : pattemore .dot. software .at. gmail .dot. com
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
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Otto Pattemore and Gary Pattemore'
__date__ = '2020-05-06'
__copyright__ = '(C) 2020 by Otto Pattemore and Gary Pattemore'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Qgeo class from file Qgeo.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgeo import QgeoPlugin
    return QgeoPlugin()
