import cv2
import time
from datetime import datetime
import argparse
import os

#cv2 is used for image detection task
#datetime to get exact time to compare image
#argparse is used to combine all the image and create a video
#os is used for file handling

face_casacde=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#Face cascade is file which contains the all the features of a face in xml file
#for every face there is cascade file,like we have cat cascade ,dog cascade etc

video=cv2.VideoCapture(0)
#to take the input from our cam,here 0 represents the our own cam

while True:
    check,frame=video.read()
    if frame is not None:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cvtColor used to convert rbg image to gray for easy feature analysis
        faces=face_casacde.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)
        #face_casacde is used for detect features of face.
        #if human face is detected draw a rectangle around face
        for x,y,w,h in faces:
            img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            #we are going to draw the image around the frame not on the gray image.
            #gray image is used for only image detection
            #x,y are starting cordinates.w-width,h-height,(0,255,0) is color
            #and 3 represents the width of the rectangle
            exact_time=datetime.now().strftime('%Y-%b-%d-%H-%S-%f')
            cv2.imwrite("face detected"+str(exact_time)+".jpg",img)
            #imwrite is used for file name.

        cv2.imshow("home surv",frame)
        key=cv2.waitKey(1)

        if key==ord('q'):
            #if user click on q.
            ap=argparse.ArgumentParser()
            ap.add_argument("-ext","--extension",required=False,default='jpg')
            #adding input
            ap.add_argument("-o","--output",required=False,default="output.mp4")
            #getting output
            args=vars(ap.parse_args())


            dir_path='.'
            ext=args['extension'] #input
            output=args['output'] #output

            images=[]

            for f in os.listdir(dir_path):
                #used to find the jpg file in the directory and add it to image list
                if f.endswith(ext):
                    images.append(f)

            image_path=os.path.join(dir_path,images[0])
            #we need to find height and width of video,so we can find it by the first image
            frame=cv2.imread(image_path)
            height,width,channels=frame.shape

            forcc=cv2.VideoWriter_fourcc(*"mp4v")
            #video format
            out=cv2.VideoWriter(output,forcc,5.0,(width,height))


            for image in images:
                image_path=os.path.join(dir_path,image)
                frame=cv2.imread(image_path)
                out.write(frame)
                #the video is slide show of images

            break

video.release()
cv2.destroyAllWindows



