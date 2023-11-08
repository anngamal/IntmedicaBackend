# from flask import Flask, make_response,jsonify, request, session
# import os
# from flask_migrate import Migrate
# from model import *
# # import pandas
# # import sqlite3
from flask_cors import CORS
from flask import Flask, make_response, jsonify, request, session
from flask_migrate import Migrate
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# Get Relative Imports with Updated System Traversal
from model import *

app=Flask(__name__)
CORS(app)

cart = {}
bcrypt = Bcrypt(app)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY')


migrate = Migrate(app, db)
db.init_app(app)

excluded_endpoints = ['login', 'signup', 'check_session', 'root', 'therafaceProducts', 'theragunProducts','WaveSeries','powerdotProducts','tables','recoveryairProducts','hotandcold','clinicsupplies', 'electrodes', 'lightforceTherapy', 'mobility', 'shockwaveAndRPW', 'vitalstimTherapy', 'smartgogglesProducts','portableElectrotherapy','electrotherapy']

@app.before_request
def check_logged_in():
    if request.endpoint not in excluded_endpoints:
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        
        if not user:
            return {'message': 'invalid session'}, 401
        else: 
            return{'message' :' valid session'}, 200

        

@app.route('/')
def root():
    return make_response(jsonify({}), 200)


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print(data)
    new_user = User(username=data['email'], firstName=data['firstName'], lastName=data['lastName'], phoneNumber=data['phoneNumber'])
    new_user.password = data['password']
    print(new_user) 
    db.session.add(new_user)
    db.session.commit()

    return {'message': 'user added'}, 201



@app.route('/login', methods=['POST', 'GET'])
def login():
    data = request.get_json()

    user = User.query.filter(User.username == data['username']).first()

    if not user:
        return {'message': 'user not found'}, 404
    
    if user.authenticate(data['password']):
       
        session['user_id'] = user.id
        return {'message': 'login success'}, 201
    else:
        return {'message': 'login failed'}, 401



@app.route('/check_session')
def check_session():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()

    if not user:
       
        return {'message': 'invalid session'}, 401
    
    return {'message': 'valid session'}, 200

@app.route('/logout', methods=['DELETE'])
def logout():
    
    session.pop('user_id', None)
    return {'message': 'logged out'}, 200

# @app.route('/add_to_cart', methods=['POST'])
# def add_to_cart():
#     data = request.get_json()
#     cart.append(data)
#     return jsonify({"message": "Item added to cart"})

# cart = []

# @app.route('/yourcart', methods=['GET'])
# def get_cart():
#     return jsonify(cart)

# @app.route('/yourcart', methods=['POST'])
# def add_to_cart():
#     data = request.json
#     cart.append(data)
#     return jsonify(cart)

# @app.route('/yourcart<int:index>', methods=['DELETE'])
# def remove_from_cart(index):
#     if index < len(cart):
#         del cart[index]
#     return jsonify(cart)


# // app routing for cart 
# add route (post)
# add get  route by user id to get the info of the cart about the user  which 

@app.route('/products/category=Recoveryair', methods=['GET'])
def recoveryairProducts():
    recoveryairProducts= Recoveryair.query.all()
    body=[recoveryair.to_dict() for recoveryair in recoveryairProducts ]
    return jsonify(body), 200





@app.route('/products/category=Powerdot', methods=['GET'])
def powerdotProducts():
    if request.method == 'GET':
        powerdotProducts= Powerdot.query.all()
        body=[powerdot.to_dict() for powerdot in powerdotProducts]
        return jsonify(body), 200



@app.route('/products/category=RecoveryTherm', methods=['GET'])
def recoverythermProducts():
    recoverythermProducts= Recoverytherm.query.all()
    body=[recoverytherm.to_dict() for recoverytherm in recoverythermProducts]
    return(body), 200



# @app.route('/theracupProducts', methods=['GET'])
# def theracupProducts():
#     theracupProducts= Theracup.query.all()
#     body=[theracup.to_dict() for theracup in theracupProducts]
#     return(body) ,200


@app.route('/products/category=Theraface', methods=['GET'])
def therafaceProducts():
    if request.method == 'GET':
        therafaceProducts = Theraface.query.all()
        body=[theraface.to_dict() for theraface in therafaceProducts]
        return jsonify(body), 200



@app.route('/products/category=Theragun', methods=['GET'])
def theragunProducts():
    if request.method == 'GET':
        theragunProducts = Theragun.query.all()
        body=[theragun.to_dict() for theragun in theragunProducts]
        return jsonify(body), 200


@app.route('/products/category=WaveSeries', methods=['GET'])
def WaveSeries():
     if request.method == 'GET':
        waveseriesProducts = Waveseries.query.all()
        body=[waveseries.to_dict() for waveseries in waveseriesProducts]
        return(body), 200

@app.route('/products/category=Electrotherapy', methods=['GET'])
def electrotherapy():
    electrotherapy = ELectrotherapy.query.all()
    body=[electrotherapy.to_dict() for electrotherapy in electrotherapy]
    return(body), 200

@app.route('/products/category=Smartgoggles', methods=['GET'])
def smartgogglesProducts():
    smartgogglesProducts = Smartgoggles.query.all()
    body=[smartgoggles.to_dict() for smartgoggles in smartgogglesProducts]
    return(body), 200

@app.route('/products/category=PortableElectrotherapy', methods=['GET'])
def portableElectrotherapy():
    portableElectrotherapy = PortableElectrotherapy.query.all()
    body=[portableElectrotherapy.to_dict() for portableElectrotherapy in portableElectrotherapy]
    return(body), 200

@app.route('/products/category=ClinicSupplies', methods=['GET'])
def clinicsupplies():
    clinicsupplies = Clinicsupplies.query.all()
    body=[clinicsupplies.to_dict() for clinicsupplies in clinicsupplies]
    return(body), 200

@app.route('/products/category=Electrodes', methods=['GET'])
def electrodes():
    electrodes = Electrodes.query.all()
    body=[electrodes.to_dict() for electrodes in electrodes]
    return(body), 200


@app.route('/products/category=hotandcold', methods=['GET'])
def hotandcold():
    hotandcold = HotandCold.query.all()
    body=[hotandcold.to_dict() for hotandcold in hotandcold]
    return(body), 200

@app.route('/products/category=lightforceTherapy', methods=['GET'])
def lightforceTherapy():
    lightforceTherapy= LightforceTherapy.query.all()
    body=[lightforceTherapy.to_dict() for lightforceTherapy in lightforceTherapy]
    return(body), 200

@app.route('/products/category=Mobility', methods=['GET'])
def mobility():
    if request.method == 'GET':
        mobility = Mobility.query.all()
        body=[mobility.to_dict() for mobility in mobility]
        return(body), 200

@app.route('/products/category=Tables', methods=['GET'])
def tables():
    tables = Tables.query.all()
    body=[tables.to_dict() for tables in tables]
    return(body), 200

@app.route('/products/category=ShockwaveAndRPW', methods=['GET'])
def shockwaveAndRPW():
    shockwaveAndRPW = Shockwave.query.all()
    body=[shockwaveAndRPW.to_dict() for shockwaveAndRPW in shockwaveAndRPW]
    return(body), 200

@app.route('/products/category=VitalstimTherapy', methods=['GET'])
def vitalstimTherapy():
    vitalstimTherapy = VitalstimTherapy.query.all()
    body=[vitalstimTherapy.to_dict() for vitalstimTherapy in vitalstimTherapy]
    return(body), 200



# @app.route("/categoriesList", method=["GET"])
# def CatList():
    # filter each cat by its name to be == to Linkname 
    



if __name__ == '__main__':
    app.run(debug=True , port=5555)