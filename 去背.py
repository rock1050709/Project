import os
import time
import cv2
from rembg import remove
import matplotlib.pyplot as plt

# 單獨處理一張圖片
img_path = r"C:\Program Files\Intel\image\blood.jpg"

# 讀取圖片
img = cv2.imread(img_path)
if img is None:
    print(f"錯誤：無法讀取圖片 {img_path}")
else:
    img_rembag = remove(img)

    # 轉換顏色 (OpenCV 是 BGR，Matplotlib 需要 RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rembag = cv2.cvtColor(img_rembag, cv2.COLOR_BGR2RGB)

    # 顯示圖片
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("原始圖片")

    plt.subplot(1, 2, 2)
    plt.imshow(img_rembag)
    plt.title("去背圖片")

    plt.show()

# 批量處理整個資料夾
def background_remove(img_dir):
    """ 批量去除圖片背景，並將結果存到桌面 'image' 資料夾 """

    # 支援的圖片格式
    valid_formats = {".jpg", ".bmp", ".webp", ".jpeg", ".png", ".JPG"}

    # 取得符合格式的所有圖片
    paths = [os.path.join(img_dir, f) for f in os.listdir(img_dir) if os.path.splitext(f)[-1].lower() in valid_formats]

    print("符合資源圖片格式數量:", len(paths))

    if len(paths) > 0:
        # 設定桌面的 "image" 資料夾
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "image")
        os.makedirs(desktop_path, exist_ok=True)  # 確保資料夾存在

        d_t = time.time()  # 開始計時

        for path in paths:
            img = cv2.imread(path)

            # 確保圖片讀取成功
            if img is None:
                print(f"錯誤：無法讀取圖片 {path}")
                continue

            # 設定輸出檔案 (轉為 PNG)
            output_path = os.path.join(desktop_path, os.path.splitext(os.path.basename(path))[0] + ".png")
            print(f"處理圖片: {output_path}")

            # 去背處理
            output = remove(img)

            # 保存結果
            cv2.imwrite(output_path, output)

        d_t = time.time() - d_t  # 計算處理時間
        print("平均去背時間(s):", d_t / len(paths))

# 執行批量處理
img_dir = r"C:\Program Files\Intel\image"  # 設定圖片資料夾
background_remove(img_dir)
