import numpy as np
from PIL import Image

def recover_watermark(image_path, output_file):
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)
    
    # Compute DFT
    dft = np.fft.fft2(img_array)
    
    # Find template (~150 after bilinear)
    template_coords = [(1,1), (1,5), (5,1), (5,5)]
    if all(abs(dft[u,v]) > 140 for u,v in template_coords):
        scale = 0.5  # Assume 50% scaling
        watermark_coords = [(2,2), (2,3), (2,4), (2,5)]
        watermark = []
        for u, v in watermark_coords:
            val = abs(dft[u, v])
            watermark.append(1 if val > 50 else 0)
        with open(output_file, 'w') as f:
            f.write(''.join(map(str, watermark)))

if __name__ == "__main__":
    recover_watermark("transformed.jpg", "watermark.txt")