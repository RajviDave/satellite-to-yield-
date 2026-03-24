import cv2
import os

image_folder = "filtered_images"
label_folder = "labels"

for img_name in os.listdir(image_folder):
    img_path = os.path.join(image_folder, img_name)
    label_path = os.path.join(label_folder, os.path.splitext(img_name)[0] + ".txt")

    img = cv2.imread(img_path)
    h, w, _ = img.shape

    # draw existing boxes
    if os.path.exists(label_path):
        with open(label_path, "r") as f:
            for line in f:
                cls, x, y, bw, bh = map(float, line.strip().split())

                x1 = int((x - bw/2) * w)
                y1 = int((y - bh/2) * h)
                x2 = int((x + bw/2) * w)
                y2 = int((y + bh/2) * h)

                cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)

    cv2.imshow("image", img)
    key = cv2.waitKey(0)

    if key == 27:  # ESC to exit
        break

cv2.destroyAllWindows()