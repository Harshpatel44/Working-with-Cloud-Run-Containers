from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login_submit():
    return render_template('index.html')

@app.route('/logout',methods=['POST'])
def logout_submit():
    return render_template('index.html')

@app.route('/loginStatus',methods=['POST'])
def logout_submit():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()