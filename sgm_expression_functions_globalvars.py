# -*- coding: utf-8 -*-

"""
    ***************************************************************************
    * Plugin name:   SgmExpressionFunctions
    * Plugin type:   QGIS 3 plugin
    * Module:        global variables
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
fnc_title_txt = "Fonctions SIGMOÉ (calculateur d'expression)"

# Help docstings
get_address_doc = """
        Fournit l'adresse d'un point en utilisant l'API Adresse d'Etalab (licence ouverte, utilisable en France uniquement).<br/>
        Cette fonction peut être utilisée sur une couche ponctuelle ou surfacique (dans ce cas, c'est l'adresse du centroïde du polygone qui est calculée).<br/>
        Le paramètre <span class="argument">format</span> permet de formater les différents éléments de l'adresse.<br/>
        Le paramètre obligatoire <span class="argument">distance_limite</span> permet d'indiquer une distance limite pour retenir ou pas l'adresse (adresse non retenue si le point adresse retrouvé est trop éloigné du point du canevas).<br/>
        Cette fonction nécessite un accès Internet.
        <h4>Syntaxe</h4>
        <div class="syntax"><code>
        <span class="functionname">get_address(</span>
        <span class="argument">format, distance_limite</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">format</td><td>format utilisé pour écrire l'adresse.</td></tr>
        <br/>L'argument format est une chaine de caractères qui utilise des mots-clés pour construire le formatage de l'adresse retournée.
        <br/>
        <br/><b>Les mots-clés disponibles sont:</b>
        <br/>'full' : retourne l'adresse complète
        <br/>'num' : retourne le numéro de voirie
        <br/>'rue' : retourne le nom de la rue
        <br/>'cop' : retourne le code postal
        <br/>'vil' : retourne le nom de la commune
        <br/>'ins' : retourne le code INSEE de la commune
        <br/>'nnr' : retourne le numéro de voirie suivi du nom de la rue
        <br/>'id' : retourne l'identifiant de l’adresse (clef d’interopérabilité)
        <br/>'riv' : retourne le code RIVOLI de l'adresse
        <br/>'FULL' : retourne l'adresse complète en lettres majuscules
        <br/>'RUE' : retourne le nom de la rue en lettres majuscules
        <br/>'VIL' : retourne le nom de la commune en lettres majuscules
        <br/>'NNR' : retourne le numéro de voirie suivi du nom de la rue en lettres majuscules
        <tr><td class="argument">distance_limite</td><td>distance limite (en mètres) de prise en compte de l'adresse. Si cette distance limite est positive, l'adresse ne sera conservée que si la distance entre le point original (dans le canevas) et le point adresse trouvé est inférieure à cette distance limite. Si la distance est plus grande que la distance limite, aucune adresse n'est retournée. Si la distance limite spécifiée est -1, toutes les adresses trouvées sont conservées, même si la distance entre le point original (dans le canevas) et le point adresse trouvé est très grande (pas de distance limite).</td></tr>
        </table>
        </code></div>
        <h4>Exemples</h4>
        <!-- Show examples of function.-->
        <div class="examples"><ul>
        <li><code>get_address('full', -1)</code> &rarr; <code>8 rue Dupont 67170 Brumath</code></li>
        <li><code>get_address('full', 20)</code> &rarr; <code>8 rue Dupont 67170 Brumath (adresse retournée uniquement si la distance entre le point original et le point adresse est inférieure à 20 mètres)</code></li>
        <li><code>get_address('num rue - cop VIL', -1)</code> &rarr; <code>8 Rue Dupont - 67170 BRUMATH</code></li>
        <li><code>get_address('NNR', -1)</code> &rarr; <code>8 RUE DUPONT</code></li>
        </ul></div>
    """
x_fromaddress_doc = """
        Retourne l'abscisse (X) du point localisant l'adresse spécifiée en paramètre.
        Cette fonction utilise l'API Adresse d'Etalab (licence ouverte, utilisable en France uniquement).<br/>
        L'abscisse est retournée dans le sytème de coordonnées RGF93-Lambert 93.<br/>
        En deuxième paramètre, vous pouvez spécifier le code INSEE de la commune de l'adresse cherchée (afin de fiabliser la recherche).<br/>
        Cette fonction nécessite un accès Internet.
        <h4>Syntaxe</h4>
        <div class="syntax"><code>
        <span class="functionname">x_fromaddress(</span>
        <span class="argument">adresse [, insee]</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">adresse</td><td>adresse cherchée mise en forme de manière compréhensible (par exemple '3 rue des tilleuls 67000 Strasbourg').</td></tr>
        <tr><td class="argument">insee</td><td>code INSEE de la commune de l'adresse cherchée (par exemple '67482'). Cet argument est optionnel.</td></tr>
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
        Retourne l'ordonnée (Y) du point localisant l'adresse spécifiée en paramètre.
        Cette fonction utilise l'API Adresse d'Etalab (licence ouverte, utilisable en France uniquement).<br/>
        L'abscisse est retournée dans le sytème de coordonnées RGF93-Lambert 93.<br/>
        En deuxième paramètre, vous pouvez spécifier le code INSEE de la commune de l'adresse cherchée (afin de fiabliser la recherche).<br/>
        Cette fonction nécessite un accès Internet.
        <h4>Syntaxe</h4>
        <div class="syntax"><code>
        <span class="functionname">y_fromaddress(</span>
        <span class="argument">adresse [, insee]</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">adresse</td><td>adresse cherchée mise en forme de manière compréhensible (par exemple '3 rue des tilleuls 67000 Strasbourg').</td></tr>
        <tr><td class="argument">insee</td><td>code INSEE de la commune de l'adresse cherchée (par exemple '67482'). Cet argument est optionnel.</td></tr>
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
        Calcule l'angle du segment (provenant de la couche cible target_layer) situé sous l'objet source, avec une tolérance permettant de trouver le bon segment correspondant au point.
        <h4>Syntaxe</h4>
        <div class="syntax"><code>
        <span class="functionname">get_lineangle(</span>
        <span class="argument">target_layer, tolerance</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">target_layer</td><td>nom de la couche cible utilisée pour trouver le segment sous le point. Par exemple 'canas'.</td></tr>
        <tr><td class="argument">tolerance</td><td>tolerance (distance autour du point) utilisée pour trouver le bon segment dans la couche cible.</td></tr>
        </table>
        <i>ATTENTION: Les 2 couches traitées (source et cible) doivent avoir le même SCR assigné.</i>
        </div>
        <h4>Exemples</h4>
        <!-- Show examples of function.-->
        <div class="examples"><ul>
        <li><code>get_lineangle('canas', 0.01)</code></li>
        </ul></div>
    """
geomtouches_startpoint_doc =  """
        Retourne la valeur du champ target_field de l'objet de la couche cible (target_layer) qui touche le premier point de l'objet source.
        Si plus d'un objet est trouvé, retourne une valeur unique composée de la concaténation de chaque valeur séparées par | (liste de valeurs).
        La couche cible (target_layer) doit impérativement être de géométrie ponctuelle, et la couche source de géométrie linéaire.
        <h4>Syntaxe</h4>
        <div class="syntax"><code>
        <span class="functionname">geomtouches_startpoint(</span>
        <span class="argument">target_layer, target_field</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">target_layer</td><td>nom de la couche cible à traiter, par exemple  'Regards'.</td></tr>
        <tr><td class="argument">target_field</td><td>nom du champ de la couche target_layer duquel vous souhaitez récupérer la valeur, par exemple 'numero'.
        <br/>Si target_field contient le nom de plusieurs champs séparés par +, le résulat est la concaténation de la valeur de chaque champ (valeurs séparées par un espace).
        <br/>Si target_field est égal à '$geometry', retoune la géométrie WKT de l'objet trouvé dans la couche cible.
        <br/>Si target_field est égal à '$id' , retoune la numéro de l'objet (id) trouvé dans la couche cible.</td></tr>
        </table>
        <i>Le nombre d'objets traités est limité à 100000 pour éviter un traitement trop long.</i>
        <br/><i>ATTENTION: Les 2 couches traitées (source et cible) doivent avoir le même SCR assigné.</i>
        </div>
        <h4>Exemples</h4>
        <!-- Show examples of function.-->
        <div class="examples"><ul>
        <li><code>geomtouches_startpoint('Regards','cote tampon')</code></li>
        <li><code>geomtouches_startpoint('Regards','identifiant+cote tampon')</code></li>
        <li><code>geomtouches_startpoint('Regards','$geometry')</code></li>
        <li><code>geomtouches_startpoint('Regards','$id')</code></li>
        </ul></div>
    """
geomtouches_endpoint_doc = """
        Retourne la valeur du champ target_field de l'objet de la couche cible (target_layer) qui touche le dernier point de l'objet source.
        Si plus d'un objet est trouvé, retourne une valeur unique composée de la concaténation de chaque valeur séparées par | (liste de valeurs).
        La couche cible (target_layer) doit impérativement être de géométrie ponctuelle, et la couche source de géométrie linéaire.
        <h4>Syntaxe</h4>
        <div class="syntax"><code>
        <span class="functionname">geomtouches_endpoint(</span>
        <span class="argument">target_layer, target_field</span>
        <span class="functionname">)</span>
        </code></div>
        <h4>Arguments</h4>
        <div class="arguments">
        <table>
        <tr><td class="argument">target_layer</td><td>nom de la couche cible à traiter, par exemple  'Regards'.</td></tr>
        <tr><td class="argument">target_field</td><td>nom du champ de la couche target_layer duquel vous souhaitez récupérer la valeur, par exemple 'numero'.
        <br/>Si target_field contient le nom de plusieurs champs séparés par +, le résulat est la concaténation de la valeur de chaque champ (valeurs séparées par un espace).
        <br/>Si target_field est égal à '$geometry', retoune la géométrie WKT de l'objet trouvé dans la couche cible.
        <br/>Si target_field est égal à '$id' , retoune la numéro de l'objet (id) trouvé dans la couche cible.</td></tr>
        </table>
        <i>Le nombre d'objets traités est limité à 100000 pour éviter un traitement trop long.</i>
        <br/><i>ATTENTION: Les 2 couches traitées (source et cible) doivent avoir le même SCR assigné.</i>
        </div>
        <h4>Exemples</h4>
        <!-- Show examples of function.-->
        <div class="examples"><ul>
        <li><code>geomtouches_endpoint('Regards','cote tampon')</code></li>
        <li><code>geomtouches_endpoint('Regards','identifiant+cote tampon')</code></li>
        <li><code>geomtouches_endpoint('Regards','$geometry')</code></li>
        <li><code>geomtouches_endpoint('Regards','$id')</code></li>
        </ul></div>
    """