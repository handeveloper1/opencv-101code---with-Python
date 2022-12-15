import cv2

framewidth = 640   #pencere boyutlandırma
frameheight = 480

cap = cv2.VideoCapture("test.mp4")
#cap = cv2.VideoCapture(0)   #böyle yaparsak webcami kullanır.
while True:
    success, img = cap.read()
    img = cv2.resize(img, (framewidth, frameheight))
    cv2.imshow("TitleName", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):   #pencereyi kapatmak için Q bas
        break