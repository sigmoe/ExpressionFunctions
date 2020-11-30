# -*- coding: utf-8 -*-
"""
    ***************************************************************************
    * Plugin name:   SgmExpressionFunctions
    * Plugin type:   QGIS 3 plugin
    * Module:        Main
    * Description:   Add custom user functions to QGIS Field calculator. 
    * Specific lib:  None
    * First release: 2018-08-10
    * Last release:  2020-11-30
    * Copyright:     (C)2020 SIGMOE
    * Email:         em at sigmoe.fr
    * License:       GPL v3
    ***************************************************************************
 
    ***************************************************************************
    * This program is free software: you can redistribute it and/or modify
    * it under the terms of the GNU General Public License as published by
    * the Free Software Foundation, either version 3 of the License, or
    * (at your option) any later version.
    *
    * This program is distributed in the hope that it will be useful,
    * but WITHOUT ANY WARRANTY; without even the implied warranty of
    * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    * GNU General Public License for more details.
    *
    * You should have received a copy of the GNU General Public License
    * along with this program. If not, see <http://www.gnu.org/licenses/>.
    *************************************************************************** 
"""

# Import the PyQt and QGIS libraries
from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt, QEventLoop, QUrl, QSettings
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QWidget

from qgis.utils import iface, qgsfunction
from qgis.core import ( QgsNetworkContentFetcher, QgsProject, QgsMapLayer, QgsFeatureRequest,
                        QgsWkbTypes, QgsCoordinateTransform, QgsCoordinateReferenceSystem,
                        QgsRectangle, QgsExpression, QgsPoint)


import os.path
import sys
import math
import json

locale = QSettings().value('locale/userLocale')[0:2]
if locale == 'fr':
    from .sgm_expression_functions_globalvars import *
else:
    from .sgm_expression_functions_globalvars_en import *

gui_dlg_expfnc, _ = uic.loadUiType(
        os.path.join(os.path.dirname(__file__), r"gui/sgm_expressionfunctions_dlg.ui"))

def _getLayerSet():
    return {layer.name():layer for layer in QgsProject.instance().mapLayers().values()}

# Check if 2 points are identical
# digit = number of digit taken into account for the comparison
def check_identical_pts(qgs_pt1, qgs_pt2, digit):
    ret = False
    if round(qgs_pt1.x(), digit) == round(qgs_pt2.x(), digit) and \
        round(qgs_pt1.y(), digit) == round(qgs_pt2.y(), digit):
        ret = True
    return ret
    
# Calculate the distance between 2 points
def dist(pt1, pt2):
    return math.sqrt( (pt2.x() - pt1.x())**2 + (pt2.y() - pt1.y())**2 )
    
# Used for get_address function
def request(url):
    ''' prepare the request and return the result of the reply
    '''
    fetcher = QgsNetworkContentFetcher()
    fetcher.fetchContent(QUrl(url))
    evloop = QEventLoop()
    fetcher.finished.connect(evloop.quit)
    evloop.exec_(QEventLoop.ExcludeUserInputEvents)
    return fetcher.contentAsString()

# Used to add docstring from a variable
def add_doc(value):
    def _doc(func):
        func.__doc__ = value
        return func
    return _doc       


@qgsfunction(args=-1, group="Fonctions SIGMOÉ", register=False, usesgeometry=True, handlesnull=True)
@add_doc(get_address_doc)
def get_address(values, feature, parent):
    dbg=debug()
    dbg.out("evaluating get_address")
    if feature.geometry().type() != QgsWkbTypes.PointGeometry:
        if feature.geometry().type() == QgsWkbTypes.PolygonGeometry :
            ft_pt = feature.geometry().pointOnSurface().asPoint()
        else:
            parent.setEvalErrorString("error: targetLayer is not a point or a polygon layer")
            return
    else:
        ft_pt = feature.geometry().asPoint()
    count = 0
    dminRes = ""
    ad_fmt = {
                'full' : ['{1}', "label"],
                'num' : ['{2}', "housenumber"],
                'rue' : ['{3}', "street"],
                'cop' : ['{4}', "postcode"],
                'vil' : ['{5}', "city"],
                'ins' : ['{6}', "citycode"],
                'nnr' : ['{7}', "name"],
                'FULL' : ['{8}', "label"],
                'RUE' : ['{9}', "street"],
                'VIL' : ['{10}', "city"],
                'NNR' : ['{11}', "name"]
                }
    # Transformation to use to retrieve the coordinates of the point for the API
    trf = QgsCoordinateTransform(iface.mapCanvas().mapSettings().destinationCrs(), 
                                        QgsCoordinateReferenceSystem(4326), QgsProject().instance())
    # Transformation to use to compare the coordinates of the result with the point coordinates
    trf_res = QgsCoordinateTransform(iface.mapCanvas().mapSettings().destinationCrs(), 
                                        QgsCoordinateReferenceSystem(2154), QgsProject().instance())
    ad_pt = trf.transform(ft_pt)
    url = "http://api-adresse.data.gouv.fr/reverse/?lon="+str(ad_pt.x())+"&lat="+str(ad_pt.y())
    result = request(url)
    fmt = values[0]
    # To avoid keywords problems, create a new keyword string to use
    nw_fmt = ''
    for ad_key in ad_fmt:
        if ad_key in fmt:
            nw_key = fmt.replace(ad_key, ad_fmt[ad_key][0])
            fmt = nw_key
    # Create the address
    try:
        data = json.loads(result)     
        # return str(data)
        # Check if the parameter distance exists
        if len(values)==2:
            d_limit =  float(values[1])
        else:
            d_limit =  1000.00   
        if len(data) > 0:
            if len(data["features"]) > 0:
                for ad_val in ad_fmt:
                    if ad_fmt[ad_val][0] in fmt:
                        try:
                            repl_str = data["features"][0]["properties"][ad_fmt[ad_val][1]]
                        except:
                            repl_str = ""
                        if ad_val.isupper():
                            repl_str = repl_str.upper()
                        ret_ad = fmt.replace(ad_fmt[ad_val][0], repl_str)
                        fmt = ret_ad
                # Calculate the distance betweew the original point in the canvas and the point
                # of the address
                ad_realpt = QgsPoint( data["features"][0]["properties"]["x"],
                                        data["features"][0]["properties"]["y"])
                ad_oript = trf_res.transform(ft_pt)
                d = dist(ad_realpt,ad_oript)
                # Return the address only if the distance calculated is under 
                # the limit distance (2nd param)
                if d <= d_limit:
                    return fmt
                else:
                    return None
            else:
                return None
        else:
            return None
    except ValueError:
        parent.setEvalErrorString("error: network problem (check your network settings: proxy) or coordinates problems")
        

@qgsfunction(args=-1, group="Fonctions SIGMOÉ", register=False, usesgeometry=True, handlesnull=True)
@add_doc(x_fromaddress_doc)
def x_fromaddress(values, feature, parent):
    dbg=debug()
    dbg.out("evaluating get_address")
    adr = values[0].replace(',', ' ').replace(' ', '%20')
    if len(values)==2:
        insee = str(values[1])
        url = "http://api-adresse.data.gouv.fr/search/?q="+adr+"&citycode="+insee
    else:
        url = "http://api-adresse.data.gouv.fr/search/?q="+adr
    result = request(url)
    
    try:
        data = json.loads(result)     
        # return str(data)
        if len(data["features"]) > 0:
            try:
                return data["features"][0]["properties"]["x"]
            except:
                return None
        else:
            return None
    except ValueError:
        parent.setEvalErrorString("error: check your network settings (proxy)")


@qgsfunction(args=-1, group="Fonctions SIGMOÉ", register=False, usesgeometry=True)
@add_doc(y_fromaddress_doc)
def y_fromaddress(values, feature, parent):
    dbg=debug()
    dbg.out("evaluating get_address")
    adr = values[0].replace(',', ' ').replace(' ', '%20')
    if len(values)==2:
        insee = str(values[1])
        url = "http://api-adresse.data.gouv.fr/search/?q="+adr+"&citycode="+insee
    else:
        url = "http://api-adresse.data.gouv.fr/search/?q="+adr
    result = request(url)
    
    try:
        data = json.loads(result)     
        # return str(data)
        if len(data["features"]) > 0:
            try:
                return data["features"][0]["properties"]["y"]
            except:
                return None
        else:
            return None
    except ValueError:
        parent.setEvalErrorString("error: check your network settings (proxy)")
        

@qgsfunction(2, "Fonctions SIGMOÉ", register=False, usesgeometry=True)
@add_doc(get_lineangle_doc)
def get_lineangle(values, feature, parent):
    layername = values[0]
    tol = values[1]
    layerSet = _getLayerSet()
    if not layername in layerSet.keys():
        parent.setEvalErrorString("Erreur: couche inexistante")
        return
    line_lyr  = layerSet[layername]
    if not feature.geometry():
        return 0.0
    else:
        ptf = feature.geometry().asPoint()
        x_pt = ptf.x()
        y_pt = ptf.y()

        # Create the rectangle of the search area
        search_rect = QgsRectangle(x_pt - tol, y_pt - tol,  x_pt + tol, y_pt + tol)

        # Find the polyline under the point 
        # and calculate the angle of the segment under the point
        ret = 0.0
        for polyline in line_lyr.getFeatures(QgsFeatureRequest().setFilterRect(search_rect)):
            dist, ptcl, ida, side =  polyline.geometry().closestSegmentWithContext(ptf)
            pt1 = ptcl
            pt2 = polyline.geometry().vertexAt(ida)
            # Special case when the point is on the last point of the polyline
            if check_identical_pts(pt1, pt2, 3):
                pt1 = polyline.geometry().vertexAt(ida-1)
            # Calculate the angle (in degrees)
            ang = math.atan2(pt2.x() - pt1.x(), pt2.y() - pt1.y()) / math.pi * 180
            ret = ang
        return ret
        

class debug:

    def __init__(self):
        self.debug = None

    def out(self,string):
        if self.debug:
            print(string)


# Manage the about window
class ExpFncDlg(QWidget, gui_dlg_expfnc):
    
    # Initialization
    def __init__(self, parent=None):
        super(ExpFncDlg, self).__init__(parent)
        self.setupUi(self)
        # Delete Widget on close event
        # self.setAttribute(Qt.WA_DeleteOnClose)


class sgmExpFunctions:

    def __init__(self, iface):
        self.iface = iface
        # Find plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        self.dbg = debug()
        self.dlg = ExpFncDlg()


    def initGui(self):
        self.dbg.out("initGui")
        QgsExpression.registerFunction(get_address)
        QgsExpression.registerFunction(get_lineangle)
        QgsExpression.registerFunction(x_fromaddress)
        QgsExpression.registerFunction(y_fromaddress)
               
        # Add Sigmoe toolbar
        self.toolbar = self.iface.addToolBar(mnu_title_txt)
        self.toolbar.setObjectName("SgmExpressionFunctions")
        # Create actions
        icon_path = os.path.join(self.plugin_dir,"icons/sgm_expfnc_i.png")
        icon = QIcon(icon_path)
        self.about_action = QAction(icon, fnc_title_txt, self.iface.mainWindow())              
        # Add actions to the toolbar
        self.toolbar.addActions([self.about_action])
        # Manage signals
        self.about_action.triggered.connect(self.about)


    def unload(self):
        QgsExpression.unregisterFunction('get_address')
        QgsExpression.unregisterFunction('get_lineangle')
        QgsExpression.unregisterFunction('x_fromaddress')
        QgsExpression.unregisterFunction('y_fromaddress')
        
        self.iface.mainWindow().removeToolBar(self.toolbar)

    def about(self):
        self.dlg.show()
