import cv2
import numpy as np
from PIL import Image

def attack_linear(image_path, output_path):
    img = Image.open(image_path).convert('L')
    img_array = np.array(img)
    
    # Resize 50% (bilinear interpolation)
    resized = cv2.resize(img_array, (4, 4), interpolation=cv2.INTER_LINEAR)
    img_array = cv2.resize(resized, (8, 8), interpolation=cv2.INTER_LINEAR)
    
    # Save
    Image.fromarray(img_array).save(output_path)

if __name__ == "__main__":
    attack_linear("templated.jpg", "transformed.jpg")