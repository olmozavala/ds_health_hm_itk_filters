#  ITK Filters and resampling and access to HiperGator
The objectives of this homework are:
1. Practice image filters using ITK
2. Practice image resampling using ITK
3. Practice accessing HiperGator data folder

All the answer should be submitted in a single jupyter notebook. 

## Image resampling (10 points)
Use ITK to resample `data/sag.mha` into isotropic voxels of size 0.5 'spacing' units. 

Plot the middle slide of all the three planes (axial, coronal, sagittal) in a single figure.


## Image filtering (10 points)
Use any edge detection filter to detect the edges of 
the resampled image from the previous question.

You can use (itk, opencv, or scipy) for this task and can chose any filter from this list:
1. Sobel
2. Prewitt
3. Laplacian
4. Canny 

Plot the middle slide of all the three planes (axial, coronal, sagittal) in a single figure.

## Image morphological filters (15 points)

Use any morphological filters to improve the segmentation
provided in `data/sag_seg.png` for the `data/sag.png` image.
To make it easier, I have provided both images
as png. You can read it with any image reader.

The current segmentation is the following:

![Segmentation](https://github.com/olmozavala/ds_health_hm_itk_filters/blob/0d1bcd725435fcc6dd56290234f679c06d8a70df/data/CurrentSeg.png?raw=true | width=300)

Describe you approach and show the results in a single figure.
