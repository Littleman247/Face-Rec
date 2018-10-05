import cognitive_face as CF
import os
from os import *
from os.path import isfile, join, isdir
import json
from LargePersonGroup import *
from sourceImage import *
import time

#dict
imageFiles = []
people = []
dirpathlist = []

#values
faceId1 = "blah"
largePersonGroupId = 'large_peron_group_id'
largePersonGroupName = 'large_perosn_group_name'

#defining the directory to access required documents
mypath = 'C:\\FaceRec\\facialRecognitionImages\\'
directory = 'C:\\FaceRec\\facialRecognitionImages\\source.jpg'

#defining key and URL to access mircrosoft's webiste to detect, identify, and verify faces for australia
KEY = '<insert_azure_facial_recognition_service_key_here>' 
CF.Key.set(KEY)
BASE_URL = 'https://australiaeast.api.cognitive.microsoft.com/face/v1.0/' 
CF.BaseUrl.set(BASE_URL)


#looks through the mypath directory and obtains all files 
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#get all the subdirectories for all the files under the mypath directory
onlydir = [d for d in listdir(mypath) if isdir(join(mypath, d))]

#gets all the names of the photos and alicates the person to their faces
for each in onlydir:
    dirpath = join(mypath, each)
    files = Get_Image_Files_From_Person(dirpath)
    people.append({"Person" : each, "faces" : files})
    imageFiles.extend(files)



clear()

print("")
print("-------------------------------------------------------------")
print("")
faceId1 = detect_sorce_face(directory)

print("")
print("-------------------------------------------------------------")
print("")
large_group_create(largePersonGroupId,largePersonGroupName)

print("")
print("-------------------------------------------------------------")
print("")
large_group_search(people,faceId1,largePersonGroupId)

print("")
print("-------------------------------------------------------------")
print("")

large_group_delete(largePersonGroupId)
time.sleep(3)
print("beginig shutting down sequence")
time.sleep(1)
print("deleting remaing open groups")
time.sleep(1)
print("groups deleted")
time.sleep(1)
print("goodbye")