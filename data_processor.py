import numpy as np
import cv2

from person import Person

import pdb


face_cascade = cv2.CascadeClassifier('haar_cascades/haarcascade_face.xml')
eye_cascade = cv2.CascadeClassifier('haar_cascades/haarcascade_eye.xml')

def generate_people(img):
        # pdb.set_trace()
        people = []

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for i, (x, y, w, h) in enumerate(faces):
                person = Person(img)
                roi_gray = gray[y:y+h, x:x+w]
                person.face = img[y:y+h, x:x+w]

                eyes = eye_cascade.detectMultiScale(roi_gray)
                for j, (ex, ey, ew, eh) in enumerate(eyes):
                        if j == 0:
                                person.eye_left = person.face[ey:ey+eh, ex:ex+ew]
                        else:
                                person.eye_right = person.face[ey:ey+eh, ex:ex+ew]

                if person.is_valid():
                        people.append(person)
                else:
                        print("Failed to generate valid face data")
        
        return people