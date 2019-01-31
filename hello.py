from flask import Flask
app = Flask(__name__)
from flask import render_template
from led import Led
led = Led('off')
@app.route('/')
def index():
    return render_template('bouton.html')

@app.route('/hello/<name>')
def hello(name):
    return 'hello %s' % name

@app.route('/led/<on_off>')
def led(on_off):
    led.led_status(on_off)
    return render_template('bouton.html')



