# Convertisseur d'Images en Format WebP

Ce script Python permet de convertir des images présentes dans un dossier spécifié en format WebP, un format d'image plus léger et plus rapide à charger sur le web.

## Prérequis

- Python 3.x
- Pillow (PIL), une bibliothèque Python pour le traitement d'images. Vous pouvez l'installer en exécutant :
pip install pillow

## Utilisation

1. Clonez ce dépôt ou téléchargez simplement le script `convert_images.py`.
2. Exécutez le script en spécifiant le chemin du dossier contenant les images à convertir :
Par défaut, le script convertira les images présentes dans le dossier spécifié et sauvegardera les images converties dans le même dossier.

Vous pouvez également spécifier un chemin de sortie différent en modifiant la variable `output_folder` dans le script.

## Paramètres

- `input_folder`: Chemin du dossier contenant les images à convertir.
- `output_folder`: Chemin du dossier où seront enregistrées les images converties. Par défaut, les images sont enregistrées dans le même dossier que celui des images d'entrée.
- `quality`: Qualité de l'image WebP (entre 0 et 100), par défaut à 80.

## Remarques

- Assurez-vous que les images à convertir sont au format compatible (.jpg, .jpeg, .png, .bmp, .gif).
- Les images originales seront supprimées après la conversion réussie.

---

Ce script peut être utile pour optimiser les images d'un site web, réduisant ainsi leur taille et améliorant les performances de chargement des pages. Si vous avez des questions ou des suggestions, n'hésitez pas à ouvrir une issue ou à contribuer au projet en proposant des améliorations.
