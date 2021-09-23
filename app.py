from flask import Flask, render_template, request, redirect, url_for

import os
import json
import time


app = Flask('app')

@app.route('/verify', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return "<h1>verify path works</h1>"
    if request.method == 'POST':
        return "POST hit"

@app.route('/generate, methods=['GET', 'POST'])
def generate):
    if request.method == 'GET':
        return "<h1>generate path works</h1>"
    if request.method == 'POST':
        return "POST hit"


if __name__ == '__main__':
    app.run(host='0.0.0.0')