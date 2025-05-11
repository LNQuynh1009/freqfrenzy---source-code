import numpy as np
from PIL import Image

def embed_watermark(image_path, output_path):
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)
    
    # Compute DFT
    dft = np.fft.fft2(img_array)
    
    # Embed watermark (1010 at (3,3)-(3,6))
    watermark_coords = [(2,2), (2,3), (2,4), (2,5)]  # 0-based
    watermark_values = [60, 40, 60, 40]
    for (u, v), val in zip(watermark_coords, watermark_values):
        dft[u, v] = val + 0j
    
    # Inverse DFT
    img_array = np.fft.ifft2(dft).real
    img_array = np.clip(img_array, 0, 255).astype(np.uint8)
    
    # Save
    Image.fromarray(img_array).save(output_path)

if __name__ == "__main__":
    embed_watermark("input.jpg", "watermarked.jpg")