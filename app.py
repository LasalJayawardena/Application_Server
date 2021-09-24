from flask import Flask, render_template, request, redirect, url_for
import requests
import os
import json
import time


app = Flask('app')

# Application ID: 
# Password: 4cce7809bbf5609ae54e3d726ebc4833

APP_ID = "APP_062044"
PASSWORD = "4cce7809bbf5609ae54e3d726ebc4833"
DEFAULT_SUBSCRIBER_ID= "tel:94766679727"
APP_HASH = "ayush123"
# APP_HASH = "abcdefgh"

current_ref_num = "213561321321613"
current_otp = "123564"
verify_url = "https://api.hSenidMobile.lk/otp/verify"
generate_url = "https://api.hSenidMobile.lk/otp/request"

generate_params = {
    "applicationId": APP_ID,
    "password": PASSWORD,
    "subscriberId": DEFAULT_SUBSCRIBER_ID,
    "applicationHash": APP_HASH,
}

verify_params = {
    "applicationId": APP_ID,
    "password": PASSWORD,
    "referenceNo": current_ref_num,
    "otp": current_otp
}

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'GET':
        return "<h1>Generate path works</h1>"
    elif request.method == 'POST':
        try:
            tel_str = request.args.get("tel")
            gen_params = generate_params
            gen_params["subscriberId"] = tel_str
            print(gen_params)
            response = requests.post(generate_url, params=gen_params)
            response_content  = dict(response.content)
            current_ref_num = response_content["referenceNo"]
            print(current_ref_num)
            return json.dumps({"code":200, "status": "good"})
        except Exception as e:
            print(e)
            return json.dumps({"code":400, "status": "error", "error": str(e)})
        return "POST hit"
    else:
        return "Unknown Request type."

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'GET':
        return "<h1>Verify path works</h1>"
    elif request.method == 'POST':
        try:
            otp = request.args.get("otp")
            verify_params = verify_params
            verify_params["otp"] = otp
            response = requests.post(generate_url, params=verify_params)
            response_content  = dict(response.content)
            success = response_content["subscriptionStatus"]
            print(success)
            # return status
            return json.dumps({"code":200, "status": success,})
        except Exception as e:
            print(e)
            return json.dumps({"code":400, "status": "error", "error": str(e)})
    else:
        "Unknown Request type."

@app.route('/test', methods=['GET', 'POST'])
def test():
    return json.dumps({"status": 200, "msg":"success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run()