# ExpressionFunctions
QGIS 3 Plugin : add functions to use in the expression builder

Description
===========
**ExpressionFunctions** is a QGIS plugin that provides new functions usable for automatic calculation in the expression builder (calculation of the address of a point, orientation angle of a segment under a point, ...). The address calculation functions use Etalab's Adresse API (works only in France).

French description
==================
**ExpressionFunctions** est une extension QGIS qui fournit des fonctions supplémentaires au calculateur d'expressions QGIS (calcul de l'adresse d'un point, angle d'orientation d'un segment sous un point, ...). Les fonctions de calcul d'adresse utilisent l'API Adresse d'Etalab (fonctionne uniquement en France).

Prerequisite
============
* QGIS 3.16 LTR

Documentation
=============
See the video (in French): https://youtu.be/drrnjESjwUM

List of functions available in the expression builder:
* **get_address** : Provides the address of a point using French Etalab API Adresse (open license, usable in France only).
* **x_fromaddress** : Returns the abscissa (X) of the point locating the address specified
* **y_fromaddress** : Returns the ordinate (Y) of the point locating the address specified
* **get_lineangle** :  Find the angle of a segment (from a target layer) located under the point of the source layer.

Author
======
* SIGMOÉ - Etienne MORO
* e-mail: em@sigmoe.fr
* website: https://www.sigmoe.fr

License
=======
GNU Public License (GPL) Version 3
