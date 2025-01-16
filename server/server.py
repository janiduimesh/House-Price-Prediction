from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        locations = util.get_location_names()  
        print("Locations fetched from util:", locations)  
        response = jsonify({'locations': locations})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error in get_location_names route:", e)  
        response = jsonify({'locations': [], 'error': str(e)})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


@app.route('/predict_home_price',methods=['POST','GET'])
def predict_home_price():
     total_sqft = float(request.form['total_sqft'])
     location = request.form['location']
     bhk = int(request.form['bhk'])
     bath = int(request.form['bath'])
     
     response = jsonify({
         'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
     })
     
     return response

if __name__ == '__main__':
    print("starting python flask server ")
    util.load_saved_artifacts()
    app.run()