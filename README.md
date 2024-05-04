# Basic tasks in CV

## Q1- Spotting differences
I cropped the given image into 2 images, converted both to grayscale, and used structural similarity function to find differences. Otsu's thresholding method was applied to the difference image, and contours were found. Contours with areas ≥ 10000 were highlighted.

## Q2- Finding distances on a map
Blob detection using OpenCV's function detected cities as small black dots but also mistakenly detected some text.

## Q3- Area & perimeter of a circle
OpenCV's HoughCircles function was used to detect circle parameters. Detected circle: centre coordinates (288, 264), radius 223. Calculated circumference: 1400.44, area: 1.4575262441074674e+113.

## Q4- Angle between minute and hour hands
Canny edge detection and HoughLines were used to detect edges and lines. The angle between hour and minute hands was calculated.

## Q5- Landmark images
Images of Amsterdam Tulip museum were processed. Gaussian noise was added and removed. Kernel was applied for enhancement.

## Q6- Digit recognition on MNIST dataset
Horizontal projection and machine learning models (knn and svm) were used for digit recognition. Achieved accuracies: Knn - 0.9, SVM - 0.9.

## Q8- Template matching
Template matching using TM_CCOEFF_NORMED method was performed. Challenges include scale/rotation variability, similar patterns, and template size.

## Q9- Histogram equalization
Histogram and cdf were obtained for the image. Histogram equalization was applied.

## Q10- Last 3 digits of mobile number
Pyocr OCR library was used to detect the last 3 digits of given mobile number images.
