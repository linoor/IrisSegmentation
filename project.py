import os
import smilPython as smil

images_folder = r"E:\Dropbox\Francja\Erasmus 2014\Mines ParisTech\Analyse d'images\examen_ES14\UBIRIS"

def get_all_images():
    return [Image(os.path.join(images_folder, img_path)) for img_path in os.listdir(images_folder)]

def copy_image(im):
    imOut = Image(im)
    smil.copy(im, imOut)
    return imOut

def binarise(im):
    imOut = copy_image(im)
    threshold(im, 0, 60, 0, 255, imOut)
    return imOut

def find_pupil(im):
    binarised_img = binarise(im)

    # filtering the image with erosion
    nl = CrossSE()
    eroded_img = copy_image(binarised_img)
    erode(binarised_img, eroded_img, nl(1))

    return eroded_img

def extract_reflections(im):
    imOut = copy_image(im)
    imMark = Image(im)
    nl = HexSE()
    ASF_Leveling(im, 5, imOut, nl(2))
    return imOut

def diff(im, im2):
    imOut = copy_image(im)
    compare(im, "!=", im2, 255, 0, imOut)
    return imOut

def main():
    # choosing an image
    image_name = "I13.png"
    original_image = Image(os.path.join(images_folder, image_name))
    original_image.show()

    pupil = find_pupil(original_image)
    pupil.show()

    # map(lambda img: extract_reflections(img).show(), get_all_images())

if __name__ == "__main__":
    main()
