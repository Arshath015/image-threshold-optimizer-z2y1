import cv2
import numpy as np
from image_utils import load_image, calculate_threshold

def main(image_path):
    image = load_image(image_path)
    threshold = calculate_threshold(image)
    binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('Binary Image', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main('image.jpg')