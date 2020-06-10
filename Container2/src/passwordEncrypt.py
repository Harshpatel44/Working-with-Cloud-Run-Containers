
class Passwd:
    def __init__(self):
        pass

    def encrypt(self,text):
        str=''
        for i in text:
            str+=chr(ord(i)+10)
        return str

    def decrypt(self,text):
        str=''
        for i in text:
            str+=chr(ord(i)-10)
        return str
