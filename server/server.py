from flask import Flask, request, jsonify
import util
# server.py is main server file where imported flask module
# and created an app using line below
app = Flask(__name__)

# for locations create new file called util
# util will contain all the core routines where server will do the
# routing of requests and response

@app.route('/get_buildyear')
def get_buildyear():
    response = jsonify({
        'by': util.get_build_year()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_district')
def get_district():
    response = jsonify({
        'district': util.get_district_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_transtype')
def get_transtype():
    response = jsonify({
        'transtype': util.get_transaction_type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_zoning')
def get_zoning():
    response = jsonify({
        'zoning': util.get_zoning()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_floor')
def get_floor():
    response = jsonify({
        'floor': util.get_floor()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_buildingstate')
def get_buildingstate():
    response = jsonify({
        'buildingstate': util.get_buildingstate()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_buildingmat')
def get_buildingmat():
    response = jsonify({
        'materials': util.get_buildingmat()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_bsc')
def get_bsc():
    response = jsonify({
        'bsc': util.get_compyesno()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_manage')
def get_manage():
    response = jsonify({
        'manage': util.get_management()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# watch flask server tutorial, read on methods get and post
# lstasqm, floortotal, bsta, bsr, bsh, bsb, parksqm, mainba, ancba, balc, tlu, tbu, tpu,
# by, district, transtype, zoning, floor, buildingstate, materials, bsc, manage):
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    # whenever making http call from html app, will get all inputs
    # in request.form. Make sure to match float, int, str types
    lstasqm = float(request.form['lstasqm'])
    floortotal = int(request.form['floortotal'])
    bsta = float(request.form['bsta'])
    bsr = int(request.form['bsr'])
    bsh = int(request.form['bsh'])
    bsb = int(request.form['bsb'])
    parksqm = float(request.form['parksqm'])
    mainba = float(request.form['mainba'])
    ancba = float(request.form['ancba'])
    balc = float(request.form['balc'])
    tlu = int(request.form['tlu'])
    tbu = int(request.form['tbu'])
    tpu = int(request.form['tpu'])
    by = request.form['by']
    district = request.form['district']
    transtype = request.form['transtype']
    zoning = request.form['zoning']
    floor = request.form['floor']
    buildingstate = request.form['buildingstate']
    materials = request.form['materials']
    bsc = request.form['bsc']
    manage = request.form['manage']

    response = jsonify({
        'estimated_price': util.get_estimated_price(lstasqm, floortotal, bsta, bsr, bsh, bsb, parksqm, mainba, ancba, balc, tlu, tbu, tpu, by, district, transtype, zoning, floor, buildingstate, materials, bsc, manage)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


#main function just use app.run()
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price prediction...")
    util.load_saved_artifacts()
    app.run()