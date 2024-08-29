# -*- coding: utf-8 -*-

"""
    ***************************************************************************
    * Plugin name:   SgmExpressionFunctions
    * Plugin type:   QGIS 3 plugin
    * Module:        global variables(english version)
    * Description:   Add custom user functions to QGIS Field calculator. 
    * Specific lib:  None
    * First release: 2018-08-10
    * Last release:  2024-08-29
    * Copyright:     (C)2024 SIGMOE
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

# Interface messages
mnu_title_txt = "Fonctions SIGMOÉ"
fnc_title_txt = "Fonctions SIGMOÉ (expression builder)"

# Help docstings
get_address_doc = """
        Provides the address of a point using French Etalab API Adresse (open license, usable in France only).<br/>
        This function can be used on a point or surface layer (in this case, the address of the centroid of the polygon is calculated).<br/>
        The parameter <span class="argument">format</span> allows to format the different elements of the address.<br/>
        The mandatory parameter <span class="argument">distance_limite</span> allows to indicate a limit distance to retain or not to retain the address (address not retained if the found address point is too far from the canvas point).
        This function requires Internet access.
        <h4>Syntax</h4>
        <div class="syntax"><code>
        <span class="functionname">get_address(</span>
        <span class="argument">format, distance_limite</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">format</td><td>the format used to write the address.</td></tr>
        <br/>The format argument is a string value that uses keywords to write the different parts of the address.
        <br/>
        <br/><b>The possible keywords are:</b>
        <br/>full : returns the full address
        <br/>num : returns the house number
        <br/>rue : returns the street name
        <br/>cop : returns the postcode
        <br/>vil : returns the city name
        <br/>ins : returns the INSEE code
        <br/>nnr : returns the house number followed by the streetname
        <br/>'id' : returns the address identifier (interoperability key)
        <br/>'riv' : returns the RIVOLI code of the address
        <br/>FULL : returns the full address in capital letters
        <br/>RUE : returns the street name in capital letters
        <br/>VIL : returns the city name in capital letters
        <br/>NNR : returns the house number followed by the streetname in capital letters
        <tr><td class="argument">distance_limite</td><td>limit distance (in meters) for taking into account the address. If this limit distance is positive, the address will only be kept if the distance between the original point (in the canvas) and the found address point is less than this limit distance. If the distance is greater than the distance limit, no address is returned. If the specified limit distance is -1, all addresses found are kept, even if the distance between the original point (in the canvas) and the found address point is very large (no limit distance).</td></tr>
        </table>
        </code></div>
        <h4>Examples</h4>
        <!-- Show examples of function.-->
        <div class="examples"><ul>
        <li><code>get_address('full', -1)</code> &rarr; <code>8 rue Dupont 67170 Brumath</code></li>
        <li><code>get_address('full', 20)</code> &rarr; <code>8 rue Dupont 67170 Brumath (address returned only if the distance between the original point and the address point is less than 20 metres)</code></li>
        <li><code>get_address('num rue - cop VIL', -1)</code> &rarr; <code>8 Rue Dupont - 67170 BRUMATH</code></li>
        <li><code>get_address('NNR', -1)</code> &rarr; <code>8 RUE DUPONT</code></li>
        </ul></div>
    """
x_fromaddress_doc = """
        Returns the abscissa (X) of the point locating the address specified in parameter.
        This function uses French Etalab API Adresse (open license, usable in France only).<br/>
        The abscissa is returned in the RGF93-Lambert 93 coordinate system.<br/>
        As a second parameter, you can specify the INSEE code of the town of the address you are looking for (in order to make the search more reliable).<br/>
        This function requires Internet access.
        <h4>Syntaxe</h4>
        <div class="syntax"><code>
        <span class="functionname">x_fromaddress(</span>
        <span class="argument">adresse [, insee]</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">adresse</td><td>address searched in an understandable format (e.g. '3 rue des tilleuls 67000 Strasbourg').</td></tr>
        <tr><td class="argument">insee</td><td>INSEE code of the municipality of the address searched for (e.g. '67482'). This argument is optional.</td></tr>
        </table>
        </code></div>
        <h4>Exemples</h4>
        <!-- Show examples of function.-->
        <div class="examples"><ul>
        <li><code>x_fromaddress('3 rue des tilleuls 67000 Strasbourg')</code> &rarr; <code>1052350.3</code></li>
        <li><code>x_fromaddress('3 rue des tilleuls 67000 Strasbourg','67482')</code> &rarr; <code>1052350.3</code></li>
        </ul></div>
    """
y_fromaddress_doc = """
        Returns the ordinate (Y) of the point locating the address specified in parameter.
        This function uses French Etalab API Adresse (open license, usable in France only).<br/>
        The abscissa is returned in the RGF93-Lambert 93 coordinate system.<br/>
        As a second parameter, you can specify the INSEE code of the town of the address you are looking for (in order to make the search more reliable).<br/>
        This function requires Internet access.
        <h4>Syntaxe</h4>
        <div class="syntax"><code>
        <span class="functionname">y_fromaddress(</span>
        <span class="argument">adresse [, insee]</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">adresse</td><td>address searched in an understandable format (e.g. '3 rue des tilleuls 67000 Strasbourg').</td></tr>
        <tr><td class="argument">insee</td><td>INSEE code of the municipality of the address searched for (e.g. '67482'). This argument is optional.</td></tr>
        </table>
        </code></div>
        <h4>Exemples</h4>
        <!-- Show examples of function.-->
        <div class="examples"><ul>
        <li><code>y_fromaddress('3 rue des tilleuls 67000 Strasbourg')</code> &rarr; <code>6844864.59</code></li>
        <li><code>y_fromaddress('3 rue des tilleuls 67000 Strasbourg','67482')</code> &rarr; <code>6844864.59</code></li>
        </ul></div>
    """
get_lineangle_doc = """
        Find the angle of the segment (from the target_layer) located under the point of the source layer, with a tolerance to find the segment corresponding to the point.
        <h4>Syntax</h4>
        <div class="syntax"><code>
        <span class="functionname">get_lineangle(</span>
        <span class="argument">target_layer, tolerance</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">target_layer</td><td>the name of a currently loaded layer, for example 'myLayer'.</td></tr>
        <tr><td class="argument">tolerance</td><td>tolerance (distance around the point) used to find the segment in the target_layer.</td></tr>
        </table>
        <i>WARNING: The 2 processed layers (source and target) must have the same assignedCRS.</i>
        </div>
        <h4>Examples</h4>
        <!-- Show examples of function.-->
        <div class="examples"><ul>
        <li><code>get_lineangle('cana', 0.01)</code></li>
        </ul></div>
    """
geomtouches_startpoint_doc =  """
        Returns the value of the target_field of the target layer object (target_layer) that touches the first point of the source object.
        If more than one object is found, returns a single value composed of the concatenation of each value separated by | (list of values).
        The target layer (target_layer) must be of point geometry, and the source layer of line geometry.
        <h4>Syntax</h4>
        <div class="syntax"><code>
        <span class="functionname">geomtouches_startpoint(</span>
        <span class="argument">target_layer, target_field</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">target_layer</td><td>name of the target layer to process, for example 'Regards'.</td></tr>
        <tr><td class="argument">target_field</td><td>name of the target_layer field from which you want to retrieve the value, for example 'numero'.
        <br/>If target_field contains the name of several fields separated by +, the result is the concatenation of the value of each field (values separated by a space).
        <br/>If target_field is equal to '$geometry', returns the WKT geometry of the object found in the target layer.
        <br/>If target_field is equal to '$id' , returns the object number (id) found in the target layer.</td></tr>
        </table>
        <i>The number of objects processed is limited to 100000 to avoid excessively long processing.</i>
        <br/><i>ATTENTION: The 2 processed layers (source and target) must have the same CRS assigned.</i>
        </div>
        <h4>Examples</h4>
        <!-- Show examples of function.-->
        <div class="examples"><ul>
        <li><code>geomtouches_startpoint('Regards','cote tampon')</code></li>
        <li><code>geomtouches_startpoint('Regards','identifiant+cote tampon')</code></li>
        <li><code>geomtouches_startpoint('Regards','$geometry')</code></li>
        <li><code>geomtouches_startpoint('Regards','$id')</code></li>
        </ul></div>
    """
geomtouches_endpoint_doc = """
        Returns the value of the target_field of the target layer object (target_layer) that touches the end point of the source object.
        If more than one object is found, returns a single value composed of the concatenation of each value separated by | (list of values).
        The target layer (target_layer) must be of point geometry, and the source layer of line geometry.
        <h4>Syntax</h4>
        <div class="syntax"><code>
        <span class="functionname">geomtouches_endpoint(</span>
        <span class="argument">target_layer, target_field</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">target_layer</td><td>name of the target layer to process, for example 'Regards'.</td></tr>
        <tr><td class="argument">target_field</td><td>name of the target_layer field from which you want to retrieve the value, for example 'numero'.
        <br/>If target_field contains the name of several fields separated by +, the result is the concatenation of the value of each field (values separated by a space).
        <br/>If target_field is equal to '$geometry', returns the WKT geometry of the object found in the target layer.
        <br/>If target_field is equal to '$id' , returns the object number (id) found in the target layer.</td></tr>
        </table>
        <i>The number of objects processed is limited to 100000 to avoid excessively long processing.</i>
        <br/><i>ATTENTION: The 2 processed layers (source and target) must have the same CRS assigned.</i>
        </div>
        <h4>Examples</h4>
        <!-- Show examples of function.-->
        <div class="examples"><ul>
        <li><code>geomtouches_endpoint('Regards','cote tampon')</code></li>
        <li><code>geomtouches_endpoint('Regards','identifiant+cote tampon')</code></li>
        <li><code>geomtouches_endpoint('Regards','$geometry')</code></li>
        <li><code>geomtouches_endpoint('Regards','$id')</code></li>
        </ul></div>
    """