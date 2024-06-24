# Alpaca-Detection-Model-using-Yolo

## Overview
This project implements an object detection and recognition system specifically designed for detecting alpacas in uncontrolled environments. The system is built using the YOLO (You Only Look Once) model, which has been trained on a custom dataset comprising 142 images of alpacas captured in various uncontrolled settings.

## Key Features
1. Object Detection: The YOLO model detects the presence of alpacas within images.
2. Object Recognition: Once detected, the model identifies and recognizes individual alpacas within the image.
3. Custom Dataset: Training was conducted using a custom dataset of 142 images, carefully annotated to include alpaca bounding boxes.
4. Accuracy: Achieved an accuracy of 93% after just 15 epochs of training.

## Dataset and Training
The custom dataset used for training consists of 142 images, each depicting alpacas in diverse environmental conditions. Annotations were meticulously created to ensure precise bounding boxes around each alpaca instance, facilitating accurate model training.

## Model Architecture
The YOLO model was chosen for its real-time object detection capabilities and efficiency. The architecture is optimized to handle the complexities of detecting and recognizing alpacas amidst varying backgrounds and lighting conditions.

## Results
The model demonstrates robust performance in real-world scenarios, accurately detecting and recognizing alpacas across various environmental conditions. See the examples folder for visual results and inference outputs.
