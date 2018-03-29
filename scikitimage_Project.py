"""
    File name: scikitimage_Project.py
    Author: Alex Ragalie - aragalie.com
    Date created:       23 March 2018
    Date last modified: 23 March 2018
    Python Version: 3.6

OBJECTIVE

Use a 5x5 window to scan over the greyscale image, where a pixel value is a float in the range 0 to 1.

The values have to be normalised so that within one window the smallest value is scaled to 0 and the largest to 1.

OUTPUT

Data export to .csv, in a table with 25 columns and 13,824 rows.

"""

import os
import pandas as pd
import matplotlib.pyplot as plt

from skimage.color import rgb2gray
from skimage import io

# Set the working directory
os.chdir("insert_directory_path_here")

# 1- Test that the algorithm works

# Load a 10x10px image
filename = 'img3.jpg'
img_test = io.imread(filename)

# Convert the image to greyscale
img = rgb2gray(img_test)

# 1.1 - Set each alternate pixel to black/white
i = 1
for col in range(10):
    i += 1
    for row in range(10):
        if i % 2 == 0:
            img[row, col] = 0
            i += 1
        else:
            img[row, col] = 1
            i += 1

# Save the test file to disk
plt.imsave('test.png', img, cmap=plt.cm.gray)

# 1.2 - Check the result
plt.imshow(img)

# 1.3 - Scan with the 5x5 window and output to .csv

# Create a list with all the column names
col_names_coordinate = []
i = 0
while i < 5:
    for x in range(5):
        col_names_coordinate.append((i, x))
    i += 1

# Create a DataFrame to hold the output
df = pd.DataFrame(columns=col_names_coordinate)

# Save all pixel values in the DataFrame based on the position of the 5x5 window
df_row_number = 0
for x in range(0, img.shape[0], 5):
    for y in range(0, img.shape[1], 5):
        top_left = (x, y)
        bottom_right = (x + 4, y + 4)
        new_row = []
        for window_h in range(x, x + 5):
            for window_w in range(y, y + 5):
                new_row.append(img[window_h, window_w])
        df.loc[df_row_number] = new_row
        df_row_number += 1

# Output the Dataframe to csv
df.to_csv('output_test.csv')

# TEST COMPLETE


# 2 - Import an actual 720x480 image and process it; img2.jpg can be used as well

filename = 'img1.jpg'
img_rgb = io.imread(filename)

# Convert the image to greyscale
img = rgb2gray(img_rgb)

# Create a list with all the column names
col_names_coordinate = []
i = 0
while i < 5:
    for x in range(5):
        col_names_coordinate.append((i, x))
    i += 1

# Create a DataFrame to hold the output
df = pd.DataFrame(columns=col_names_coordinate)

# Save all pixel values in the DataFrame based on the position of the 5x5 window
df_row_number = 0
for x in range(0, img.shape[0], 5):
    for y in range(0, img.shape[1], 5):
        top_left = (x, y)
        bottom_right = (x + 4, y + 4)
        new_row = []
        for window_h in range(x, x + 5):
            for window_w in range(y, y + 5):
                new_row.append(img[window_h, window_w])
        df.loc[df_row_number] = new_row
        df_row_number += 1

# Output the Dataframe to csv
df.to_csv('output.csv')
