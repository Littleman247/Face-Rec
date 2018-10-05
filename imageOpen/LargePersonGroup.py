import cognitive_face as CF
import os
from os import *
from os.path import isfile, join, isdir
import time





def Get_Image_Files_From_Person(path):
    personFiles = []
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        personFiles.append(join(path, file))
    return personFiles



def clear():
    print("remaing open groups:")
    result = CF.large_person_group.list()
    print(result)
    time.sleep(1)
    print("termanating remianing groups")
    for group in result:
        CF.large_person_group.delete(group['largePersonGroupId'])
        print("groups terminated")
    return



def large_group_create(largePersonGroupId,largePersonGroupName):
    print("creating list")
    CF.large_person_group.create(largePersonGroupId, largePersonGroupName)
    return



def large_group_search(Persons,sourceFaceId,largePersonGroupId):
    for person in Persons:
        personName = person ["Person"]
        personFaces = person  ["faces"]
        personIdResult = CF.large_person_group_person.create(largePersonGroupId, personName, personName)
        personId = personIdResult['personId']
        person ["personId"] = personId
        print("added images" + str(person))
        for image in personFaces:
            persitFaceId = CF.large_person_group_person_face.add(image, largePersonGroupId, personId, image)
    
    print("")
    print("-------------------------------------------------------------")
    print("")

    print('beginign AI training...')
    time.sleep(1)
    print("to run on a hamster wheel!")
    CF.large_person_group.train(largePersonGroupId)


    while True:
        status = CF.large_person_group.get_status(largePersonGroupId)
        print (status)
        time.sleep(1)
        if status["status"] == "succeeded":
            print("Training Complete")
            break
        elif status["status"] == "running":
            print ("Still Training")
            continue
        else:
            print("something not working")
            break
    
    print("")
    print("-------------------------------------------------------------")
    print("")

    print(sourceFaceId)
    matches = CF.face.identify([sourceFaceId],large_person_group_id=largePersonGroupId, max_candidates_return = 5)
    print(matches)
    time.sleep(1)
    for match in matches:
        for candidates in match['candidates']:
            person = CF.large_person_group_person.get(largePersonGroupId, candidates["personId"])
            print("found possible match " + person['name'])
            print(person)
            targetPerson = [p for p in Persons if p ['personId'] == person ['personId']]
            for p in targetPerson:
                for image in p["faces"]:
                    os.startfile(image)


    return


def large_group_delete(largePersonGroupId):
    CF.large_person_group.delete(largePersonGroupId)
    return