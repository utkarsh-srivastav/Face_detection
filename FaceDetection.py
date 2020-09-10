import cv2

# creates cascade classifier object
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# reading img
# img = cv2.imread("C:\\Users\\hp\\Desktop\\DSC_6867.jpg")
# convert to gray scale img
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# search the coord of the img
# faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)
    print(faces)

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 300, 0), 2)
    cv2.putText(img, " Hello Dear ", (x, y), cv2.FONT_ITALIC, 1, (255, 255, 0), 3)
    cv2.imshow("window_name", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
