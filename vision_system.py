import cv2
import torch

# Load YOLOv5 model (auto-downloads first time)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access camera")
    exit()

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Run object detection
    results = model(frame)

    # Convert results to pandas dataframe
    detections = results.pandas().xyxy[0]

    # Draw bounding boxes
    for index, row in detections.iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        label = row['name']
        confidence = row['confidence']

        # Draw rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Put label
        text = f"{label} {confidence:.2f}"
        cv2.putText(frame, text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)

    # Show output
    cv2.imshow("Vision System - Object Detection", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()