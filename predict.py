from ultralytics import YOLO
import cv2

class LICENSEPLATE_DETECTION :
    def __init__(self,model_path):
        self.model = YOLO(model_path)
        
    def __call__(self,input_image, output_path):
        img = cv2.imread(input_image)
        results = self.model(input_image)[0]
        for i in range(len(results.boxes.data)):
            boxes = results.boxes.data[i].numpy().tolist()
            cv2.rectangle(img,(int(boxes[0]),int(boxes[1])),(int(boxes[2]),int(boxes[3])),[0,255,0],2)
            cv2.putText(img,
                        f'{results.names[int(boxes[5])]}:{int(boxes[4]*100)}%', 
                        (int(boxes[0]), int(boxes[1] - 2)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, 
                        [225, 0, 0],
                        thickness=2)
        cv2.imwrite(output_path, img)