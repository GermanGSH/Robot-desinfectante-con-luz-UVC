import time
import board
import adafruit_scd4x
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)   

GPIO.setup(12,GPIO.OUT)
buzer1 = GPIO.PWM(12, 100)

i2c = board.I2C() # uses board.SCL and board.SDA
 
def ppmaire (): 
        scd4x = adafruit_scd4x.SCD4X(i2c)
        scd4x.start_periodic_measurement()
        
        while True:
            if scd4x.data_ready:
                temp = ("CO2: %d ppm" % scd4x.CO2)

                if scd4x.CO2 > 1000:
                     buzer1.start (50) 
                else:
                     buzer1.ChangeDutyCycle(0)
                return temp
    


        



