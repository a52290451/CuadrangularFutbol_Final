# Autor: Brayan Sierra

# Clase que representa el endpoint del BackEnd.

# Recibe las peticiones GET y POST que se realizan desde el FrontEnd (vistas).
# Tambien realiza el tejido de las vistas.

# Importación de paquetes Flask y de la lógica.
from flask import Flask, request, render_template, escape
from campeonato import *

app = Flask(__name__)

# Objeto de la clase Campeonato (Almacena información - Maneja persistencia en tiempo de ejecución)
camp = campeonato()

# Método que recibe peticiones de tipo GET / POST para registrar
# equipos, generar los cuentros y retornarlos.
@app.route('/marcadores/', methods =["GET","POST"])
def inicio():
    if request.method =="POST":
        try:
            # Reinicio y registro de equipos
            camp.equipos = []
            camp.emparejamientos = []
            camp.resEncuentros = []
            mensaje = ""
            camp.registrarEquipo(request.form["equipo1"])
            camp.registrarEquipo(request.form["equipo2"])
            camp.registrarEquipo(request.form["equipo3"])
            camp.registrarEquipo(request.form["equipo4"])
            # ---------------
            if (request.form["equipo1"] == request.form["equipo2"] or 
                request.form["equipo1"] == request.form["equipo3"] or
                request.form["equipo1"] == request.form["equipo4"] or
                request.form["equipo2"] == request.form["equipo3"] or
                request.form["equipo2"] == request.form["equipo4"] or
                request.form["equipo3"] == request.form["equipo4"]):
                mensaje = "El nombre de los equipos debe ser diferente"
                return render_template("index.html",mensaje=mensaje)
            else:
                # Generar encuentros
                camp.crearEncuentros()
                encuentros = []
                for par in camp.emparejamientos:
                    encuentros.append((par[0].nombre,par[1].nombre)) 
                # Redirecciona a la vista 'Marcadores', retornando la información de los encuentros.
                return render_template("marcadores.html",encuentros=encuentros)
        except Exception as e:
            print("==========>>>>")
            print(e)
    # Con una petición de tipo GET, redirecciona a la vista inicial.
    return render_template("index.html")

# Método que recibe peticiones de tipo GET / POST para calcular los puntos de los equipos,
# actualizar información, ordenar los equipos y retornarlos.
@app.route('/posiciones/', methods =["GET","POST"])
def posiciones():
    if request.method =="POST":
        try:
            # For para registrar el resultado de los encuentros
            for i in range(len(camp.emparejamientos)):
                camp.registrarEncuentro(camp.emparejamientos[i],
                        int(escape(request.form["goles1"+str(i)])),
                        int(escape(request.form["goles2"+str(i)])))
            resultados = []
            # For para calcular los puntos de cada equipo y almacenarlos en un arreglo
            for eq in camp.equipos:
                i = []
                i.append(eq.nombre)
                i.append(eq.victorias)
                i.append(eq.derrotas)
                i.append(eq.empates)
                i.append(eq.golesAnotados)
                i.append(eq.golesRecibidos)
                i.append(eq.golesAnotados - eq.golesRecibidos)
                i.append(eq.victorias*3 + eq.empates)
                resultados.append(i)
            # Ordenamiento de los equipos
            resultados.sort(key = lambda x: (-x[7],-x[6],-x[4],-x[1]))
            # Redirecciona a la vista 'posiciones', retornando la información de los resultados.
            return render_template("posiciones.html", resultados=resultados)
        except Exception as e:
            print("==========>>>>")
            print(e)
    # Con una petición de tipo GET, redirecciona a la vista inicial.
    return render_template("index.html")

# Método que recibe peticiones de tipo GET / POST para reiniciar el campeonato y
# redireccionar a la vista de inicio.
@app.route('/', methods =["GET","POST"])
def reinicio():
    camp.equipos = []
    camp.emparejamientos = []
    camp.resEncuentros = []
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)