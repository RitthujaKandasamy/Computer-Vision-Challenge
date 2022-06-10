# Import the useful libraries
import cv2
import matplotlib.pyplot as plt

# Load the image and transform in gray scale
img = cv2.imread("sudoku.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# plt.imshow(img_gray, cmap='gray')
# plt.show()



# Apply binary inverse on the threshold
ret,thresh_inv = cv2.threshold(img_gray, 210, 255, cv2.THRESH_BINARY_INV)       # To see all the boxes we need to set the value at least 210
plt.imshow(thresh_inv, cmap='gray')
plt.show()


