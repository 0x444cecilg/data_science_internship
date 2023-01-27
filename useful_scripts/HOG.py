import dlib
from skimage import io
import argparse

def detect_faces(image_path):
    # Load the pre-trained model
    face_detector = dlib.get_frontal_face_detector()

    # Load the image
    image = io.imread(image_path)

    # Detect faces in the image
    faces = face_detector(image, 1)

    # Print the number of faces detected
    print("Number of faces detected: {}".format(len(faces)))
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="path to the image file")
    args = parser.parse_args()
    detect_faces(args.image_path)
