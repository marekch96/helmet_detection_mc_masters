from flask import Flask, render_template, redirect, request, send_file, url_for, Response
from werkzeug.utils import send_from_directory
from ultralytics import YOLO
import numpy as np
import os
import cv2
import io
from PIL import Image
import argparse




app=Flask(__name__)

@app.route('/')
def home():
    return render_template("new_index.html")


@app.route('/<path:filename>')
def display(filename):
    folder_path='runs/detect'
    subfolders=[f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path,f))]
    latest_subfolder=max(subfolders, key=lambda x: os.path.getctime(os.path.join(folder_path,x)))
    directory=folder_path+'/'+latest_subfolder
    
    files=os.listdir(directory)
    
    latest_file=files[0]
    print("latest file (dipslay)",latest_file)
    
    filename=os.path.join(folder_path,latest_subfolder,latest_file)
    file_extension=filename.rsplit('.',1)[1].lower()
    
    environ=request.environ
    if file_extension=='jpg':
        print('TEST IF JPG   ')
        return send_from_directory(directory,latest_file,environ)
    
    else:


        return "Invalid file format"

#method to process image and inference yolo 

#code source and support:https://github.com/robmarkcole/yolov5-flask/tree/master , https://www.youtube.com/watch?v=8SQcB2g_cp4&t=877s&ab_channel=CodeWithAarohi

@app.route('/',methods=["GET","POST"])
def predict():
    if request.method=="POST":  
        f=request.files["file"] #object passed by form from index.html
        path=os.path.dirname(__file__)
        file_path=os.path.join(path,'uploads',f.filename)
        print("images and videos will be saved in: ",file_path)
        f.save(file_path)
        
        global imgpath
        imgpath = f.filename  #assign file path to image path
        
        #file extension handling-> video must be divided into image frames 
        
        file_extension = f.filename.rsplit('.',1)[1].lower() # . is separator , lower cased
        
        if file_extension=="jpg":  # or file_extension=="jpeg"): handling jpg
            input_img=cv2.imread(file_path)
            #frame=cv2.imencode('.jpg',cv2.UMat(input_img))[1].tobytes()
            #print(frame)
            #image=Image.open(io.BytesIO(frame))
            
            ##detection
            
            yolo=YOLO("helmet_motorcycle_detection_best.pt")
            detections=yolo.predict(input_img,save=True)
            return display(f.filename)
            
        elif file_extension=="mp4":
            video_path=file_path
            cap=cv2.VideoCapture(video_path)
            
            #video dimensions and frame count
            frame_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            frame_count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            #video codec
            #fourcc = cv2.CV_FOURCC(*'mp4v') # doesn't work
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            output_video=cv2.VideoWriter('detections_output.mp4',fourcc,frame_count,(frame_width,frame_height))    
        
            #read video frames:
            
            model=YOLO("helmet_motorcycle_detection_best.pt")
            
            while cap.isOpened():
                ret,frame=cap.read()
                if not ret:
                    break
                results=model(frame,save=True)
                print(results)
                cv2.waitKey(1)
            
                res_plotted=results[0].plot()
                cv2.imshow("results",res_plotted)
                output_video.write(res_plotted)
                if cv2.waitKey(1)==ord('q'):
                    break 
        
        return video_feed()
            
    
def get_frame():
    folder_path=os.getcwd()
    mp4_files='detections_output.mp4'
    video=cv2.VideoCapture(mp4_files)
    while True:
        success,image=video.read()
        if not success:
            break
        ret,jpeg=cv2.imencode('.jpg',image)
        yield(b'--frame\r\n'
              b'Content-Type: image\jpeg\r\n\r\n' + jpeg.tobytes()+b'\r\n\r\n')
        time.sleep(0.1)  
             
@app.route('/video_feed')
def video_feed():
    print('video feed function called ')
    return Response(get_frame(),
                    mimetype='multipart/x mixed-replace boundary=frame')   
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov8 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    app.run()

#update