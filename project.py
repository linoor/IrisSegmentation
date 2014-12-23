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
    threshold(im, 0, 40, 0, 255, imOut)
    return imOut

def extract_reflections(im):
    imOut = copy_image(im)
    nl = HexSE()
    erode(im, imOut, nl(2))
    return imOut

def diff(im, im2):
    imOut = copy_image(im)
    compare(im, "!=", im2, 255, 0, imOut)
    return imOut

def find_pupil(im):
    extracted = extract_reflections(im)

    # finding the pupil
    # finding general area of the pupil
    binarised_img = binarise(im)

    # removing noise
    nl = CrossSE()
    pupil_marker = copy_image(binarised_img)
    erode(binarised_img, pupil_marker, nl(1))
    pupil_marker.show()

    # finding pupil edges
    gradient_img = copy_image(extracted)
    gradient(extracted, gradient_img)

    # gradient_dilated = copy_image(gradient_img)
    # dilate(gradient_img, gradient_dilated)
    inv(gradient_img, gradient_img)

    # choosing the pupil by reconstruction
    pupil = Image(im)
    raze(pupil_marker, gradient_img, pupil)

    return pupil

def main():
    # choosing an image
    image_name = "I15.png"
    original_image = Image(os.path.join(images_folder, image_name))
    original_image.show()

    # extracting the reflections from the eye
    holes_filled = Image(original_image)
    # first we have to find the region of the pupil

if __name__ == "__main__":
    main()
