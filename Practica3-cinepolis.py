from flask import Flask, request, render_template

app = Flask(__name__)

class CompraBoleteria:
    def __init__(self, nombre, cantidad, paga_tarjeta, compradores):
        self.nombre = nombre
        self.cantidad = cantidad
        self.paga_tarjeta = paga_tarjeta
        self.compradores = compradores
        
    def calcular_precio(self):
        valor = self.cantidad * 12
        error="No se pudo procesar la compra la cantidad de boletas por persona debe ser menor a 7"
        if self.cantidad  > self.compradores*7:
            return error
        if self.cantidad > 5:
            valor = valor * 0.85
        elif self.cantidad >= 3:
            valor = valor * 0.9
        
        if self.paga_tarjeta:
            valor = valor * 0.9
        
        return valor

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        compradores = int(request.form['compradores'])
        paga_tarjeta = 'paga_tarjeta' in request.form
        
        compra = CompraBoleteria(nombre, cantidad, paga_tarjeta,compradores)
        precio = compra.calcular_precio()
        
        return render_template('resultado.html', nombre=nombre, cantidad=cantidad, precio=precio, compradores=compradores)
    
    return render_template('formulario.html')

if __name__=="__main__":
    app.run(debug=True,port=8080)
