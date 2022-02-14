from PIL import Image


# takes list of image paths
def split_images(images):
    # split images into 2 groups 
    images_cpy = images.copy()
    images_1 = images_cpy[0:len(images_cpy)//2]
    images_2 = images_cpy[len(images_cpy)//2::]
    return images_1, images_2
    # convert images to pillow image objects
 

# convert list of image paths to pillow image objects
def open_pillow_images(images):
    pil_images = []
    i = 0 #list index for used to display current img
    for img in images:
        pil_images.append(Image.open(img))
        # pil_images[i].show()
        i += 1
    return pil_images


def resize_images(images):
    width = 600 # half the width of full thumbnail
    height = 600 # height of full thumbnail
    num_imgs = len(images)

    # get resized image dimensions based on number of images
    height = height//num_imgs

    resized_images = []
    i = 0 # index of img
    for img in images:
        resized_img = img.resize((width, height))
        resized_images.append(resized_img)
    return resized_images


def combine_images(images):
    num_images = len(images)
    if(num_images == 1):
        return images[0]
    
    images_1 = images[0:num_images//2]
    image_sizes_1 = []
    for img in images_1:
        image_sizes_1.append(img.size)

    images_2 = images[num_images//2::]
    image_sizes_2 = []
    for img in images_2:
        image_sizes_2.append(img.size)

    new_image = Image.new('RGB', (len(images_1)*image_sizes_1[0][0], image_sizes_1[0][1]), (250, 250, 250))
    new_image.paste(images_1[0], (0, 0))
    images_1.pop(0)
    
    for i in range(len(images_1)): 
        new_image.paste(images[i], (image_sizes_1[0][0]*i, 0))

    new_image_2 = Image.new('RGB', (len(images_2)*image_sizes_2[0][0], image_sizes_2[0][1]), (250, 250, 250))
    new_image_2.paste(images_2[0], (0, 0))
    images_2.pop(0)
    for i in range(len(images_2)):
        new_image.paste(images[i], (image_sizes_2[0][0]*i, 0))

    new_img_1_size = new_image.size
    output_img = Image.new('RGB', (new_img_1_size[0], 2*new_img_1_size[1]), 0)
    output_img.paste(new_image, (0,0))
    output_img.paste(new_image_2, (0, new_img_1_size[1]))
    return output_img



if __name__ == '__main__':
    # temporarily hard-coded images
    image_1 = './img/PI-R-556-47241.jpg'
    image_2 = './img/RD-10379.jpg'
    image_3 = './img/TR-18495.jpg'
    images = [image_1, image_2, image_3]

    # split images into 2 groups
    images_1, images_2 = split_images(images)
    print(f'images_1: {images_1},\nimages_2: {images_2}')
    
    # convert to pillow image objects
    pil_images_1 = open_pillow_images(images_1)
    pil_images_2 = open_pillow_images(images_2)

    # resize images
    pil_images_1 = resize_images(pil_images_1)
    pil_images_2 = resize_images(pil_images_2)

    # combine images
    left_img = combine_images(pil_images_1)
    right_img = combine_images(pil_images_2)
    
    # show left and right half of final image
    left_img.show()
    right_img.show()

    # combine left and right image horizontally
    left_img_size = left_img.size
    final_image = Image.new('RGB', (2*left_img_size[0], left_img_size[1]), (250, 250, 250))
    final_image.paste(left_img, (0, 0))
    final_image.paste(right_img, (left_img_size[0], 0))
    final_image.show()
    final_image.save('./new-img/final-image.jpg')