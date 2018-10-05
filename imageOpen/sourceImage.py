import cognitive_face as CF
import os
from os import *
from os.path import isfile, join, isdir
import json
from LargePersonGroup import *




def detect_sorce_face(directory):
    img1 = directory
    time.sleep(0.5)
    print("Opening target's file")
    time.sleep(0.5)
    os.startfile(img1)
    time.sleep(0.5)
    print("detecting targets face")
    img1Result = CF.face.detect(img1)
    print (img1Result)
    faceId1 = img1Result[0]['faceId']
    print(" ")
    return faceId1