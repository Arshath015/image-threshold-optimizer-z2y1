import cv2
import numpy as np

def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def calculate_threshold(image):
    std_dev = np.std(image)
    hist, bins = np.histogram(image, 256, [0, 256])
    threshold = np.argmax(hist) + std_dev
    return threshold