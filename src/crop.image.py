from PIL import Image
import sys

'''

Use https://www.image-map.net/ to get the coordinates of the selected area in an image

'''

if len(sys.argv) < 6:
    print("error: image file missing")
    exit(1)

file_name = sys.argv[1]
top_left_x = int(sys.argv[2])
top_left_y = int(sys.argv[3])
bottom_right_x = int(sys.argv[4])
bottom_right_y = int(sys.argv[5])

print("cropping image -> ", file_name )
img_old = Image.open(file_name)
img_new = img_old.crop((top_left_x, top_left_y, bottom_right_x, bottom_right_y))
img_new.save(file_name)

