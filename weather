from flask import Flask, request
import json
import requests
#  incoming use import request
#  outgoing use import requests
app = Flask('bootcamp')
@app.route('/weather', methods=['GET', 'POST'])
def weather():
  city = request.values['Body']
  response = requests.get('http://api.openweathermap.org/data/2.5/weather',
  params={
        'appid': '972498aee47cf8cee7487e742cd1bc15',
        'q': city
    })
  data = json.loads(response.content)
  temp = data["main"]["temp"] - 273.15
  return """<?xml version="1.0" encoding="UTF-8"?><Response><Message>"""+"the weather in "+ city  +" is "+str(temp)+ " deg C"+"</Message></Response>"""
app.run(debug=True, host='0.0.0.0', port=8080)