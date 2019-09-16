import cv2
import os
import sys

# Returns path where this script is running
def get_current_path():
    current_path = '.'
    if __file__ == None:
        current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    else:
        current_path = os.path.dirname(os.path.realpath(__file__))
    return current_path

def create_gif(images):
    # Save into a GIF file that loops forever
    images[0].save('pictures.gif', format='GIF', append_images=images[1:], save_all=True, duration=100, loop=0)

# Detects all faces from received image using received cascade
def detect_faces(image_path, cascade_path):
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascade_path)

    # Read the image in gray
    gray = cv2.imread(image_path, 0)
    if gray is None:
        message = "Couldn't load image from path: " + image_path
        raise Exception(message)

    # Detect faces in the gray image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    return faces

# Detects faces and crops them only chin down
def bottom_crop(margin_bottom = 10, image_name = "image", image_extension = "jpg"):
    image_extension = "." + image_extension
    cropped_image_name = image_name + "_cropped"

    # Defining path variables
    current_path = get_current_path()
    frontalImagePath = current_path + "/" + image_name + '_3' + image_extension
    cascPath = current_path + "/haarcascade_frontalface_default.xml"

    # Getting all faces within image
    faces = detect_faces(frontalImagePath, cascPath)

    # Croping all 5 images based on the frontal detection
    (x, y, w, h) = faces[0]
    endY = y + h + margin_bottom
    for i in range(1,6):
        currentImagePath = current_path + "/" + image_name + '_' + str(i) + image_extension
        image = cv2.imread(currentImagePath)

        crop_img = image[0:endY].copy()
        file_path = current_path + "/" + cropped_image_name + '_' + str(i) + image_extension
        cv2.imwrite(file_path, crop_img)

# Detects faces and crops a rectangle
def rectangle_crop(image_name = "image", image_extension = "jpg", margin_top = 50, margin_left = 20, margin_right = 20, margin_bottom = 15):
    # Get user supplied values
    current_path = get_current_path()
    image_extension = "." + image_extension
    cropped_image_name = image_name + "_cropped"
    frontalImagePath = current_path + "/" + image_name + '_3' + image_extension
    cascPath = current_path + "/haarcascade_frontalface_default.xml"

    # Detect faces in the image
    faces = detect_faces(frontalImagePath, cascPath)

    print("Found {0} faces!".format(len(faces)))

    # Crop the face
    (x, y, w, h) = faces[0]
    startY = y - margin_top
    startX = x - margin_left
    endY = y + h + margin_bottom
    endX = x + w + margin_right
    for i in range(1,6):
        currentImagePath = current_path + "/" + image_name + '_' + str(i) + image_extension
        image = cv2.imread(currentImagePath)

        crop_img = image[startY:endY, startX:endX].copy()
        file_path = current_path + "/" + cropped_image_name + '_' + str(i) + image_extension
        cv2.imwrite(file_path, crop_img)
