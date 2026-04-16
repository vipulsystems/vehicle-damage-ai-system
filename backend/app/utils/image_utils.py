import os
import cv2


def save_image(file, path):
    file.save(path)


def read_image(path):
    return cv2.imread(path)


def resize_image(image, size=(640, 640)):
    return cv2.resize(image, size)


def save_processed_image(image, path):
    cv2.imwrite(path, image)