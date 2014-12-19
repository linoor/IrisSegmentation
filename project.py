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
    # finding general area of the pupil
    binarised_img = binarise(im)

    # removing noise
    nl = CrossSE()
    eroded_img = copy_image(binarised_img)
    erode(binarised_img, eroded_img, nl(1))
    eroded_img.show()

    # finding pupil edges
    gradient_img = copy_image(im)
    gradient(im, gradient_img)
    gradient_img.show()

    return eroded_img

def extract_reflections(im):
    imOut = copy_image(im)
    nl = CrossSE()
    erode(im, imOut, nl(2))
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

    extracted = extract_reflections(original_image)
    extracted.show()

    pupil = find_pupil(extracted)

    # map(lambda img: extract_reflections(img).show(), get_all_images())

if __name__ == "__main__":
    main()
