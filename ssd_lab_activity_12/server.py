from flask import Flask,render_template, session, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, login_manager, login_user, logout_user, login_required ,UserMixin)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db13.db'
app.config['SECRET_KEY'] = 'shukanS'
db = SQLAlchemy(app)

login_manager = LoginManager()

class user(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    password = db.Column(db.String(200)) 

    def __init__(self, name1, email1, password1):
        self.name = name1
        self.email = email1
        self.password = password1

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def hello_world():
    return "Hello"

@app.route('/user/signup',methods = ['POST', 'GET'])
def sign_up_new():
    if request.method == 'POST':
        response = request.get_json()
        if not response['email'] or not response['password'] or not response['name']:
            return jsonify({ "msg" : "Insufficient Data"}),500
        else:
            user1 = user(response['email'],response['password'],response['name'])

            db.session.add(user1)
            db.session.commit()
         
            return jsonify({ "msg" : 'SUCCESS'}),200
    return jsonify({ "msg" : "Something Wrong"}),500

@app.route('/user/signin',methods = ['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        responase = request.get_json()
        if not responase['email'] or not responase['password']:
            ans1 = "Not all data given"
            return jsonify({ "msg" : ans1}),500
        else:
            answer = user.query.filter_by(email = responase['email']).first()
            db.commit()
            if len(answer) == 0:
                return jsonify({ "msg" : "User Not Signed Up.."}),500
            else :
                if request.get_json["password"] == answer.password :
                    return jsonify({ "msg" : "User Sucessfully Signed In."}),200
                else:
                    return jsonify({ "msg" : "Password not matching"}),500
        
    return jsonify({ "msg" : "Something went wrong"}),500   

@app.route('/user/signout',methods = ['POST', 'GET'])
def sign_out():
    if request.method == 'GET':
        return jsonify({ "msg" : "ans1"}),500
        
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug = True)