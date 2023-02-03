from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "!hola mundo!"

@app.route('/hola')
def hola():
    return "!hola IDGS-804"


if __name__=="__main__":
    app.run(debug=True,port=8080)