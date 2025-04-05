import cv2
import numpy as np
import matplotlib.pyplot as plt
#调用文件夹中的照片
img=cv2.imread(r'E:\证件照\mmexport1695807557875.jpg')
#显示照片
cv2.imshow('image',img)
#等待时间，0表示毫秒
cv2.waitKey(0)
#关闭窗口
cv2.destroyAllWindows()

print(img.size)


