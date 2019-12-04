from flask import Flask, request
import json
import requests
#  incoming use import request
#  outgoing use import requests

app = Flask('bootcamp')

@app.route('/ingredients', methods=['GET', 'POST'])
def weather():

  city = request.values['Body']

  response = requests.get('https://jobs.github.com/positions.json', 
  params={
        'description': 'python',
        'location': city
    })

  data = json.loads(response.content)

  temp = data[ 0]
  company =temp["company"]
  title = temp["title"]


  return """<?xml version="1.0" encoding="UTF-8"?
  ><Response><Message>"""+"the company is "+ str(company)+ "and title is" + str(title) + "</Message></Response>" ""



app.run(debug=True, host='0.0.0.0', port=8080)
