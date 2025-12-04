import os
from tifffile import imread, imwrite
import numpy as np
import shutil

# Configure these three fields to match the directories containin the outputs from syGlass
# and the directory where you'd like the result images to be written
IMAGE_DIR = r'C:\Users\natha\Downloads\88-0412-OG_647_ROI-2\Image'
MASK_DIR = r'C:\Users\natha\Downloads\88-0412-OG_647_ROI-2\Mask'
RESULTS_DIR = r'C:\Users\natha\Downloads\mask_labels_results'

# Ensure that results directory exists
if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

# Determine the masks present in the mask TIFFs
mask_ids = set()
for mask_path in os.listdir(MASK_DIR):
    img = imread(f"{MASK_DIR}/{mask_path}")
    mask_ids.update(np.unique(img))
mask_ids.discard(0)
print(f"\nMask IDs detected:\n{mask_ids}\n")

# Write new image TIFFs for each mask, only where that mask exists
mask_paths = os.listdir(MASK_DIR)
image_paths = os.listdir(IMAGE_DIR)
for mask_id in mask_ids:
    mask_dir = f"{RESULTS_DIR}/Mask{mask_id}"
    if os.path.exists(mask_dir):
        shutil.rmtree(mask_dir)
    os.makedirs(mask_dir)
    for i in range(0, len(mask_paths)):
        image = imread(f"{IMAGE_DIR}/{image_paths[i]}")
        mask = imread(f"{MASK_DIR}/{mask_paths[i]}")
        result = np.where(mask == mask_id, image, 0).astype(image.dtype)
        result_path = f"{mask_dir}/{image_paths[i][:-5]}_Mask-{mask_id}.tiff"
        imwrite(result_path, result, compression = 'zlib')
    print(f"Created TIFF stack for mask ID {mask_id}")
print("\nFinished!")