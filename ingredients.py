from flask import Flask, request
import json
import requests
#  incoming use import request
#  outgoing use import requests
app = Flask('bootcamp')
@app.route('/ingredients', methods=['GET', 'POST'])
def weather():
  city = request.values['Body']

url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=CvpvIrihyzoxCvbBpjSI992YwbXfUQMkDDLJtGhg'
myobj = {'generalSearchInput': 'items'}

response= requests.post(url, data = myobj)
output = json.loads(response.content)


  




 #5 return """<?xml version="1.0" encoding="UTF-8"?><Response><Message>"""+"the weather in "+ city  +" is "+str(temp)+ " deg C"+"</Message></Response>"""
app.run(debug=True, host='0.0.0.0', port=8080)