import os

from PIL import Image


def convert_images_in_folder(input_folder, output_folder):
    # Vérifiez si le dossier de sortie existe, sinon, créez-le
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Parcourez tous les fichiers dans le dossier d'entrée
    for filename in os.listdir(input_folder):
        input_image_path = os.path.join(input_folder, filename)

        # Vérifiez si le fichier est une image
        if input_image_path.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            try:
                image = Image.open(input_image_path)
                output_image_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".webp")
                image.save(output_image_path, "webp", quality=quality)
                print(f"L'image {filename} a été convertie en {output_image_path}")

                # Supprimez l'original
                os.remove(input_image_path)
                print(f"L'original {filename} a été supprimé")
            except Exception as e:
                print(f"Erreur lors de la conversion de {filename} : {str(e)}")


if __name__ == "__main__":
    input_folder = r"C:\xampp\htdocs\Portfolio\Images"  # Utilisation de r devant la chaîne
    # pour indiquer une chaîne brute
    output_folder = input_folder  # Remplacez par le chemin du dossier de sortie
    quality = 80  # Qualité de l'image WebP (entre 0 et 100)

    convert_images_in_folder(input_folder, output_folder)
