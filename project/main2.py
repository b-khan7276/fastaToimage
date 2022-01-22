#Turning A CSV Back Into An Image (Python)
import cv2
import csv
import numpy as np
def pic_data_strip_csv():
   img = cv2.imread(r"image.png")
   img_height, img_width = img.shape[:2]
   for x in range (0, img_height,1):
      for y in range (0,img_width,1):
         pixel_value = img[x,y,:]
         with open(r"demo.csv",mode="a") as pic_data:
            pic_data_writer = csv.writer(pic_data, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write_pic_data = pic_data_writer.writerow([x,y,pixel_value])
   return()
def pic_data_strip_dict_csv():
   img = cv2.imread(r"image.png")
   img_height, img_width = img.shape[:2]
   for x in range (0, img_height,1):
      for y in range (0,img_width,1):
         pixel_value = img[x,y,:]
         with open(r"demo.csv",mode="a",newline="") as pic_data:
            field_names = ["x","y","bgr"]
            pic_data_writer = csv.DictWriter(pic_data, fieldnames=field_names)
            pic_data_writer.writeheader()
   return()
def create_pic_from_csv():
   image = np.zeros((423,253,3), np.uint8)
   with open(r"demo.csv", newline="") as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
         x = row['a']
         x = int(x)
         y = row['b']
         y = int(y)
         bgr = row['bgr']
         #gets the BGR value out of the []
         bgr_edit = str(bgr)
         print(bgr_edit)
         head,sep,tail = bgr_edit.partition('')
         b = head.strip("[")
         bgr_tail = tail.strip()
         bgr_tail = bgr_tail.replace("]","")
         head,sep,tail = bgr_tail.partition(" ")
         g = head
         r = tail
         b = int(b)
         g = int(g)
         r = int(r)
         image[x,y]=[b,g,r]
      cv2.imshow("image",image)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
   return()
"""  

import cv2

import csv

import numpy as np

def pic_data_strip_csv():

    img = cv2.imread(r"image.png")

    img_height, img_width = img.shape[:2]

    for x in range (0, img_height,1):

    for y in range (0,img_width,1):

    pixel_value = img[x,y,:]

    with open(r"demo.csv",mode="a") as pic_data:

    pic_data_writer = csv.writer(pic_data, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    write_pic_data = pic_data_writer.writerow([x,y,pixel_value])

 return()

def pic_data_strip_dict_csv():

    img = cv2.imread(r"image.png")

    img_height, img_width = img.shape[:2]

    with open(r"demo.csv",mode="a",newline="") as pic_data:

    field_names = ["x","y","bgr"]

    pic_data_writer = csv.DictWriter(pic_data, fieldnames=field_names)

    pic_data_writer.writeheader()

        for x in range (0, img_height,1):

        for y in range (0,img_width,1):

        pixel_value = img[x,y,:]

        write_pic_data = pic_data_writer.writerow({"x":x,"y":y,"bgr":pixel_value})

    return()

'''Sudheer'''

def create_pic_from_csv():

    image = np.zeros((512,512,3), np.uint8)

    with open(r"demo.csv", newline="") as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        x = row["x"]

        x = int(x)

        y = row["y"]

        y = int(y)

        bgr = row["bgr"]

        #gets the BGR value out of the []

        bgr_edit = str(bgr)

        print(bgr_edit)

        head,sep,tail = bgr_edit.partition(" ")

        b = head.strip("[")

        bgr_tail = tail.strip()

        bgr_tail = bgr_tail.replace("]","")

        head,sep,tail = bgr_tail.partition(" ")

        g = head

        r = tail

        b = int(b)

        g = int(g)

        r = int(r)

        image[x,y]=[b,g,r]

        cv2.imshow("xkcd 1696",image)

        cv2.waitKey(0)

        cv2.destroyAllWindows()

    return()

pic_data_strip_csv()

pic_data_strip_dict_csv()

create_pic_from_csv() """