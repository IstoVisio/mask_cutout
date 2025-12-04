# mask_cutout
Create TIFF stacks containing cutouts of the original image data where a given mask exists, using syGlass-exported segmentation as input.

## Usage

First, ensure that Python 3 and all dependecies are installed. If a dependency such as `tifffile` is missing, you can typically install it via `pip` from the command line, e.g. `pip install tifffile`.

Modify the mask, image, and results directories in [`mask_cutout.py`](mask_cutout.py). The mask and image directories should correspond to the directories where the mask and image TIFF files were exported from syGlass. The results directory is the directory in which you'd like the output image stacks to be placed.

https://github.com/IstoVisio/mask_cutout/blob/3cc02a74a65d90d7674f8283d9dfc246a8a0af41/mask_cutout.py#L6-L10

Finally, from the command line, run `python mask_cutout.py`. When the script has finished, a separate TIFF stack for each mask should be written to the results directory, each containing the bits of the original image stack that were overlapped by that mask, with black (zero) values elsewhere.
