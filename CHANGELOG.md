# CHANGELOG

### 3.0.5 - 29/08/2024
*Ajout de 2 nouvelles fonctions :
- **geomtouches_startpoint** : retourne la valeur d'un champ de l'objet de la couche cible (ponctuelle) qui touche le premier point de l'objet source (linéaire).
- **geomtouches_endpoint** : retourne la valeur d'un champ de l'objet de la couche cible (ponctuelle) qui touche le dernier point de l'objet source (linéaire).

### 3.0.4 - 23/02/2022

* Modification de la fonction **get_address** pour tenir compte de tous les systèmes de coordonnées légaux français, y compris ceux des DROM.
**ATTENTION** : désormais le second argument **distance_limite** est obligatoire.

### 3.0.3 - 26/08/2021

* Ajout de 2 codes supplémentaires dans le paramètre **format**:
- **id** : retourne l'identifiant de l’adresse (clef d’interopérabilité)
- **riv** : retourne le code RIVOLI de l'adresse

### 3.0.2 - 30/11/2020

* Ajout d'un paramètre **distance** sur la fonction **get_address**. Ce paramètre permet d'indiquer une distance limite pour retenir ou pas l'adresse (adresse non retenue si le point adresse retrouvé est trop éloigné du point du canevas)
* Correction de 2 bogues sur la fonction **get_address**

### 3.0.1 - 03/11/2020

* Première version