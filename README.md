# Reconnaissance Optique de Caractères (OCR) - Projet

Ce projet utilise EasyOCR pour détecter et extraire le texte à partir d'images. Il se concentre sur l'extraction du texte à partir d'une image de carte (Genova.png) et d'une image de tableau (Extrait_IQOA_data.png). Le résultat est fourni au format JSON, incluant le texte, les coordonnées des boîtes englobantes et le score de confiance.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé Python sur votre système. Vous pouvez le télécharger depuis [le site officiel de Python](https://www.python.org/downloads/).

## Installation

1. Clonez le repository en utilisant la commande suivante dans votre terminal :
```bash
git clone https://github.com/measri/ocr-project.git
```

2. Accédez au répertoire du projet :
```bash
cd ocr-project
```

3. Installez les dépendances en exécutant la commande suivante :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Assurez-vous que les images que vous souhaitez traiter (Genova.png et Extrait_IQOA_data.png) sont placées dans le répertoire du projet.

2. Exécutez le script principal en utilisant la commande suivante :
```bash
python main.py
```
3. Suivez les instructions affichées dans la console pour voir les résultats de la détection du texte.

## Structure des Fichiers

- **main.py**: Le script principal qui coordonne le processus de détection de texte.
- **requirements.txt**: Fichier contenant la liste des dépendances du projet.
- **Carte_info_extracted.json**: Fichier JSON contenant les informations extraites de la carte (Genova.png).
- **Table_info_extracted.json**: Fichier JSON contenant les informations extraites du tableau (Extrait_IQOA_data.png).
- **Genova.png**: Image de carte à traiter.
- **Extrait_IQOA_data.png**: Image de tableau à traiter.

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, n'hésitez pas à ouvrir une issue pour discuter des modifications que vous proposez, ou soumettez directement une pull request.

En suivant ces instructions, vous serez en mesure d'utiliser et de contribuer à ce projet OCR. Si vous avez des questions ou des problèmes, n'hésitez pas à ouvrir une issue. Merci !

