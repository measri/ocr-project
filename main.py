import cv2
import easyocr
import json
import matplotlib.pyplot as plt

def main(img_path):
    # Lire l'image
    img = cv2.imread(img_path)

    # Initialiser l'outil OCR
    reader = easyocr.Reader(['en'], gpu=False)

    # Lire le texte de l'image
    text_results = reader.readtext(img)

    # Seuil de confiance
    seuil = 0.1

    # Stocker les résultats
    output = []

    for bbox, text, score in text_results:
        if score > seuil:
            # Convertir les valeurs de bbox en listes pour les rendre sérialisables
            bbox = [list(map(int, point)) for point in bbox]
            result = {
                "text": text,
                "bbox": bbox,
                "score": float(score)  # Convertir le score en nombre flottant
            }
            output.append(result)

    # Convertir la liste de dictionnaires en une chaîne JSON
    json_output = json.dumps(output, indent=4)
    print(json_output)

    # Enregistrer le JSON dans un fichier
    with open('output.json', 'w') as f:
        f.write(json_output)

    # Dessiner les rectangles et le texte sur l'image
    for result in output:
        bbox = result['bbox']
        text = result['text']
        score = result['score']
        cv2.rectangle(img, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 2)
        cv2.putText(img, text, tuple(bbox[0]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    # Afficher l'image avec les annotations
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

if __name__ == "__main__":
    img_path = 'Genova.png'
    main(img_path)

