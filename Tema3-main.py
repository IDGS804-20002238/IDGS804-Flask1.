from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "!hola mundo!"

#pasamos un STRING
@app.route('/user/<string:user>')
def user(user):
    return "hola "+ user

#pasamos parametros INT
@app.route('/numero/<int:n>')
def numero(n):
    return "Numero {}".format(n)

#pasamos mas de un parametro 
@app.route('/user/<int:id>/<string:username>')
def usern(id, username):
    return "ID {} nombre:{}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "la suma es: {}".format(n1+n2)




if __name__=="__main__":
    app.run(debug=True,port=8080)