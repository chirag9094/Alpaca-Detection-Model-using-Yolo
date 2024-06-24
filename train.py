from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt')
    results = model.train(data='config.yaml', imgsz=640, epochs=15, batch=1, name='yolov8n_v8_50e67')

if __name__ == '__main__':
    main()
