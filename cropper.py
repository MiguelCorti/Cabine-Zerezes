import cv2
import os
import sys
import datetime
from PIL import Image

# Returns path where this script is running
def get_current_path(argv, file):
    current_path = '.'
    if __file__ == None:
        current_path = os.path.dirname(os.path.realpath(argv))
    else:
        current_path = os.path.dirname(os.path.realpath(file))
    return current_path

def create_gif(cropped_paths, image_path):
    images = []
    num_of_imgs = len(cropped_paths)
    for i in range(0, num_of_imgs):
        images.insert(i, Image.open(cropped_paths[i]))
        if i != 0:
            reverse_index = -(i+1)
            images.append(Image.open(cropped_paths[reverse_index]))

    # Save into a GIF file that loops forever
    gif_name = image_path + '/final_image.gif'
    images[0].save(gif_name, format='GIF', append_images=images[1:], save_all=True, duration=200, loop=0)

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
def bottom_crop(all_paths, margin_bottom = 10):
    # Get user supplied values
    current_path = get_current_path(sys.argv[0], __file__)
    cascPath = current_path + "/haarcascade_frontalface_default.xml"

    middle_index = int(len(all_paths)/2)
    # Detect faces in the image
    faces = detect_faces(all_paths[middle_index], cascPath)

    print("Found {0} faces!".format(len(faces)))

    # Croping all 5 images based on the frontal detection
    (x, y, w, h) = faces[0]
    endY = y + h + margin_bottom
    cropped_paths = []
    for i in range(0,len(all_paths)):
        image = cv2.imread(all_paths[i])

        crop_img = image[0:endY].copy()
        img_dir = current_path + "/images"
        if not os.path.exists(img_dir):
            os.mkdir(img_dir)

        file_path = img_dir + "/cropped_image_" + str(i+1) + ".jpg"
        cv2.imwrite(file_path, crop_img)
        cropped_paths += [file_path]

    return cropped_paths

# Detects faces and crops a rectangle
def rectangle_crop(all_paths, margins):
    # Get user supplied values
    current_path = get_current_path(sys.argv[0], __file__)
    cascPath = current_path + "/haarcascade_frontalface_default.xml"

    middle_index = int(len(all_paths)/2)
    # Detect faces in the image
    faces = detect_faces(all_paths[middle_index], cascPath)

    num_faces = len(faces)
    print("Found {0} faces!".format(num_faces))
    if num_faces == 0:
        print("Can't crop without a face reference.")
        return all_paths

    # Crop the face
    (x, y, w, h) = faces[0]
    startY = y - margins["top"]
    startX = x - margins["left"]
    endY = y + h + margins["bottom"]
    endX = x + w + margins["right"]
    cropped_paths = []
    for i in range(0,len(all_paths)):
        image = cv2.imread(all_paths[i])

        crop_img = image[startY:endY, startX:endX].copy()
        img_dir = current_path + "/images"
        if not os.path.exists(img_dir):
            os.mkdir(img_dir)

        file_path = img_dir + "/cropped_image_" + str(i+1) + ".jpg"
        cv2.imwrite(file_path, crop_img)
        cropped_paths += [file_path]

    return cropped_paths
