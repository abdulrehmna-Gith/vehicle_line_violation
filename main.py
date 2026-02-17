from ultralytics import YOLO
import os

# -----------------------------
# Video Path
# -----------------------------
VIDEO_PATH = "/home/abdul-rehman/Documents/vehicle_line_violation/Cars in Highway Traffic (FREE STOCK VIDEO).mp4"

OUTPUT_DIR = "runs/detect"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Load YOLOv8 Model
# -----------------------------
model = YOLO("yolov8n.pt")  # small model for CPU, fast enough

# -----------------------------
# Video Detection Function
# -----------------------------
def detect_video():

    print("Starting video detection...")

    model.predict(
        source=VIDEO_PATH,
        show=True,   # Opens video window
        save=True,   # Saves output video
        device="gpu"
    )

    print("Detection completed! Output saved in 'runs/detect/'")


# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    detect_video()
