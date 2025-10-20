import cv2

image = cv2.imread(r"C:\Users\Thanveer Ahamed A\OneDrive\Desktop\NASRIN STUDYROOM\NASRIN 30 DAYS AI\Open CV Original And Gray Image\photo.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Gray", grayImage)
cv2.imwrite("graynew.png", grayImage)
print(image.shape)
print(image.size)
