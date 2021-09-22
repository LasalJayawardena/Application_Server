from flask import Flask, render_template, request, redirect, url_for

import os
import json
import time


app = Flask('app')

@app.route('/test', methods=['GET', 'POST'])
def test():
    return "yeah"


@app.route('/res', methods=['GET', 'POST'])
def res():
    # if request.method == 'POST':
    #     pass
    return "yo"

if __name__ == '__main__':
    app.run()