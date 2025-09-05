
# 🐟 Fish Species Detection & Segmentation using YOLOv8

This project implements **YOLOv8 segmentation** to detect and segment 23 species of coral reef fish.  
The model is trained on a custom dataset and can identify, localize, and segment fish species in underwater images.

---

## 📌 Features
- Detects and segments **23 coral reef fish species**.
- Built using **YOLOv8-seg** (Ultralytics).
- Trained on a **custom dataset** with labeled bounding boxes and segmentation masks.
- Outputs include bounding boxes, class labels, confidence scores, and segmentation masks.

---

## 📂 Dataset
- **Train Path:** `/kaggle/input/fish4classification/dataset/dataset/images/train`
- **Validation Path:** `/kaggle/input/fish4classification/dataset/dataset/images/val`
- **Classes:** 23 fish species

### Supported Fish Species
1. Dascyllus reticulatus  
2. Plectroglyphidodon dickii  
3. Chromis chrysura  
4. Amphiprion clarkii  
5. Chaetodon lunulatus  
6. Chaetodon trifascialis  
7. Myripristis kuntee  
8. Acanthurus nigrofuscus  
9. Hemigymnus fasciatus  
10. Neoniphon sammara  
11. Abudefduf vaigiensis  
12. Canthigaster valentini  
13. Pomacentrus moluccensis  
14. Zebrasoma scopas  
15. Hemigymnus melapterus  
16. Lutjanus fulvus  
17. Scolopsis bilineata  
18. Scaridae  
19. Pempheris vanicolensis  
20. Zanclus cornutus  
21. Neoglyphidodon nigroris  
22. Balistapus undulatus  
23. Siganus fuscescens  

---

## ⚙️ Installation
```bash
# Clone repo
git clone https://github.com/<your-username>/fish-segmentation.git
cd fish-segmentation

# Install dependencies
pip install ultralytics
pip install -r requirements.txt


---

## 🚀 Training

```python
from ultralytics import YOLO

# Load model
model = YOLO("yolov8s-seg.pt")  # segmentation model

# Train
model.train(
    data="dataset.yaml",
    epochs=15,
    imgsz=640,
    batch=8,
    project="yolov8-seg-results",
    name="fish_segmentation"
)
```

---

## 📊 Results

* **Epochs:** 15
* **Best Performance:**

  * Box mAP50: \~0.685
  * Box mAP50-95: \~0.553
  * Segmentation mAP50: \~0.685
  * Segmentation mAP50-95: \~0.511

Example training output:

```
Epoch [2/15]
Box mAP50: 0.685
Box mAP50-95: 0.553
Seg mAP50: 0.685
Seg mAP50-95: 0.511
```

---

## 📈 Inference

Run inference on test images:

```python
results = model.predict("test.jpg", save=True, imgsz=640, conf=0.5)
```

This will save predictions (with masks & labels) in `runs/segment/predict/`.

---

## 📝 Notes

* You can switch to larger YOLOv8 models (`yolov8m-seg.pt`, `yolov8l-seg.pt`) for higher accuracy.
* Training time and GPU requirements increase with larger models.

---

## 📜 License

This project is licensed under the **MIT License**.

