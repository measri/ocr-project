import cv2
import easyocr 
import json
import matplotlib.pyplot as plt  

# Fonction pour traiter une image et extraire les informations de texte
def process_image(img_path, output_json):
    # Lecture de l'image
    img = cv2.imread(img_path)
    # Initialisation du lecteur EasyOCR pour l'anglais
    reader = easyocr.Reader(['en'], gpu=False)
    # Reconnaissance de texte dans l'image
    text_results = reader.readtext(img)
    # Seuil de confiance pour filtrer les résultats de texte
    seuil = 0.1
    output = []

    # Parcours des résultats de texte détectés
    for bbox, text, score in text_results:
        if score > seuil:
            bbox = [list(map(int, point)) for point in bbox]
            result = {"text": text, "bbox": bbox, "score": float(score)}
            output.append(result)

    # Conversion des résultats en format JSON et sauvegarde dans un fichier
    json_output = json.dumps(output, indent=4)
    with open(output_json, 'w') as f:
        f.write(json_output)

    # Dessin des rectangles et des textes sur l'image
    for result in output:
        bbox = result['bbox']
        text = result['text']
        cv2.rectangle(img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 2)
        cv2.putText(img, text, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    # Affichage de l'image
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

# Fonction principale pour le traitement de l'image contenant la carte
def main_Genova(img_path):
    process_image(img_path, 'Carte_info_extracted.json')
    print("Les informations de la carte ont été sauvegardées dans le fichier Carte_info_extracted.json.")

# Fonction principale pour le traitement de l'image contenant le tableau
def main_table(img_path):
    process_image(img_path, 'Table_info_extracted.json')
    print("Les informations du tableau ont été sauvegardées dans le fichier Table_info_extracted.json.")
    
if __name__ == "__main__":
    img_path_iqoa = 'Extrait_IQOA_data.png'
    main_table(img_path_iqoa)
    
    img_path = 'Genova.png'
    main_Genova(img_path)
