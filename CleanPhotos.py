import cv2
import os

BASE_PATH = "PATH_BEFORE_FOLDER"
FOLDER_NAME = "FOLDERNAME"
cascPath = "PATH_TO_CLASSIFIER/haarcascade_frontalface_default.xml"
EXT = [".JPG"] #List of extensions 

faceCascade = cv2.CascadeClassifier(cascPath)

def face_detected(IMG_PATH):
    image = cv2.imread(IMG_PATH)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    
    if len(faces) > 0:
        print("FACE FOUND")
        return True
        
    else:
        print("NO FACE FOUND {}".format(IMG_PATH))
        return False
        
 
for folder in os.listdir(BASE_PATH):
    for IMG_NAME in os.listdir(BASE_PATH+folder):
        
        IMG_PATH = BASE_PATH+folder+"/"+IMG_NAME #create img_path
        if not "."+IMG_NAME.split(".")[-1] in EXT:
            os.remove(IMG_PATH) #delete if invalid name
        if not face_detected(IMG_PATH):
            os.remove(IMG_PATH) #remove if no face
        