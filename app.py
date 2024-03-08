from flask import Flask, render_template
from meudb import obj_computador


app = Flask(__name__)


@app.route('/bd/tabela/computador')
def teste():
    
    return render_template("view.html", lista_computador = obj_computador.selecionar_todos_registros())


if __name__ == '__main__':
    app.run()
