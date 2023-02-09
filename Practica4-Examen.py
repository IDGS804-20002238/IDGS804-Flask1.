from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def examen():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apaterno = request.form["apaterno"]
        amaterno = request.form["amaterno"]
        dia = int(request.form["dia"])
        mes = int(request.form["mes"])
        anio = int(request.form["anio"])
        sexo = request.form["sexo"]
        pregunta1 = request.form["pregunta1"]
        pregunta2 = request.form["pregunta2"]
        pregunta3 = request.form["pregunta3"]
        pregunta4 = request.form["pregunta4"]
        pregunta5 = request.form["pregunta5"]

        fecha_nacimiento = datetime.datetime(anio, mes, dia)
        hoy = datetime.datetime.now()
        edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        url=''
        dragon = [1940, 1952, 1964, 1976, 1988, 2000, 2012]
        rata = [1936, 1948, 1960, 1972, 1984, 1996, 2008]
        buey = [1937, 1949, 1961, 1973, 1985, 1997, 2009]
        tigre = [1938, 1950, 1962, 1974, 1986, 1998, 2010]
        conejo = [1939, 1951, 1963, 1975, 1987, 1999, 2011]
        serpiente = [1941, 1953, 1965, 1977, 1989, 2001, 2013]
        caballo = [1942, 1954, 1966, 1978, 1990, 2002, 2014]
        cabra = [1943, 1955, 1967, 1979, 1991, 2003, 2015]
        mono = [1944, 1956, 1968, 1980, 1992, 2004, 2016]
        gallo = [1945, 1957, 1969, 1981, 1993, 2005, 2017]
        perro = [1946, 1958, 1970, 1982, 1994, 2006, 2018]
        cerdo = [1947, 1959, 1971, 1983, 1995, 2007, 2019]

        if anio in dragon:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Dragon-300x257.jpg"
        elif anio in rata:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Rata-300x257.jpg"
        elif anio in buey:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Buey-300x257.jpg"
        elif anio in tigre:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Tigre-300x257.jpg"
        elif anio in conejo:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Conejo-300x257.jpg"
        elif anio in serpiente:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Serpiente-300x257.jpg"
        elif anio in caballo:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Caballo-300x257.jpg"
        elif anio in cabra:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Cabra-300x257.jpg"
        elif anio in mono:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Mono-300x257.jpg"
        elif anio in gallo:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Gallo-300x257.jpg"
        elif anio in perro:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Perro-300x257.jpg"
        elif anio in cerdo:
            url = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Cerdo-300x257.jpg"

        calificacion = 0
        if pregunta1 == "2":
            calificacion += 1
        if pregunta2 == "3":
            calificacion += 1
        if pregunta3 == "4":
            calificacion += 1
        if pregunta4 == "5":
            calificacion += 1
        if pregunta5 == "6":
            calificacion += 1
        return render_template("resultados.html", nombre=nombre, apaterno=apaterno, amaterno=amaterno, edad=edad, url=url, calificacion=calificacion, sexo=sexo)

    return render_template("alumnosExam.html")



if __name__=="__main__":
    app.run(debug=True,port=8080)