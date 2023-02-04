from flask import Flask, request, render_template

app = Flask(__name__)

class CompraDeBoletos:
    def __init__(self, num_boletos, nombre, usando_cineco):
        self.num_boletos = num_boletos
        self.nombre = nombre
        self.usando_cineco = usando_cineco

    def calcular_descuento(self):
        precio_base = 12
        total = precio_base * self.num_boletos

        if self.num_boletos > 5:
            descuento = total * 0.15
        elif self.num_boletos >= 3 and self.num_boletos <= 5:
            descuento = total * 0.10
        else:
            descuento = 0

        if self.usando_cineco:
            descuento += total * 0.10

        return total - descuento

@app.route("/", methods=["GET", "POST"])
def comprar_boletos():
    if request.method == "POST":
        num_boletos = int(request.form["num_boletos"])
        nombre = request.form["nombre"]
        usando_cineco = request.form.get("usando_cineco") is not None
        num_compradores = int(request.form["num_compradores"])

        if num_boletos * num_compradores > 7 * num_compradores:
            mensaje_error = "No se puede comprar más de 7 boletos por persona."
            return render_template("comprar_boletos.html", mensaje_error=mensaje_error)

        compra = CompraDeBoletos(num_boletos, nombre, usando_cineco)
        total = compra.calcular_descuento()

        return render_template("resultado.html", nombre=nombre, total=total)

    return render_template("formulario.html")

if __name__ == "__main__":
    app.run()
