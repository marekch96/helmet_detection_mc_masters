from flask import Flask, render_template, redirect, request
from ultralytics import YOLO

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('/templates/index.html')

if __name__ == "__main__":
    app.run()



