```
import zipfile

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# the rest is up to you!
images = {} # dictionary of lists indexed with filenames
# [0] : PIL Image File
# [1] : Text in image

name_list = [] # list of filenames

def unzip_images(zip_name):
    '''
    iterates over images in a zipfile and extracts and modifies global dictionary for all
    also creates a namelist containing all names of all images in the zipfile
    '''
    zf = zipfile.ZipFile(zip_name)
    for each in zf.infolist():
        images[each.filename] = [Image.open(zf.open(each.filename))]
        name_list.append(each.filename)
#         print(each.filename)
        
if __name__ == '__main__':
#     working with a global data structure using HINTS 1 and 2
    
#     unzip_images('readonly/small_img.zip')
    unzip_images('readonly/images.zip')
    
    for name in name_list:
#         display(images[name][0])
#         print(name)
        img = images[name][0]
        
        images[name].append(pytesseract.image_to_string(img).replace('-\n',''))
#         using string data to omit line separators "-\n" in the data
#         modifying global data structure to append text present in each image

#         print(images[name][1])
        
        if 'Mark' in images[name][1]: 
#             using HINT 3
            print('Results found in file',name)
            
            try:
                faces = (face_cascade.detectMultiScale(np.array(img),1.35,4)).tolist()
#                 storing the bounding boxes of all faces detected in each image of iteration

                images[name].append(faces)
#                 modifying global data structure to append faces present in each image

                faces_in_each = []
                
                for x,y,w,h in images[name][2]:
                    faces_in_each.append(img.crop((x,y,x+w,y+h)))
#                     modifying local data structure in each iteration to sotre PIL Image of each face
#                     display((img.crop((x,y,x+w,y+h))).resize((110,110)))
                
                contact_sheet = Image.new(img.mode, (550,110*int(np.ceil(len(faces_in_each)/5))))
#                 contact sheet modification to display each iteration's result
                x = 0
                y = 0

                for face in faces_in_each:
                    face.thumbnail((110,110))
#                     using HINT 4
                    contact_sheet.paste(face, (x, y))
                    
                    if x+110 == contact_sheet.width:
                        x=0
                        y=y+110
                    else:
                        x=x+110
                        
                display(contact_sheet)
            except:
                print('But there were no faces in that file!')
      
```
