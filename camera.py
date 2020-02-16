import cv2
import numpy as np


class Camera:
    def __init__(self, port):
        self.video = cv2.VideoCapture(port)
        self.check, self.frame = self.video.read()
        self.height, self.width, self.channels = self.frame.shape
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        self.option = 0
        self.x, self.y = 0, 0

    def blur_cont(self, f):
        gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        ret, thresh_img = cv2.threshold(blur, 175, 200, cv2.THRESH_BINARY)
        edged = cv2.Canny(thresh_img, 50, 150)
        return edged

    def boxed(self, cont, image):
        x, y, w, h = cv2.boundingRect(cont)
        color = (0, 255, 0)
        boxedImg = cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        return boxedImg, int((2 * x + w) / 2), int((2 * y + h) / 2)

    def gray_cont(self, f):
        gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        edged2 = cv2.Canny(gray, 50, 150)
        ret2, thresh_img2 = cv2.threshold(edged2, 175, 200, cv2.THRESH_BINARY)
        return thresh_img2

    def contour(self, image, f):
        contours, hierarchy = cv2.findContours(image, 0, 1)
        cnts = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        cnt = cnts[0]

        img_, midX, midY = self.boxed(cnt, f)
        return img_, midX, midY

    def options(self, opt):
        self.option = opt

    def update_frame(self):
        self.check, self.frame = self.video.read()

    def convert_frame(self):
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

    def green(self):
        lower_green = np.array([70, 90, 0])
        upper_green = np.array([100, 255, 255])
        mask = cv2.inRange(self.hsv, lower_green, upper_green)
        res = cv2.bitwise_and(self.frame, self.frame, mask=mask)
        return res

    def yellow(self):
        lower_yellow = np.array([20, 70, 0])
        upper_yellow = np.array([60, 230, 255])
        mask = cv2.inRange(self.hsv, lower_yellow, upper_yellow)
        res = cv2.bitwise_and(self.frame, self.frame, mask=mask)
        return res

    def blue(self):
        lower_blue = np.array([100, 70, 0])
        upper_blue = np.array([120, 240, 255])
        mask = cv2.inRange(self.hsv, lower_blue, upper_blue)
        res = cv2.bitwise_and(self.frame, self.frame, mask=mask)
        return res

    def boxing(self):
        cv2.waitKey(1)
        if self.option == 1:
            res = self.green()
        elif self.option == 2:
            res = self.yellow()
        elif self.option == 3:
            res = self.blue()
        else:
            return

        try:
            gray = self.gray_cont(res)
            img, self.x, self.y = self.contour(gray, self.frame)
        except:
            return

    def get_x_y(self):
        return self.x, self.y

    def set_power(self):
        return 180 * (self.x / self.width)

    def windows(self):
        cv2.imshow('frame', self.frame)
