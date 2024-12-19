#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from base64 import b64encode
import os
import hashlib
import subprocess

app = Flask(__name__)

@app.route("/")
def show_gallery():
    return render_template("index.html")
    
@app.route("/file")
def view_image():
    image = request.args.get('name', '')
    if image == '':
        return "No image?"
    else:
        try:
            with open(f'/app/uploads/{image}', 'rb') as f:
                return render_template("view.html", url=f"data:image/jpeg;base64, {b64encode(f.read()).decode()}")
        except FileNotFoundError:
                return render_template("view.html", url="https://placehold.co/800x800")

if __name__ == '__main__':
    app.run('0.0.0.0', 1337)
