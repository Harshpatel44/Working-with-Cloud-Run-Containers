from flask import Flask
from flask import render_template,redirect
from flask import request

from Service import Service

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login_submit():
    userName=request.form['loginUsername']
    password=request.form['loginPassword']


    loginMessage=Service().loginService(userName,password)
    onlineUsers = Service().getOnlineUsersService()

    if(loginMessage=="User logged in"):
        if (onlineUsers != []):
            onlineUsers.remove(userName)
            userActive=userName
    else:
        userActive=''

    return render_template('index.html', loginStatus=loginMessage, onlineUsers=onlineUsers, userActive=userActive)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001)