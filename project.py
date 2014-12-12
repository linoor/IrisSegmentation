import os
import smilPython as smil

images_folder = r"E:\Dropbox\Francja\Erasmus 2014\Mines ParisTech\Analyse d'images\examen_ES14\UBIRIS"

def extract_reflections()

def main():
	# choosing an image
	image_name = "I13.png"
	original_image = Image(os.path.join(images_folder, image_name))
	#original_image.show()

	# reflection extraction
	img_no_reflections = Image(original_image)
	open(original_image, img_no_reflections, VertSE(3))
	img_no_reflections.show()

	# # getting gradient
	# img_gradient = Image(original_image)
	# gradient(img_without_lights, img_gradient)
	# #img_gradient.show()

	# # h maxima
	# img_maxima = Image(original_image)
	# hMaxima(img_gradient, 20, img_maxima)
	# img_maxima.show()

	# # watershed
	# img_watershed = Image(original_image)
	# watershed(img_gradient, img_watershed)
	# img_watershed.show()

if __name__ == "__main__":
	main()
