import itk
import numpy as np
import matplotlib.pyplot as plt

## Read data and plot metadate
img = itk.imread('data/sag.mha')
meta = itk.dict_from_image(img)
print(f"Size: {img.shape}")
print(f"Spacing: {meta['spacing']}")
print(f"Origin: {meta['origin']}")


