from flask import Flask, jsonify
app = Flask(__name__)
myData = [{'Customer':'Jostens Inc', 'Q1':200, 'Q2':230, 'Q3':300},
        {'Customer':'ADOLFO   RODRIGUEZ', 'Q1':120, 'Q2':320, 'Q3':200},
        {'Customer':'Wired Rhino, Inc.', 'Q1':400, 'Q2':150, 'Q3':90},
        {'Customer':'Spotify USA Inc', 'Q1':500, 'Q2':210, 'Q3':30}]

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"
@app.route('/data', methods=['GET'])
def getMyData():
    return jsonify({'myData':myData})

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
