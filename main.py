from flask import Flask, render_template, redirect, request
from ultralytics import YOLO

app=Flask(__name__)

@app.route('/')
def home():
    return f('test')

if __name__ == "__main__":
    app.run()



