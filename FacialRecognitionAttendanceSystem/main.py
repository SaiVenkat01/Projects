import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

#face recognition is used to recognize faces and
# compares faces which are already in database
#cv2 is used to take input from external camera and process it
# and give it to the face recognition.

video_capture=cv2.VideoCapture(0)
#taking video from camera.0 represents the default camera.

jobs_image=face_recognition.load_image_file("photos/jobs.jpg")
jobs_encoding=face_recognition.face_encodings(jobs_image)[0]

tesla_image=face_recognition.load_image_file("photos/tesla.jpg")
tesla_encoding=face_recognition.face_encodings(tesla_image)[0]

tata_image=face_recognition.load_image_file("photos/tata.jpg")
tata_encoding=face_recognition.face_encodings(tata_image)[0]

sai_image=face_recognition.load_image_file("photos/sai.jpg")
sai_encoding=face_recognition.face_encodings(sai_image)[0]

known_face_encoding=[
    jobs_encoding,
    tesla_encoding,
    tata_encoding,
    sai_encoding
]
#we can load all photos using for loop

known_faces_names=[
    "jobs",
    "tesla",
    "tata",
    "sai"
]

students=known_faces_names.copy()

face_locations=[]
face_encodings=[]
face_names=[]


now=datetime.now()
current_date=now.strftime("%Y-%m-%d")

f=open(current_date+'.csv','w+',newline='')
lnwriter=csv.writer(f)
#we use it when we want to write in csv file

while True:
    signal,frame=video_capture.read()
    #reading the video input and then read method we are extracting data
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    #we are decreasing the size of the input that coming from web cam
    rgb_small_frame=small_frame[:,:,::-1]
    #we are converting it to rgb.video input is taken in bgr format
    if True:
        face_locations=face_recognition.face_locations(rgb_small_frame)
        #it detect whether a face is available in frame or not
        face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
        #face data is encoded.
        face_names=[]
        for face_encoding in face_encodings:
            matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
            #comparing the existing face with new face
            name=""
            face_distance=face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index=np.argmin(face_distance)
            #finds the best fix for our face.It gives a probability number and
            #based on that face is matched.
            if matches[best_match_index]:
                name=known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    print(name)
                    students.remove(name)
                    #to get rid of multiple times of getting entered.
                    #thats why we are removing
                    print(students)
                    current_time=now.strftime("%H-%M-%S")
                    lnwriter.writerow([name,current_time])

        cv2.imshow("attendance system",frame)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()
f.close()



