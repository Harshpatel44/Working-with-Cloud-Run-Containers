from flask import Flask
from flask import render_template
from flask import request

from Injector import Injector

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login_submit():
    userName=request.form['loginUsername']
    password=request.form['loginPassword']
    Injector.instance(Injector()).getService().loginService(userName,password)
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register_submit():

    return redirect()
@app.route('/logout',methods=['POST'])
def logout_submit():
    return render_template('index.html')

@app.route('/loginStatus',methods=['POST'])
def login_status():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()