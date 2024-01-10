import time                     
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)       
GPIO.setwarnings(False)

pinDir1 = 4
pinDir2 = 14
pinDir3 = 17
pinDir4 = 8

GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

motor1 = GPIO.PWM(18, 2000)
motor2 = GPIO.PWM(15, 2000)
motor3 = GPIO.PWM(27, 2000)
motor4 = GPIO.PWM(7, 2000)
duty = 50

def Forward ():
        GPIO.output(pinDir1, 0)
        GPIO.output(pinDir2, 1)
        GPIO.output(pinDir3, 0)
        GPIO.output(pinDir4, 1)
        motor1.start (duty) 
        motor2.start (duty)
        motor3.start (duty)
        motor4.start (duty) 
        
def Backward ():
        GPIO.output(pinDir1, 1)
        GPIO.output(pinDir2, 0)
        GPIO.output(pinDir3, 1)
        GPIO.output(pinDir4, 0)
        motor1.start (duty) 
        motor2.start (duty)
        motor3.start (duty)
        motor4.start (duty) 

def Right ():
        GPIO.output(pinDir1, 0)
        GPIO.output(pinDir2, 0)
        GPIO.output(pinDir3, 1)
        GPIO.output(pinDir4, 1)
        motor1.start (duty) 
        motor2.start (duty)
        motor3.start (duty)
        motor4.start (duty)   
        
def Left ():
        GPIO.output(pinDir1, 1)
        GPIO.output(pinDir2, 1)
        GPIO.output(pinDir3, 0)
        GPIO.output(pinDir4, 0)
        motor1.start (duty) 
        motor2.start (duty)
        motor3.start (duty)
        motor4.start (duty) 
        
def TRight ():
        GPIO.output(pinDir1, 0)
        GPIO.output(pinDir2, 0)
        GPIO.output(pinDir3, 0)
        GPIO.output(pinDir4, 0)
        motor1.start (duty) 
        motor2.start (duty)
        motor3.start (duty)
        motor4.start (duty) 
        
def TLeft ():
        GPIO.output(pinDir1, 1)
        GPIO.output(pinDir2, 1)
        GPIO.output(pinDir3, 1)
        GPIO.output(pinDir4, 1)
        motor1.start (duty) 
        motor2.start (duty)
        motor3.start (duty)
        motor4.start (duty)
        
def CRight ():
        GPIO.output(pinDir1, 0)
        GPIO.output(pinDir4, 1)
        motor1.start (duty) 
        motor4.start (duty) 
        
def CLeft ():
        GPIO.output(pinDir2, 1)
        GPIO.output(pinDir3, 0)
        motor2.start (duty)
        motor3.start (duty)
        
        
def Stop ():
        motor1.ChangeDutyCycle(0)
        motor2.ChangeDutyCycle(0)
        motor3.ChangeDutyCycle(0)
        motor4.ChangeDutyCycle(0)
        
GPIO.cleanup()

