from flask import Flask, request
import json
import requests
app = Flask('bootcamp')
@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
  items = request.values['Body']

  url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=CvpvIrihyzoxCvbBpjSI992YwbXfUQMkDDLJtGhg'
  myobj = {'generalSearchInput': items}

  headers = {
     "Content-type": "application/json",
 }

  response = requests.post(url, headers=headers, data = json.dumps(myobj))

  output = json.loads(response.content)

  foods = output.get('foods')
  description=""
  ing = ""
  for i in foods:
     ing = i.get('ingredients')
     if ing:
        description = i.get('description')
        break
  return """<?xml version="1.0" encoding="UTF-8"?><Response><Message>"""+"The List of ingredients in the NAME- "+ str(description)  +": is "+str(ing)+"</Message></Response>"
app.run(debug=True, host='0.0.0.0', port=8080)