import RPi.GPIO as GPIO
class Led:
    def __init__(self, status):
        self.status = status
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(14, GPIO.OUT)


    def led_status(self):
        if (self.status == 'on'):
            GPIO.output(14, GPIO.HIGH)
        elif (self.status == 'off'):
            GPIO.output(14, GPIO.LOW)
        else:
            return 'Erreur de manipulation'
