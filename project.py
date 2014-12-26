import os
import smilPython as smil

images_folder = r"E:\Dropbox\Francja\Erasmus 2014\Mines ParisTech\Analyse d'images\examen_ES14\UBIRIS"

def get_all_images():
    return [Image(os.path.join(images_folder, img_path)) for img_path in os.listdir(images_folder)]

def copy_image(im):
    imOut = Image(im)
    smil.copy(im, imOut)
    return imOut

def diff(im, im2):
    imOut = copy_image(im)
    compare(im, "!=", im2, 255, 0, imOut)
    return imOut

def binarise(im):
    imOut = copy_image(im)
    imIn = copy_image(im)
    min_val = 0
    max_val = 80
    trueval = 0
    falseval = 255
    threshold(imIn, min_val, max_val, trueval, falseval, imOut)
    return imOut

def main():
    # choosing an image
    image_name = "I13.png"
    original_image = Image(os.path.join(images_folder, image_name))
    original_image.show()

    # initialising images
    no_reflections = Image(original_image)

    # removing reflections
    median(original_image, no_reflections, CrossSE(2))
    smil.open(no_reflections, no_reflections, CrossSE(2))
    no_reflections.show()

    # thresholding image to get the pupil (sometimes we get also the eyelashes)
    binarised_img = binarise(original_image)
    binarised_img.show()
    write(binarised_img, "binarised.png")

    # removing eyelashes, closing the pupil
    

    # # remove reflection from the original image
    # no_reflection = copy_image(original_image)
    # compare(closed_pupil, "<=", original_image, closed_pupil, original_image, no_reflection)
    # no_reflection.show()
    # write(no_reflection, "no_reflection.png")

if __name__ == "__main__":
    main()
