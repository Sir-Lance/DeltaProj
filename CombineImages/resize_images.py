from PIL import Image

def resize_images(images):
    width = 1200 # full width of thumbnail
    height = 300 # half height of thumbnail

    num_images = len(images)
    width = width//num_images    # get resized width for number of images
    
    resized_images = []
    for image in images:
        resized_image = image.resize((width, height))
        resized_images.append(resized_image)
    return resized_images