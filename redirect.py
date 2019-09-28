from flask import Flask, redirect
from jsonLoader import Load

app = Flask(__name__)

__author__ = 'Alisson Tenorio Pinto'
__email__ = 'alisson@nti.ufal.br'


@app.route("/")
def test_system():
    return "System operational"


@app.route('/<url>')
def load(url):
    return_url = Load.search(url)

    if return_url is not None:
        return redirect(return_url, code=302)
    else:
        return "Unidade nao cadastrada no json file"


if __name__ == "__main__":
    app.run()

