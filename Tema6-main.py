from flask import Flask, render_template

app=Flask(__name__)

@app.route("/datos")
def datos():
    nombre="Angel"
    lista1=["uno","dos","tres","cuatro"]
    return render_template("datos.html",nombre=nombre,lista1=lista1)




if __name__=="__main__":
    app.run(debug=True,port=8080)