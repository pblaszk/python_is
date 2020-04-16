from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return render_template('index.html')

#@app.route('/jakas-inna-strona', methods = ['POST', 'GET'])
def inna_funkcja():
    return "I co teraz?"

@app.route('/witaj')
@app.route('/witaj/<imie>')
@app.route('/witaj/<imie>/<path:wiek>')
def witaj_imie(imie = '', wiek=0):
    #return f"Witaj {imie}, masz {wiek} lat!".format(imie)
    return render_template('index.html', t_imie=imie, t_wiek=wiek)
app.run()