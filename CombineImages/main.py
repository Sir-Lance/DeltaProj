from os import listdir
from os.path import isfile, join
from PIL import Image
from split_images import split_images
from convert_to_pil import convert_to_pil
from join_horizontal import join_horizontal
from join_vertical import join_vertical
from resize_images import resize_images

    
    

def main():
    # #temp hardcoded images
    # image_1 = './img/PI-R-556-47241.jpg'
    # image_2 = './img/RD-10379.jpg'
    # image_3 = './img/TR-18495.jpg'
    # image_4 = './img/meirl.png'
    # image_5 = './img/gamer.png'
    # image_6 = './img/loveit.png'
    # images = [image_1, image_2, image_3, image_4, image_5, image_6]

    # get all images in img folder
    images = [f for f in listdir('./img') if isfile(join('./img/', f))]

    #split images into 2 groups for top and bottom of thumbnail
    images_1, images_2 = split_images(images)

    # convert images from paths to pillow image objects
    images_1 = convert_to_pil(images_1)
    images_2 = convert_to_pil(images_2)

    # resize images to fit in 1200x600 thumbnail
    images_1 = resize_images(images_1)
    images_2 = resize_images(images_2)
    
    # join images horizontally 
    top = join_horizontal(images_1) # get top half of output image
    bot = join_horizontal(images_2) # get bottom half of output image
    
    # # check that images joined correctly
    # top.show()
    # bot.show()

    # join top and bottom image
    output = join_vertical(top, bot)

    #check output generated properly
    output.show()
    
    # save output
    output.save('./output-img/output.jpg')



if __name__ == '__main__':
    main()