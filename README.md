# mask_cutout & mask_split

`mask_cutout.py` creates separate TIFF stacks containing cutouts of the original image data where a given mask exists, using syGlass-exported segmentation as input. This can be useful for showing each part separately in Imaris, e.g.

`mask_split.py` create separate TIFF stacks as well, but each containing a binary mask (0 where mask doesn't exist, 1 where it does). This is useful for adding masks to Imaris.

## Usage

First, ensure that Python 3 and all dependecies are installed. If a dependency such as `tifffile` is missing, you can typically install it via `pip` from the command line, e.g. `pip install tifffile`.

Modify the mask, image, and results directories in [`mask_cutout.py`](mask_cutout.py) or in [`mask_split.py`](mask_split.py). The mask and image directories should correspond to the directories where the mask and image TIFF files were exported from syGlass. The results directory is the directory in which you'd like the output image stacks to be placed.

https://github.com/IstoVisio/mask_cutout/blob/3cc02a74a65d90d7674f8283d9dfc246a8a0af41/mask_cutout.py#L6-L10

Finally, from the command line, run `python mask_cutout.py` or `python mask_split.py`. When the script has finished, a separate TIFF stack for each mask should be written to the results directory, each containing the bits of the original image stack that were overlapped by that mask, with black (zero) values elsewhere, or, in the case of `mask_split.py`, a binary mask.
