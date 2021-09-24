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
# APP_HASH = "ayush123"
APP_HASH = "abcdefgh"

current_ref_num = "213561321321613"
current_otp = "123564"
verify_url = "https://api.dialog.lk/subscription/otp/verify"
generate_url = "https://api.dialog.lk/subscription/otp/request"

generate_params = {
    "applicationId": APP_ID,
    "password": PASSWORD,
    "subscriberId": DEFAULT_SUBSCRIBER_ID,
    "applicationHash": APP_HASH,
    "applicationMetaData": {
    "client": "MOBILEAPP",
    "device": "Samsung S10",
    "os": "android 8",
    "appCode": "https://play.google.com/store/apps/details?id=lk.dialog.megarunlor"
  }
}

verify_params = {
    "applicationId": APP_ID,
    "password": PASSWORD,
    "referenceNo": current_ref_num,
    "otp": current_otp
}

headers_dict = {
    'Content-Type': 'application/json',
}

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'GET':
        return "<h1>Generate path works</h1>"
    elif request.method == 'POST':
        try:
            return json.dumps({"code":200, "status": "good"})
            tel_str = request.args.get("tel")
            gen_params = generate_params
            gen_params["subscriberId"] = tel_str
            print("\n"+tel_str+"\n")
            response = requests.post(generate_url, headers=headers_dict, data=json.dumps(gen_params))
            print(response.content)
            # return(response.json)
            response_content  = json.loads(response.text)
            # print(response_content)
            current_ref_num = response_content["referenceNo"]
            verify_params["referenceNo"] = current_ref_num
            print(current_ref_num)
            # return json.dumps({"code":200, "status": "good", "referenceNo":current_ref_num })
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
            return json.dumps({"code":200, "status": "valid"})
            otp = request.args.get("otp")
            if otp == None:
                raise Exception("OTP not provided")
            verify_p = verify_params
            verify_p["otp"] = otp
            print("otp is", otp)
            return json.dumps({"code":200, "status": "valid"})
            # verify_p["referenceNo"] = current_ref_num
            response = requests.post(verify_url, headers=headers_dict, data=json.dumps(verify_p))
            response_content  = json.loads(response.text)
            print(response_content)
            print("valid")
            success = response_content["statusDetail"]
            # print(success)
            # # return status
            return json.dumps({"code":200, "status": success})
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