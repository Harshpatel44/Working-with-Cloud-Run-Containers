from flask import Flask
from flask import render_template,redirect
from flask import request

from src.Service import Service

app = Flask(__name__)

@app.route('/')
def main_page():
    onlineUsers = Service().getOnlineUsersService()
    return render_template('index.html', onlineUsers = onlineUsers)


@app.route('/login',methods=['POST'])
def login_submit():
    userName=request.form['loginUsername']
    password=request.form['loginPassword']


    loginMessage=Service().loginService(userName,password)
    onlineUsers = Service().getOnlineUsersService()
    print(onlineUsers)
    if(loginMessage=="User created"):
        if (onlineUsers != []):
            onlineUsers.remove(userName)
            userActive=userName
    else:
        #onlineUsers=[]
        userActive=''

    return render_template('index.html', loginStatus=loginMessage, onlineUsers=onlineUsers, userActive=userActive)



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


@app.route('/logout',methods=['POST'])
def logout_submit():
    userToLogout=request.form['userNameActive']
    print(userToLogout)
    Service().logoutService(userToLogout)
    onlineUsers = Service().getOnlineUsersService()
    return render_template('index.html',onlineUsers = onlineUsers)



if __name__ == '__main__':
    app.run()