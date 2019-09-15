import cv2
import os
import sys

margin_bottom = 10
image_name = "picture"
image_extension = "." + image_extension
cropped_image_name = image_name + "_cropped"

# Assign path variables
current_path = '.'
if __file__ == None:
    current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
else:
    current_path = os.path.dirname(os.path.realpath(__file__))

frontalImagePath = current_path + "/" + image_name + '3' + image_extension
cascPath = current_path + "/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image in gray
gray = cv2.imread(frontalImagePath, 0)
if gray is None:
    message = "Couldn't load image from path: " + frontalImagePath
    raise Exception(message)

# Detect faces in the gray image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Crop the all 5 images
(x, y, w, h) = faces[0]
endY = y + h + margin_bottom
for i in range(1,6):
    currentImagePath = current_path + "/" + image_name + str(i) + image_extension
    image = cv2.imread(currentImagePath)

    crop_img = image[0:endY].copy()
    file_path = current_path + "/" + cropped_image_name + str(i) + image_extension
    cv2.imwrite(file_path, crop_img)
