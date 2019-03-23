from flask import Flask,request, jsonify
import requests

app = Flask(__name__)

"""@app.route('/',methods=['GET','POST'])
def index():
    d = request.json
    #print(d)
    return 'Bot replies' + d["text"]  """

@app.route('/webhook',methods=['POST','GET'])
def webhook():
    d=request.json
    intent =d['queryResult']['intent']['displayName']
    if intent == 'numbers':
        typ = d['queryResult']['parameters']['type']
        num = d['queryResult']['parameters']['number-integer']
        print(intent,typ,num)
        num = int(num)
        url = 'http://numbersapi.com/'+str(num)+'/'+typ+'?json'
        r = requests.get(url)
        print(r.text)
        data = r.json()
        replytext = data['text']
        print(replytext)
        response = {
            'fulfillmentMessages' : [
                {
                    'text':{
                        'text':[replytext]
                    }
                }
            ]
        }
        return jsonify(response)
    pass

if __name__ == '__main__':
    app.run(debug=True)