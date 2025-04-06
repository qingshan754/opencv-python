import cv2

# 尝试不同的摄像头索引（0, 1, 2...）
cap = cv2.VideoCapture(1)  # 如果失败，尝试 1 或其他索引

if not cap.isOpened():
    print("无法打开摄像头，请检查连接或索引！")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法获取帧")
        break

    cv2.imshow("Panasonic S5II", frame)
    if cv2.waitKey(1) == ord('q'):  # 按 'q' 退出
        break

cap.release()
cv2.destroyAllWindows()