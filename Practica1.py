from flask import Flask
from flask import request


app=Flask(__name__)



@app.route('/calculadora', methods=["GET","POST"])
def calculadora():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        operacion = request.form.get("operacion")
        
        if operacion == "suma":
            resultado = int(num1) + int(num2)
        elif operacion == "resta":
            resultado = int(num1) - int(num2)
        elif operacion == "multiplicacion":
            resultado = int(num1) * int(num2)
        elif operacion == "division":
            if int(num2) != 0:
                resultado = int(num1) / int(num2)
            else:
                return "<h1>No se puede dividir por cero</h1>"
        else:
            return "<h1>Operación no válida</h1>"
        
        return "<h1>El resultado es: {}</h1>".format(resultado)
    else:
        return'''
            <form action="/calculadora" method="POST">
            <label>N1:</label>
            <input type="text" name="num1"/></br></br>
            <label>N2:</label>
            <input type="text" name="num2"/></br></br>
            <input type="radio" name="operacion" value="suma"> Suma <br>
            <input type="radio" name="operacion" value="resta"> Resta <br>
            <input type="radio" name="operacion" value="multiplicacion"> Multiplicación <br>
            <input type="radio" name="operacion" value="division"> División <br>
            <input type="submit" value="Calcular"/>
            </form>
            '''

    
if __name__=="__main__":
    app.run(debug=True,port=8080)