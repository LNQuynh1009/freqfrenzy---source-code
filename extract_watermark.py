import numpy as np
from PIL import Image

def extract_watermark(image_path, output_file):
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)
    
    # Compute DFT
    dft = np.fft.fft2(img_array)
    
    # Extract watermark
    watermark_coords = [(2,2), (2,3), (2,4), (2,5)]
    watermark = []
    for u, v in watermark_coords:
        val = abs(dft[u, v])
        watermark.append(1 if val > 50 else 0)
    with open(output_file, 'w') as f:
        f.write(''.join(map(str, watermark)))

if __name__ == "__main__":
    extract_watermark("attacked.jpg", "extracted.txt")