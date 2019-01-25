import numpy as np
import cv2

from person import Person
from data_processor import generate_people

import pdb

# Load Image
img = cv2.imread('./assets/jonas.jpg', 1)



def main():

    # Create Face Data
    people = generate_people(img)

    for person in people:
        cv2.imshow('Person Face', person.face)
        cv2.imshow('Person Left Eye', person.eye_left)
        cv2.imshow('Person Right Eye', person.eye_right)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    


if __name__ == "__main__":
    main()