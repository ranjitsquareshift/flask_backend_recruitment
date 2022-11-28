from flask import Flask, request
from flask_cors import CORS
from data import *
from helperFunctions import *
app = Flask(__name__)
CORS(app,support_credentials=True)

@app.route('/health',methods = ["GET"])
def health_status():
    if(request.method == 'GET'):
        return 'Health Ok'
    else:
       return 'Oops! something went wrong' 

#api/v1/warehouse/distance?postal_code=465535
@app.route('/api/v1/warehouse/distance',methods = ["GET"])
def warehouse_distance():
    if(request.method == 'GET'):
        postal_code = int(request.args.get('postal_code'))
        print(request)
        result = searchPostalCode(postal_codes, postal_code);
        if (result == "error"): 
            return {'status': 400, 'response' : result , 'message': "Invalid postal code, valid ones are 465535 to 465545."}
        else:
            return {'status': 200, 'distance_in_kilometers' : result}
    else:
        return {'status':400, 'message':"Wrong Method"}

#/api/v1/product/1
@app.route('/api/v1/product/<id>',methods = ["GET"])
def get_Product(id):
    if(request.method == 'GET'):
        value = int(id)
        result = searchProduct(products,value);
        print (result)
        if (result == "error") :
            return {'status':400, 'message':"Invalid product id. Valid product id range is 100 to 110."}
        else:
            return {'status': 200, 'response': result} 
    else:
        return {'status':400, 'message':"Wrong Method"}

if __name__=="__main__":
    app.run(debug=True)