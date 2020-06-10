from flask import Flask
from flask import render_template,redirect
from flask import request

from Service import Service

app = Flask(__name__)

# @app.route('/')
# def main_page():
#     onlineUsers = Service().getOnlineUsersService()
#     return render_template('index.html', onlineUsers = onlineUsers)


@app.route('/register',methods=['POST'])
def register_submit():
    registerUserName = request.form['registerUserName']
    registerEmail = request.form['registerEmail']
    registerPassword = request.form['registerPassword']
    registerTopic = request.form['registerTopic']

    onlineUsers = Service().getOnlineUsersService()

    if(registerUserName=='' or registerEmail=='' or registerPassword=='' or registerTopic==''):
        registerMessage="Please Enter all fields"
        return render_template('index.html', registrationStatus=registerMessage, onlineUsers=onlineUsers)

    if(Service().registerService(registerUserName,registerEmail,registerPassword,registerTopic)):
        registerMessage="Registration successfull"

    else:
        registerMessage="Registration unsucessfull"

    return render_template('index.html', registrationStatus=registerMessage,onlineUsers = onlineUsers)



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)