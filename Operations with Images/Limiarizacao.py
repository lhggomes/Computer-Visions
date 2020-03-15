import cv2

img = cv2.imread("Photos/moedas.jpg",0)


adp1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                             cv2.THRESH_BINARY, 11, 2)

adp2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 11, 2)

cv2.imshow("original", img)
cv2.imshow("limiMedia", adp1)
cv2.imshow("LimGaussian", adp2)

cv2.waitKey(0)
cv2.destroyAllWindows()