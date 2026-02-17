# Path to your video
VIDEO_PATH = "/home/abdul-rehman/Documents/vehicle_line_violation/Cars in Highway Traffic (FREE STOCK VIDEO).mp4"

# Minimum object size to consider (width, height)
MIN_OBJECT_SIZE = (30, 30)

# Line coordinates for counting (x1, y1), (x2, y2)
LINE_START = (100, 300)   # adjust based on your video
LINE_END = (500, 300)

# YOLO model for better detection
MODEL_NAME = "yolov8l.pt"  # large model for high-accuracy detection

# Detection confidence threshold
CONF_THRESHOLD = 0.25

# Frame skip for faster processing (1 = every frame)
FRAME_SKIP = 1
