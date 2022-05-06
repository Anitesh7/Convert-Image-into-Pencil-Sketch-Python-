
import cv2

img_location = 'D:/VS CODE/Python/'
filename = 'AR8.jpg'

org_image = cv2.imread(img_location+filename)
resize_image = cv2.resize(org_image, (550, 450))

gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
inverted_gray_image = 255 - gray_image
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 8)
inverted_blurred_img = 255 - blurred_image

pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_img, scale=300.0)

# cv2.imshow("Original Image", org_image)
cv2.imshow("Original Image", resize_image)
# cv2.imshow("Gray Image", gray_image)
# cv2.imshow("Inverted Gray Image", inverted_gray_image)
# cv2.imshow("Inverted Gray Image", inverted_gray_image)
# cv2.imshow("Blurred Image", blurred_image)
# cv2.imshow("Inverted Blurred Image", inverted_blurred_img)
cv2.imshow("Pencil Sketch Image", pencil_sketch_image)
cv2.waitKey(0)
