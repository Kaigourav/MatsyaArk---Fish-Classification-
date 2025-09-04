```markdown
# 🐟 MatsyaArk – Fish Classification (YOLOv8)

MatsyaArk is an AI-powered fish classification system built using **YOLOv8**.  
It can detect and classify different fish species in real-time from videos or images, supporting **aquaculture, biodiversity monitoring, and sustainable fisheries**.

---

## 📂 Project Structure
```

├── app.py                # Flask app for running inference
├── requirements.txt      # Python dependencies
├── best.pt               # Trained YOLOv8 weights (best model)
├── last.pt               # Last checkpoint from training
├── templates/            # HTML templates for web interface
├── Output/               # (optional) Inference outputs
├── videoplayback.mp4     # Sample demo video
└── This\_the\_fish\_\*.mp4   # Additional test video

````

---

## ⚡ Features
- Real-time fish detection & classification.
- Built with **YOLOv8** for high accuracy and speed.
- Web-based interface powered by **Flask**.
- Supports video uploads for inference.
- Trained custom weights (`best.pt`, `last.pt`).

---

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kaigourav/MatsyaArk---Fish-Classification-.git
   cd MatsyaArk---Fish-Classification-
````

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### Run the Flask App

```bash
python app.py
```

This will start a local server (default: `http://127.0.0.1:5000/`).

### Inference with YOLOv8

If you want to test the trained model directly:

```bash
yolo task=detect mode=predict model=best.pt source=videoplayback.mp4
```

---

## 📊 Results

* The model achieves accurate fish detection on sample videos.
* Demo videos (`videoplayback.mp4`, `This_the_fish_*.mp4`) are included in the repo.
* Trained weights (`best.pt`) are optimized for classification.

---

## 🛠️ Tech Stack

* **Python**
* **YOLOv8 (Ultralytics)**
* **Flask**
* **OpenCV**

---

## 🌍 Applications

* Smart aquaculture monitoring
* Automated biodiversity surveys
* Sustainable fisheries management
* Marine research

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---

## 📜 License

This project is licensed under the MIT License – feel free to use and adapt.

---

## 👨‍💻 Author

**Kaigourav** – Developer of MatsyaArk (Fish Classification using YOLOv8).

```


https://github.com/user-attachments/assets/e9e982ff-2fc2-4c82-8dd3-c2165408be27



