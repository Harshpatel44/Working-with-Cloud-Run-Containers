from flask import Flask
from flask import render_template,redirect
from flask import request

from Service import Service

app = Flask(__name__)


@app.route('/logout',methods=['POST'])
def logout_submit():
    userToLogout=request.form['userNameActive']
    Service().logoutService(userToLogout)
    onlineUsers = Service().getOnlineUsersService()
    return render_template('index.html',onlineUsers = onlineUsers)



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)