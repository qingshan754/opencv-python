import cv2

# 读取彩色图像
color_img = cv2.imread('D:\打印\导出\P1016084.JPG')  # 替换为你的图片路径

# 转换为灰度图
gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

# 保存灰度图像
cv2.imwrite('gray_image.jpg', gray_img)

sobelx=cv2.Sobel(gray_img,cv2.CV_64F,1,0,ksize=3)
sobelx=cv2.convertScaleAbs(sobelx)
sobely=cv2.Sobel(gray_img,cv2.CV_64F,0,1,ksize=3)
sobely=cv2.convertScaleAbs(sobely)
sobelxy=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)

cv2.namedWindow('sobelxy', cv2.WINDOW_NORMAL)  # 使窗口可调整
cv2.imshow('sobelxy',sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()