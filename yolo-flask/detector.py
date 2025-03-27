import cv2
import torch
from ultralytics import YOLO

# Check if CUDA is available, otherwise use CPU
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the trained YOLOv8 model
model = YOLO("C:/NaqibWorks/project/Yolo/runs/detect/train/weights/best.pt")
model.to(device)  # Send model to appropriate device

# Initialize video capture (0 = default webcam)
cap = cv2.VideoCapture(0)

# Define class labels and colors
class_names = ["with_mask", "mask_weared_incorrect", "without_mask"]
colors = [(0, 255, 0), (0, 165, 255), (0, 0, 255)]  # Green, Yellow-Orange, Red

def detect():
    """ Generator function to stream frames with YOLO detection """
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Perform object detection
        results = model(frame)

        # Visualize results on the frame
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                conf = box.conf[0]  # Confidence score
                cls = int(box.cls[0])  # Class label

                label = f"{class_names[cls]}: {conf:.2f}"
                color = colors[cls]  # Get color based on class

                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

                # Label box
                (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
                label_x2 = x1 + w + 10
                label_y2 = y1 - h - 5 if y1 - h - 5 > 10 else y1 + h + 5

                cv2.rectangle(frame, (x1, y1 - h - 10), (label_x2, y1), color, -1)  # Label background
                cv2.putText(frame, label, (x1 + 5, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Convert frame to JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield frame for Flask response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def release_camera():
    """ Release camera resources """
    cap.release()
    cv2.destroyAllWindows()
