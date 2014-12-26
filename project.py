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

def normalize(im):
    """ linear normalization of a grayscale digital image """
    min_val = minVal(im)
    max_val = maxVal(im)
    imOut = copy_image(im)
    for i in range(im.getWidth()):
        for j in range(im.getHeight()):
            pixel = im.getPixel(i, j)
            imOut.setPixel(i, j, long((pixel - min_val) * (255 - 0) / (max_val - min_val) + 0))

    return imOut

def main():
    # choosing an image
    image_name = "I13.png"
    original_image = Image(os.path.join(images_folder, image_name))
    original_image.show()

    # initialising images
    no_reflections = Image(original_image)

    # normalize image
    im = normalize(original_image)
    im.show()

    # removing reflections
    

    # # thresholding image to get the pupil (sometimes we get also the eyelashes)
    # binarised_img = binarise(original_image)
    # binarised_img.show()
    # write(binarised_img, "binarised.png")

    # removing eyelashes, closing the pupil


    # # remove reflection from the original image
    # no_reflection = copy_image(original_image)
    # compare(closed_pupil, "<=", original_image, closed_pupil, original_image, no_reflection)
    # no_reflection.show()
    # write(no_reflection, "no_reflection.png")

if __name__ == "__main__":
    main()
