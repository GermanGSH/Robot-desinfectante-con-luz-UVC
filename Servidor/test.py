from flask import Flask,render_template, Response
from flask import Flask,render_template, jsonify
from threading import Thread
import cv2
import motores
import time                     
import RPi.GPIO as GPIO
import adafruit_scd4x
import SU
import co2

GPIO.setmode(GPIO.BCM) 


TRIG = 10 
ECHO = 9 
TRIGB = 11
ECHOB = 5
TRIGR = 23
ECHOR = 24
TRIGL = 6
ECHOL = 13
PIRA = 16
PIRA2 = 20
PIRA3 = 21 
RELE= 26
MRELE= 19


GPIO.setup(TRIG, GPIO.OUT) 
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIGB, GPIO.OUT) 
GPIO.setup(ECHOB, GPIO.IN) 
GPIO.setup(TRIGR, GPIO.OUT) 
GPIO.setup(ECHOR, GPIO.IN) 
GPIO.setup(TRIGL, GPIO.OUT) 
GPIO.setup(ECHOL, GPIO.IN) 
GPIO.setup(PIRA, GPIO.IN)
GPIO.setup(PIRA2, GPIO.IN)
GPIO.setup(PIRA3, GPIO.IN)
GPIO.setup(RELE, GPIO.OUT)
GPIO.setup(MRELE, GPIO.OUT)

GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.output(MRELE, 1)
GPIO.output(RELE, 0)


stop_run = False 

def manual_run():
    c = Thread(target= contador)
    t = Thread(target=sensor)
    c.start()
    t.start()
    return "procesing"

def sensor():
    global stop_run
    while not stop_run:
      x= 0  
      y= 0
      z= GPIO.input(PIRA)
      if 1 in (x, y, z):
          GPIO.output(RELE, 0)
      else:
          GPIO.output(RELE, 1)
          time.sleep(5)

def contador():
    global stop_run
    n = 0
    while not stop_run:
        n = n+1
        time.sleep(1)
        return n


app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def index():
    return render_template('index.html')     

@app.route("/update")
def update():
    dis = SU.distanci()
    disb = SU.distancib()
    disr = SU.distancir()
    disl = SU.distancil()
    templateData = {'data,' : dis ,
                    'datab' : disb,
                    'datar' : disr,
                    'datal' : disl}
    return jsonify(templateData), 200

@app.route("/updateco")
def updateco():
    ppm = co2.ppmaire()
    templateData = {'dataco' : ppm }
    return jsonify(templateData), 200

@app.route('/lighton')
def luzon():
    global stop_run
    stop_run = False
    con = contador()
    templateData = {'datacon' : con}
    return  jsonify(templateData),200 , Response(manual_run(), mimetype="text/html")


@app.route('/lightoff')
def luzoff():
    GPIO.output(RELE, 0)
    global stop_run
    stop_run = True
    return 'true'

@app.route('/motorson')
def mon():
    GPIO.output(MRELE, 0)
    return 'true'

@app.route('/motorsoff')
def moff():
    GPIO.output(MRELE, 1)
    return 'true'


@app.route('/forward')
def enfrente():
    motores.Forward()
    return 'true'

@app.route('/stop')
def detener():
    motores.Stop()
    return 'true'

@app.route('/right')
def derecha():
    motores.Right()
    return 'true'
    
@app.route('/left')
def izquierda():
    motores.Left()
    return 'true'
    
@app.route('/back')
def atras():
    motores.Backward()
    return 'true'

@app.route('/Tleft')
def girariz():
    motores.TLeft()
    return 'true'
    
@app.route('/Tright')
def girarde():
    motores.TRight()
    return 'true'
    
@app.route('/Cleft')
def ciz():
    motores.CLeft()
    return 'true'
    
@app.route('/Cright')
def cde():
    motores.CRight()
    return 'true'


@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(host= '192.168.4.1', debug=False)
