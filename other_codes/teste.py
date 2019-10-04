import cropper
import os
import sys
all_paths = []
current_path = cropper.get_current_path(sys.argv[0], __file__)
img_dir = current_path + "/images"
for i in range(1,6):
    all_paths.append("C:/Users/migue/Desktop/MyFaceDetect/images" + '/image_' + str(i) + '.jpg')

print(all_paths)
all_paths = cropper.rotate_images(all_paths)
margins = {
    "top": 200,
    "bottom": 25,
    "right": 100,
    "left": 100,
}
cropped_paths = cropper.rectangle_crop(all_paths, margins)
dest_path = current_path
cropper.create_gif(cropped_paths, dest_path)
