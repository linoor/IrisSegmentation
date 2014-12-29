import os
import smilPython as smil
import math

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
    max_val = 50
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

def draw_circle(im, x0, y0, r):
    for d in range(360):
        t = math.radians(d)
        x = int(r*math.cos(t))
        y = int(r*math.sin(t))
        im.setPixel(x0+x, y0+y, 255)

def main():
    # choosing an image
    image_name = "I15.png"
    original_image = Image(os.path.join(images_folder, image_name))
    original_image.show()

    # initialising images
    no_reflections = copy_image(original_image)
    closed_pupil = Image(original_image)

    # normalizing the image
    im = normalize(original_image)
    # im.show()

    # removing reflections over the area of the pupil
    no_reflections.getPixel(76, 50)
    for i in range(30, 100):
        for j in range(25, 90):
            if no_reflections.getPixel(i, j) > 240:
                no_reflections.setPixel(i, j, 0)
    compare(no_reflections, "==", 0, no_reflections, im, no_reflections)
    smil.open(no_reflections, no_reflections, HexSE(2))
    # no_reflections.show()

    # thresholding image to get the pupil (sometimes we get also the eyelashes)
    binarised_img = binarise(original_image)
    # binarised_img.show()
    write(binarised_img, "binarised.png")

    # removing eyelashes, closing the pupil
    smil.close(binarised_img, closed_pupil, VertSE(2))
    smil.open(closed_pupil, closed_pupil, HexSE(9))
    # closed_pupil.show()

    # # reconstruction
    # inv_closed_pupil = Image()
    # inv(closed_pupil, inv_closed_pupil)
    # inv_closed_pupil.show()
    # recon = Image()
    # build(inv_closed_pupil, original_image, recon)
    # recon.show()

    # calculating the the pupil's center of mass from the binary image
    pixels = []
    x_sum = 0
    y_sum = 0
    num_black_pixels = 0
    image = closed_pupil
    for i in range(image.getWidth()):
        for j in range(image.getHeight()):
            pixel = image.getPixel(i, j)
            if pixel == 0:
                num_black_pixels += 1
                x_sum += i
                y_sum += j

    pupil_x = int((1.0/num_black_pixels) * x_sum)
    pupil_y = int((1.0/num_black_pixels) * y_sum)
    pupil_r = int(math.sqrt(num_black_pixels / math.pi))

    # showing where the pupil is
    pupil_showed = Image(original_image)
    pupil_showed << 0
    draw_circle(pupil_showed, pupil_x, pupil_y, pupil_r)
    # pupil_showed.show()
    overlay(pupil_showed, original_image)

    # gradient
    grad = copy_image(no_reflections)
    close(grad, grad, SquSE(10))
    threshold(grad, grad)
    gradient(grad, grad)
    grad.show()

if __name__ == "__main__":
    main()
