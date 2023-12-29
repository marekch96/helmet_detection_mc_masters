
# Motorcycle and helmet detection end-user website
An end-user website runs trained by the author YOLOv8 model to detecttwo types of objects: motorcycles and helmets.
There are two types of files allowed:
- images in ".jpg" format
- videos in ".mp4" format
  
![Website head](_website_head.png)
To run the web application follow these four steps: 
1. Clone repo
2. Download requirements file
```
python3 -m pip install -r .\requirements.txt
```
3. Run the web application
```
python3 .\webapp.py --port 5000 
```
4. Click and follow the link to 127.0.0.1:5000 to load website
# Example prediction
![example_prediction](example_detection.jpg)
# Configuration


# Performance 
| Class       |  mAP@0.5 | 
| :---        | :---:    |    
| Motorcycle  | 0.842    |
| Helmet      | 0.742    | 
| Combined    | 0.792    |

