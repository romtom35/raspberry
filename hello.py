from flask import Flask
app = Flask(__name__)
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.OUT)
from flask import render_template
@app.route('/')
def index():
    return render_template('bouton.html')

@app.route('/hello/<name>')
def hello(name):
    return 'hello %s' % name

@app.route('/led/<on_off>')
def led(on_off):
    if(on_off == 'on'):
        GPIO.output(14, GPIO.HIGH)
        return render_template('bouton.html')
    elif(on_off == 'off'):
        GPIO.output(14, GPIO.LOW)
        return render_template('bouton.html')
    else:
        return 'Erreur de manipulation'
    return '%s' % on_off
