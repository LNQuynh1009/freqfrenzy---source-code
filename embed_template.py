import numpy as np
from PIL import Image

def embed_template(image_path, output_path):
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)
    
    # Compute DFT
    dft = np.fft.fft2(img_array)
    
    # Embed template (~200 at (2,2), (2,6), (6,2), (6,6))
    template_coords = [(1,1), (1,5), (5,1), (5,5)]
    for u, v in template_coords:
        dft[u, v] = 200.0 + 0j
    
    # Inverse DFT
    img_array = np.fft.ifft2(dft).real
    img_array = np.clip(img_array, 0, 255).astype(np.uint8)
    
    # Save
    Image.fromarray(img_array).save(output_path)

if __name__ == "__main__":
    embed_template("watermarked.jpg", "templated.jpg")