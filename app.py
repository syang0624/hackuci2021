from project import start_analysis
from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os
from flask import Flask, flash, request, redirect, url_for
UPLOAD_FOLDER = './userupload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav'}
app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)
@app.route('/music/<path:path>')
def send_js(path):
    return send_from_directory('music', path)
    
@app.route('/')
def index():
    return "Welcome"

@app.route('/voice-analysis', methods=['POST'])
def voice_analysis():
    userfile = request.files['file']
    print(userfile)
    userfile.save(os.path.join(app.config['UPLOAD_FOLDER'], 'user' + userfile.filename))
    result = start_analysis('./userupload/user' + userfile.filename)
    return result



