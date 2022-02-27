from PIL import Image

def join_horizontal(images):
    if(len(images) == 1):
        return images[0]
    image_sizes = []

    for image in images:
        image_sizes.append(image.size)
    new_image = Image.new('RGB', (len(images)*image_sizes[0][0], image_sizes[0][1]), (250, 250, 250))    
    new_image.paste(images[0], (0, 0)) # add first image from images to new image

    for i in range(len(images)):
        new_image.paste(images[i], (image_sizes[0][0]*i, 0))
    return new_image