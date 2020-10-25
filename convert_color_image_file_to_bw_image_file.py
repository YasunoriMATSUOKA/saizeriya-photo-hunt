import os
import cv2
import numpy as np
from create_dir_before_write_file import create_dir_before_write_file


def convert_color_image_file_to_bw_image_file(color_image_file_path, bw_image_file_path):
    color_image = cv2.imread(color_image_file_path)
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    threshold_value, bw_image = cv2.threshold(
        gray_image, 0, 255, cv2.THRESH_OTSU)
    create_dir_before_write_file(bw_image_file_path)
    cv2.imwrite(bw_image_file_path, bw_image)
