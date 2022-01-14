import cv2


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while 1:
    success, img = cap.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_img = 255 - gray_img
    blurred_img = cv2.GaussianBlur(inverted_gray_img, (21, 21), 0)
    inverted_blurred_img = 255 - blurred_img
    pencil_sketch_img = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)
    cv2.imshow("image", gray_img)
    cv2.imshow("Blurred image", pencil_sketch_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

