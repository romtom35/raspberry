from flask import Flask
app = Flask(__name__)
from flask import render_template
from led import Led
led1 = Led('off')
@app.route('/')
def index():
    return render_template('bouton.html')

@app.route('/hello/<name>')
def hello(name):
    return 'hello %s' % name

@app.route('/led/<on_off>')
def led(on_off):
    if on_off == 'on' or on_off == 'off':
        led1.status = on_off
        led1.led_status()
    elif on_off == 'blink':
        led1.blink()
    return render_template('bouton.html')



