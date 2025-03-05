import cv2

# 載入 Haar Cascade 人臉偵測模型
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 開啟攝像頭（或指定影片文件）
cap = cv2.VideoCapture(0)  # '0' 是默認攝像頭

while True:
    # 捕捉每一幀
    ret, frame = cap.read()

    # 將圖片轉為灰階圖，這是大多數檢測算法的標準步驟
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用 Haar Cascade 偵測人臉
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # 在偵測到的人臉上畫矩形框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # 顯示結果
    cv2.imshow('Face Detection', frame)

    # 按 'q' 鍵退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放攝像頭並關閉所有視窗
cap.release()
cv2.destroyAllWindows()
