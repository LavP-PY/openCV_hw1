import cv2

vid = cv2.VideoCapture(0)
eyes_casc = cv2.CascadeClassifier('eyes.xml')

while True:
    success, img = vid.read()  # значение true/false в переменную success.
    results = eyes_casc.detectMultiScale(img, scaleFactor=3, minNeighbors=2)

    for x, y, w, h in results:
        const = img[y - h//4: y + h + h//4, x - w//2: x + w + w //2]
        img2 = const
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
        img2 = cv2.GaussianBlur(img2, (23, 23), sigmaX=10, sigmaY=10)
        img[y - h//4: y + h + h//4, x - w//2: x + w + w//2] = img2


    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
