import cv2
import numpy as np

logo = np.zeros((300, 300, 3), dtype='uint8')
size = (300, 300, 3)
square = np.zeros(size, dtype='uint8')
i = 0
k = 0
r = 255
for _ in range(r):
    # square = cv2.cvtColor(square, cv2.COLOR_BGR2GRAY)
    square[:, 0 + i:r + i] = (0 + k, 0 + k, 0 + k)
    i += 1
    k += 1
# Почему мой градиент не поворачивается?
# def rotate(img_param, angle):
#     height, width = img_param.shape[:2]
#     point = (width//2, height//2)
#     mat = cv2.getRotationMatrix2D(point, angle, 1)
#     return cv2.warpAffine(img_param, mat, (width, height))
# rot = rotate(square, 180)

logo[:] = 230, 59, 103

# Круги
cv2.circle(logo, (88, 145), 58, (255, 255, 255), thickness=cv2.FILLED)
# cv2.circle(logo, (88, 145), 34, (230, 59, 103), thickness=cv2.FILLED)
cv2.circle(logo, (217, 66), 44, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(logo, (217, 66), 22, (230, 59, 103), thickness=cv2.FILLED)
cv2.circle(logo, (217, 159), 44, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(logo, (217, 159), 22, (230, 59, 103), thickness=cv2.FILLED)
# Маски
# cv2.rectangle(logo, (26, 82), (150, 145), (230, 59, 103), thickness=cv2.FILLED)
cv2.rectangle(logo, (169, 18), (265, 66), (230, 59, 103), thickness=cv2.FILLED)
cv2.rectangle(logo, (169, 111), (265, 159), (230, 59, 103), thickness=cv2.FILLED)
# прямоугольники
# cv2.rectangle(logo, (30, 31), (54, 145), (255, 255, 255), thickness=cv2.FILLED)
cv2.rectangle(logo, (30, 31), (146, 145), (255, 255, 255), thickness=cv2.FILLED)
# cv2.rectangle(logo, (122, 31), (146, 145), (255, 255, 255), thickness=cv2.FILLED)
# cv2.rectangle(logo, (54, 31), (122, 55), (255, 255, 255), thickness=cv2.FILLED)

cv2.rectangle(logo, (173, 31), (195, 66), (255, 255, 255), thickness=cv2.FILLED)
cv2.rectangle(logo, (239, 31), (261, 66), (255, 255, 255), thickness=cv2.FILLED)

cv2.rectangle(logo, (173, 124), (195, 159), (255, 255, 255), thickness=cv2.FILLED)
cv2.rectangle(logo, (239, 124), (261, 159), (255, 255, 255), thickness=cv2.FILLED)

# НЕДОЛОГО
cv2.circle(logo, (88, 145), 50, (0, 0, 0), thickness=cv2.FILLED)
cv2.circle(logo, (88, 145), 50, (230, 59, 103), thickness=2)
cv2.ellipse(logo, (88, 155), (24, 20), 0, 0, 180, (0, 255, 0), 2)
cv2.ellipse(logo, (88, 155), (12, 10), 0, 0, 180, (0, 255, 0), 2)
cv2.line(logo, (76, 155), (76, 130), (255, 0, 0), thickness=2)
cv2.line(logo, (64, 155), (64, 130), (255, 0, 0), thickness=2)
cv2.line(logo, (100, 155), (100, 130), (255, 0, 0), thickness=2)
cv2.line(logo, (112, 155), (112, 130), (255, 0, 0), thickness=2)
cv2.line(logo, (64, 130), (76, 130), (0, 0, 255), thickness=2)
cv2.line(logo, (100, 130), (112, 130), (0, 0, 255), thickness=2)

# Текст
cv2.putText(logo, 'Urban University', (20, 260), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.15, (255, 255, 255), 1)

cv2.imshow('photo', logo)
cv2.imshow('photo2', square)
cv2.waitKey(0)
