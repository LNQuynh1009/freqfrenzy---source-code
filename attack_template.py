import numpy as np
from PIL import Image

def attack_template(image_path, output_path):
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)
    
    # Compute DFT
    dft = np.fft.fft2(img_array)
    
    # Remove template (~200 to ~50)
    template_coords = [(1,1), (1,5), (5,1), (5,5)]
    for u, v in template_coords:
        dft[u, v] = 50.0 + 0j
    
    # Inverse DFT
    img_array = np.fft.ifft2(dft).real
    img_array = np.clip(img_array, 0, 255).astype(np.uint8)
    
    # Save
    Image.fromarray(img_array).save(output_path)

if __name__ == "__main__":
    attack_template("templated.jpg", "attacked.jpg")