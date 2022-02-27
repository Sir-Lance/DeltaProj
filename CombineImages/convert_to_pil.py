from PIL import Image

def convert_to_pil(images):
    pil_images = []
    for image in images:
        pil_images.append(Image.open('./img/' + image))
    return pil_images