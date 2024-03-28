import cv2

img = cv2.imread('images/color_text.jpg')

# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img1 = cv2.GaussianBlur(img1, (3, 3), 0)
img1 = cv2.Canny(img1, 20, 25)

img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

a = len(img1)
for i in range(170):
    for j in range(len(img1[i])):
        img1[i][j][0] = 0
        img1[i][j][2] = 0

for i in range(152, 170):
    for j in range(560, len(img1[i])):
        for k in img1[i][j]:
            if img1[i][j][1] != 0:
                img1[i][j] = ([0, 0, 255])


for i in range(170, 303):
    for j in range(len(img1[i])):
        img1[i][j][0] = 0
        img1[i][j][1] = 0

for i in range(303, a):
    for j in range(len(img1[i])):
        for k in img1[i][j]:
            if img1[i][j][0] == 255:
                img1[i][j] = ([230, 11, 148])

for i in range(303, 320):
    for j in range(650, len(img1[i])):
        for k in img1[i][j]:
            if img1[i][j][0] != 0:
                img1[i][j] = ([0, 0, 255])


cv2.imshow('Result', img1)
cv2.waitKey(0)  # показывание картинки бесконечного кол-ва времени
