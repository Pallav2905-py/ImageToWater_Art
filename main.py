'''
To Convert An Image Into Water Art: 

#Step-1 : Resize Image
#Step-2 : Clear Impurities [Using MedianBluring / Edge Filtering]
#Step-3 : Apply Filtering
#Step-4 : Turning Into Art And Tuning It!
'''


import cv2
#To Read Image
image = cv2.imread('img.jpeg')

#Step-1:
image_resized = cv2.resize(image,None,fx=1,fy=1)

#step-2:
image_cleared = cv2.medianBlur(image_resized,3)
image_cleared = cv2.medianBlur(image_cleared,3)
image_cleared = cv2.medianBlur(image_cleared,3)
image_cleared = cv2.edgePreservingFilter(image_cleared,sigma_s=5) #Sigma_s color ko mila degi

# Step-3
image_filtered = cv2.bilateralFilter(image_cleared, 3, 5, 0)
image_filtered = cv2.bilateralFilter(image_filtered,3,10,10)
image_filtered = cv2.bilateralFilter(image_filtered, 5, 15, 20)

#Step - 4
gaussian_mask = cv2.GaussianBlur(image_filtered,(11,11),2)
image_sharp = cv2.addWeighted(image_filtered,2.5,gaussian_mask,-1.5,15)

#To Show OutPut
cv2.imshow('art',image_sharp)
cv2.waitKey(0)