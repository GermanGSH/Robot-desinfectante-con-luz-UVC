# Importamos la paquteria necesaria
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)   
GPIO.setwarnings(False)

TRIG = 10 
ECHO = 9 
TRIGB = 11
ECHOB = 5
TRIGR = 23
ECHOR = 24
TRIGL = 6
ECHOL = 13

GPIO.setup(TRIG, GPIO.OUT)  
GPIO.setup(ECHO, GPIO.IN)  
GPIO.setup(TRIGB, GPIO.OUT) 
GPIO.setup(ECHOB, GPIO.IN) 
GPIO.setup(TRIGR, GPIO.OUT) 
GPIO.setup(ECHOR, GPIO.IN) 
GPIO.setup(TRIGL, GPIO.OUT) 
GPIO.setup(ECHOL, GPIO.IN) 

def distanci ():
    while True:

        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.5) 

        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)
        
        while True:
            pulso_inicio = time.time()
            if GPIO.input(ECHO) == GPIO.HIGH:
                break
        
        while True:
            pulso_fin = time.time()
            if GPIO.input(ECHO) == GPIO.LOW:
                break

        duracion = pulso_fin - pulso_inicio

        distancia = (34300 * duracion) / 2

        dis = ( "%.0f cm" % distancia)
        return dis
      


def distancib ():
    while True:

        GPIO.output(TRIGB, GPIO.LOW)
        time.sleep(0.5)

        GPIO.output(TRIGB, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIGB, GPIO.LOW)
        
        while True:
            pulso_inicio = time.time()
            if GPIO.input(ECHOB) == GPIO.HIGH:
                break
        
        while True:
            pulso_fin = time.time()
            if GPIO.input(ECHOB) == GPIO.LOW:
                break

        duracion = pulso_fin - pulso_inicio

        distancia = (34300 * duracion) / 2

        dis = ( "%.0f cm" % distancia)
        return dis      
       
def distancir ():
    while True:

        GPIO.output(TRIGR, GPIO.LOW)
        time.sleep(0.5)

        GPIO.output(TRIGR, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIGR, GPIO.LOW)
        
        while True:
            pulso_inicio = time.time()
            if GPIO.input(ECHOR) == GPIO.HIGH:
                break
        
        while True:
            pulso_fin = time.time()
            if GPIO.input(ECHOR) == GPIO.LOW:
                break

        duracion = pulso_fin - pulso_inicio

        distancia = (34300 * duracion) / 2

        dis = ( "%.0f cm" % distancia)
        return dis    

def distancil ():
    while True:

        GPIO.output(TRIGL, GPIO.LOW)
        time.sleep(0.5)

        GPIO.output(TRIGL, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIGL, GPIO.LOW)
        
        while True:
            pulso_inicio = time.time()
            if GPIO.input(ECHOL) == GPIO.HIGH:
                break
        
        while True:
            pulso_fin = time.time()
            if GPIO.input(ECHOL) == GPIO.LOW:
                break

        duracion = pulso_fin - pulso_inicio

        distancia = (34300 * duracion) / 2

        dis = ( "%.0f cm" % distancia)
        return dis      
         
       
    
GPIO.cleanup()
