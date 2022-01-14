import cv2

count = 1
img = cv2.imread('4.jpeg')
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_img = 255 - gray_img
blurred_img = cv2.GaussianBlur(inverted_gray_img, (21, 21), 0)
inverted_blurred_img = 255 - blurred_img
pencil_sketch_img = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)
# cv2.imshow("Image", img)
# cv2.imshow("Alternate image", gray_img)
cv2.imshow("Blurred image", pencil_sketch_img)
cv2.imwrite("NumberPlate_"+str(count)+".jpg", pencil_sketch_img)
cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
cv2.putText(img, "Saved Scan", (150, 265), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)
cv2.imshow("Result", img)
cv2.waitKey(500)
count = count+1
cv2.waitKey(0)
cv2.destroyAllWindows()

