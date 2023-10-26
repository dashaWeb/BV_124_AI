import cv2

img = cv2.imread('image/1.jpg')
cv2.imshow('Input image', img)

# Load the image in grayscale mode
gray_img = cv2.imread('image/1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale', gray_img)

# Saving an image
cv2.imwrite('image/output.jpg', gray_img)
cv2.waitKey()
