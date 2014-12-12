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
	open(im, imOut, VertSE(3))
	return imOut

def main():
	# choosing an image
	image_name = "I13.png"
	original_image = Image(os.path.join(images_folder, image_name))
	#original_image.show()

	# reflection extraction
	extract_reflections(original_image).show()

	map(lambda img: extract_reflections(img).show(), get_all_images())

if __name__ == "__main__":
	main()
