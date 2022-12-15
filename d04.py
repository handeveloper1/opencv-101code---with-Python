import cv2

img = cv2.imread("test.jpg")
print(img.shape)  #image boyutları

imgcropped = img[300:450,180:600]  #kroplama

imgResize = cv2.resize(img,(480,480))



cv2.imshow("image crop", imgcropped)
cv2.imshow("test", img)
cv2.imshow("imgResize", imgResize)   #yeniden boyutlandırma

cv2.waitKey(0)