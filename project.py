import os
import smilPython as smil

images_folder = r"E:\Dropbox\Francja\Erasmus 2014\Mines ParisTech\Analyse d'images\examen_ES14\UBIRIS"

def get_all_images():
	return [Image(os.path.join(images_folder, img_path)) for img_path in os.listdir(images_folder)]

def copy_image(im):
	imOut = Image(im)
	smil.copy(im, imOut)
	return imOut

def extract_reflections(im):
	imOut = copy_image(im)
	open(im, imOut, CrossSE(7))
	return imOut

def diff(im, im2):
	imOut = copy_image(im)
	compare(im, "!=", im2, 255, 0, imOut)
	return imOut

def main():
	# choosing an image
	image_name = "I13.png"
	original_image = Image(os.path.join(images_folder, image_name))
	#original_image.show()

	# reflection extraction
	no_reflections = extract_reflections(original_image)
	no_reflections.show()

	map(lambda img: extract_reflections(img).show(), get_all_images())

if __name__ == "__main__":
	main()
