# Import the useful libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np


# Load the image and transform in gray scale
# img = cv2.imread("sudoku.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # plt.imshow(img_gray, cmap='gray')
# # plt.show()

# # Apply binary inverse on the threshold
# ret,thresh_inv = cv2.threshold(img_gray, 210, 255, cv2.THRESH_BINARY_INV)       # To see all the boxes we need to set the value at least 210
# plt.imshow(thresh_inv, cmap='gray')
# plt.show()


def preprocessing(image):
    # Load the image and resize as a square
    img=cv2.imread(image)
    img=cv2.resize(img, (600,600))
    rgb_img=img.copy()

    # Switch the color from BGR to RGB and then from RGB to gray
    rgb_img=cv2.cvtColor(rgb_img, cv2.COLOR_BGR2RGB)
    gray_img=img.copy()
    gray_img=cv2.cvtColor(gray_img, cv2.COLOR_BGR2GRAY)

    # Set the threshold and find contours
    retval, threshold = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY_INV, +cv2.THRESH_OTSU)    
    contours, hierarchy  =cv2.findContours(threshold,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_contours=sorted(contours, key=cv2.contourArea, reverse=True)
    drawing = cv2.drawContours(rgb_img, sorted_contours[0], -1, (0,255,0), 2)
    x,y,w,h = cv2.boundingRect(sorted_contours[0])
    copy=rgb_img.copy()
    rect=cv2.rectangle(copy, (x,y), (x+w, y+h), (0,255,0), 2)
    cropped_img=threshold[y:y+h, x:x+w]
    cropped_img=cv2.resize(cropped_img, (504,504))
    for i in range(9):
        for j in range(9):
            image=cropped_img[i*56:(i+1)*56, j*56:(j+1)*56]
            f_name=f'digits/digit{i}.png'
            image=cv2.imwrite(f_name,image)
    plt.imshow(cropped_img, cmap='gray')
    plt.show()

    # Plot the result
    # plt.imshow(rect)
    # plt.show()


preprocessing('sudoku.png')


# def preprocess_image(path):
#     orig_img = cv2.imread(path)
#     img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
#     img = cv2.GaussianBlur(img, (9,9), 0)
#     retval, img = cv2.threshold(img, 0,255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#     img = cv2.morphologyEx(img, cv2.MORPH_OPEN, (9,9))

#     # img = cv2.bitwise_not(img,img)
#     ext_contours, ext_hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#     print(len(ext_contours))
#     contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     print(len(contours))
#     # img = cv2.bitwise_not(img,img)
#     cv2.drawContours(orig_img, contours, -1, (0, 255,0) , 2)
#     cv2.drawContours(orig_img, ext_contours, -1, (0, 255,0), 2)


#     return orig_img



# cv2.imwrite('preprocessed_output.png', preprocess_image('sudoku.png'))