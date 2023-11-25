# data_science_internship
# Face Detection Model Comparison

This repository contains an analysis and comparison of three pretrained face detection models: DLIB_CNN, DLIB_HOG_CNN, and MTCNN. The evaluation focuses on their performance in handling unstructured data, particularly images.

## Models

### DLIB_CNN
DLIB_CNN is a face detection model utilizing a Convolutional Neural Network (CNN) based on the "mmod_human_face_detector.dat" pre-trained model provided by the dlib library. This model excels in discerning facial features within images.

### DLIB_HOG_CNN
DLIB_HOG_CNN is a hybrid model combining both dlib's `cnn_face_detection_model_v1` and `get_frontal_face_detector()`. It integrates the strengths of CNN and Histogram of Oriented Gradients (HOG) techniques, using the "mmod_human_face_detector.dat" model for enhanced face detection, particularly focusing on frontal poses.

### MTCNN (Multi-Task Cascaded Convolutional Networks)
MTCNN, implemented through the facenet_pytorch library, employs a cascaded architecture of neural networks for face detection and facial landmark localization. Recognized for its effectiveness in real-time face detection, MTCNN excels in handling diverse angles and poses.

## Evaluation Metrics
The comparison of these models is based on critical performance metrics, including:
- False Positive Rate
- Precision
- Execution Time

## Usage
To replicate the evaluation or use these models in your projects, follow the instructions in the respective model directories.

## Dependencies
For HOG_CNN and HOG_Front_CNN:

dlib

For MTCNN:

facenet_pytorch
imutils
skimage (io)

Common Dependancies:

OpenCV (cv2)
time
os
urllib.request
numpy (np)
scikit-learn (sklearn)

## Citation
If you find this work helpful, consider citing this repository.

## License
This project is licensed under the [MIT License].
