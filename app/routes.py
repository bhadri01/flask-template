from flask import Blueprint, current_app, jsonify,request
from .lib.mailservice import MailSender

# Create blueprint for authentication routes
auth_routes = Blueprint('auth', __name__, url_prefix='/auth')

@auth_routes.post('/signin')
def signin():
    # Implement signin logic here
    return jsonify({"message":"signin","method":request.method})

@auth_routes.route('/signup')
def signup():
    # Implement signup logic here
    return jsonify({"message":"signup"})

@auth_routes.route('/signout')
def signout():
    # Implement signout logic here
    return jsonify({"message":"signout"})



# Create blueprint for main routes
main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    # Access the MongoDB instance using the Flask app's context
    db = current_app.config['MONGO']

    # Access a collection and perform operations
    collection = db.users
    data = collection.find_one()
    print(data)
    return jsonify({"message":"root"})

@main_routes.route('/send_email')
def send_email():
    # Access the Mail instance using the Flask app's context
    mail = current_app.config['MAIL']
    to = "bhadri2002@gmail.com"
    body = "this is test email"
    message = "hellow world"

    MailSender(mail,to,body,message)
   

    return jsonify({"message":"Email sent"})
