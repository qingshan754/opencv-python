import cv2
import numpy as np

width, height = 512, 512
image = np.zeros((height, width), dtype=np.uint8)  # 全黑背景
center = (width // 2, height // 2)  # 圆心
radius = 200  # 圆半径

# 生成线性渐变（水平方向）
for y in range(height):
    for x in range(width):
        dist = np.sqrt((x - center[0])**2 + (y - center[1])**2)
        if dist <= radius:
            # 从左到右渐变（x 坐标影响亮度）
            image[y, x] = int(255 * (x / width))

cv2.imshow("Linear Gradient Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()