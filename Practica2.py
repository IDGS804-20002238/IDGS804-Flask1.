from flask import Flask, render_template
from flask import request
import math


app=Flask(__name__)

@app.route("/distancia")
def distancia():
    return render_template("distancia.html")

@app.route("/resDistancia", methods=["post"])
def resDistancia():
    x1 = int(request.form.get("txtX1"))
    x2 = int(request.form.get("txtX2"))
    y1 = int(request.form.get("txtY1"))
    y2 = int(request.form.get("txtY2"))
    res = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))   
    return render_template("resDistancia.html", x1=x1, x2=x2, y1=y1, y2=y2, res=res)




if __name__=="__main__":
    app.run(debug=True,port=8080)