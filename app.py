from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import warnings

# Suppress torch FutureWarnings
warnings.filterwarnings("ignore", category=FutureWarning)

app = Flask(__name__)

# Load YOLOv8 model (replace with your best.pt path)
model = YOLO("best.pt")

# Path to your video
VIDEO_PATH = "This_the_fish_202507231344_tvan4.mp4"

def generate_frames():
    camera = cv2.VideoCapture(VIDEO_PATH)

    if not camera.isOpened():
        raise RuntimeError(f"Could not open video file: {VIDEO_PATH}")

    while True:
        success, frame = camera.read()

        if not success:
            # Loop back to start if video ends
            camera.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Run YOLOv8 detection
        results = model(frame, stream=True)

        for r in results:
            annotated_frame = r.plot()

        # Resize for faster streaming
        annotated_frame = cv2.resize(annotated_frame, (640, 360))

        # Encode to JPEG
        ret, buffer = cv2.imencode(".jpg", annotated_frame)
        if not ret:
            continue

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False, host="0.0.0.0", port=5000)
