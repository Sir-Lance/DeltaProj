from PIL import Image

def split_images(images):
    images_copy = images.copy()
    images_1 = images_copy[0:len(images_copy)//2]
    images_2 = images_copy[len(images_copy)//2::]
    return images_1, images_2