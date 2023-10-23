#Librerías generales

from flask import Flask
from flask import render_template

#Librería para servidor de producción
from waitress import serve

import requests





#Código general de Flask

app = Flask(__name__,static_folder='static')


def solicitud():
    response = requests.get("https://zenoplay.zenomedia.com/api/zenofm/nowplaying/9bzzhtf2uk8uv")
    data = response.json()
    title = data['title']

    return title


@app.route('/')
def index():

    variable = solicitud()
    print(variable)

    return render_template('header.html', variable = variable)






mode = "prod"

if __name__ == '__main__':
     
    if mode == "dev":
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        serve(app,host='0.0.0.0',port=5000,threads=6)

