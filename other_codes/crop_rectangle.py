import cv2
import os
import sys

MARGIN_TOP = 50
MARGIN_LEFT = 10
MARGIN_RIGHT = 10
MARGIN_BOTTOM = 10

# Get user supplied values
current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
imagePath = current_path + "/random_face_front.png"
cascPath = current_path + "/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.imread(imagePath,0)
if image.any() == None:
    message = "Couldn't load image from path: " + imagePath
    raise Exception(message)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
)

print("Found {0} faces!".format(len(faces)))

# Crop the face
for (x, y, w, h) in faces:
    startY = y - MARGIN_TOP
    startX = x - MARGIN_LEFT
    endY = y + h + MARGIN_BOTTOM
    endX = x + w + MARGIN_RIGHT

    crop_img = image[startY:endY, startX:endX].copy()
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)
    file_path = current_path + "/crop.png"
    cv2.imwrite(file_path, crop_img)
