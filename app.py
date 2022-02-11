from flask import Flask, escape, request, render_template, url_for #Importar la librería

app = Flask(__name__) #Inicializamos la app con el nombre

@app.route ('/') #Definimos que en la ruta de inicio será aplicada la función hola.
def hola():
    return 'Hi Penguins!' #Retorna Hi Penguins!



@app.route ('/coach') #Creamos la ruta coach
def hola_coaches(): #Definimos la función que será devuelta
    nombre= 'Meli' #Inicializamos un dato
    devolver= request.args.get('nombre', nombre) #Definimos que será devuelto y renderizado
    return f'Hola, {escape(devolver)}' #Retornamos al html

@app.route ('/inicio') #Creamos la ruta inicio
def inicio():
    return render_template('inicio.html')

@app.route ('/contacto') #Creamos la ruta contacto
def contacto():
    return render_template('contacto.html')
    
app.run(debug=True)