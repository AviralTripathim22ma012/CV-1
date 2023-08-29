# CV-1
# REPORT

Colab link for the entire assignment: m22ma012_CV_Assignment_1.ipynb - Colaboratory (google.com)
## Q1- Spotting differences
Colab link: m22ma012_Q1.ipynb - Colaboratory (google.com)
First I cropped the given image into 2 images, between which the differences are to be spotted, then I converted both the images into grayscale, and used structural_simillarity( ) function to find the structural similarity between both the images
The difference between the two images is then calculated and displayed as an image. The difference image is thresholded using Otsu's thresholding method, and contours are found in the thresholded image. The contours are filtered based on their areas, and if their area is greater than or equal to 10000, a rectangle is drawn around the contour in both the original images and the number of differences is incremented.
## Q2- Finding distances on a map
Colab link: m22ma012_Q2.ipynb - Colaboratory (google.com)
I gave used blob detection using cv2.SimpleBlobDetector_create( ) function of open cv, to detect the various cities located on map by small black dots, some major limitations of this method is that:
Apart from black dots, some letters in text, written on the map, are also detected, which were not to be detected
## Q3- Area & perimeter of a circle
Colab link: m22ma012_Q3.ipynb - Colaboratory (google.com)
I have used cv2.HoughCircles( ) function in open cv to find the values of radius and centre of detected circle, the given image of circle was detected at the following parameter values:
 PARAM1= 100
 PARAM2= 100
Following results were obtained:
 coordinates of detected circle's centre, and radius: [[[288 264 223]]]
 the radius of the given circle is: 223
 circumference: 1400.44
 area: 1.4575262441074674e+113
## Q4- Angle between minute and hour hands
Colab link: m22ma012_Q4.ipynb - Colaboratory (google.com)
I have used canny edge detection and HoughLines to first obtain the edges and then find lines, after which I used cv.lines( ) to draw lines, extracted the end points of detected lines and found the angle between them using the following formula:
angle = np.arctan2(y4-y3, x4-x3) - np.arctan2(y2-y1, x2-x1)
here x1, x2, x3, x4, y1, y2, y3, y4, are end points
following were the results obtained
 for image- clock_1.png: -119.05460409907714
 for image- clock_2.png: 117.96521503040182
## Q5- Landmark images
Colab link: m22ma012_Q5.ipynb - Colaboratory (google.com)
As my name starts with “A” (Aviral), I chose the images of Amsterdam Tulip museum, I resized the 3 images into 256x256 using cv2.resize( ), converted them into grey using cv2.cvtColor( ), found the average, subtracted image 1 from image 2, added Gaussian noise, and removed the noise using cv2.medianBlur( )
(average image) (image-1 subtracted from image-2)
(original image-1) (adding Gaussian noise in image-1) (median blur to remove noise)
(applying {−1, −1, −1; 0, 0, 0; 1, 1, 1} kernel on image-1)
## Q6- Digit recognition on MNIST dataset
Colab link: m22ma012_Q6.ipynb - Colaboratory (google.com)
For computing horizontal projection, which is the sum of pixel intensity of each row of the image, I used np.sum(img, axis=1), thereafter I used knn and svm from skLearn to perform the required tasks, following were the accuracies found in each case:
 Knn: 0.9
 SVM: 0.9
## Q8- Template matching
Colab link: m22ma012_Q8.ipynb - Colaboratory (google.com)
I have used TM_CCOEFF_NORMED method to perform template matching:
(template)
(template matching using TM_CCOEFF_NORMED)
It can be observed that the template matching has not detected the entire letter, the following may be the reasons for the same:
 Scale and rotation variability: If the template and the image being searched have different scales or rotations, it can be difficult to find a match using template matching.
 Similar patterns: If there are similar patterns in the image that resemble the template, it can result in false positives or difficulty in finding the correct match.
 Template size: If the template size is not well suited for the size of the object being searched, it can result in a poor match.
## Q9- Histogram equalization
Colab link: m22ma012_Q9.ipynb - Colaboratory (google.com)
Following histogram and cdf were obtained for this image:
After histogram equalization:
## Q10- Last 3 digits of mobile number
Colab link: m22ma012_Q10.ipynb - Colaboratory (google.com)
I have used pyocr OCR library to detect the last 3 digits of given images of mobile numbers:
