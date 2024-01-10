# Robot-desinfectante-con-luz-UVC

*.- La carpeta Servidor contiene todos los archivos para el control del robot 

*.- El archivo test.py es el principal, el que levanta el servidor

*.- Para utilizar el sensor SCD-40 para la medición del CO2 se instaló la librería Adafruit scd4x.

*.- Los archivos dentro de la carpeta servidor como motores, SU y PIR contienen funciones que se importan a test.py 

*.- El archivo index.html que está dentro de la carpeta templates, es la página web que muestra la interfaz para controlar el robot.

*.- Para levantar la red wifi se tomó en cuenta este link https://www.raspberrypi.com/documentation/computers/configuration.html#setting-up-a-routed-wireless-access-point

*.- Para ejecutar el programa al encendido de la tarjeta se usó el método de System ya que los demás no funcionaron para levantar el servidor.

*.- Para poder usar el robot y cualquier duda con respecto a su funcionamiento se puede leer los documentos "Manual de usuario Robot desinfectante con luz UVC.pdf" y "Robot Desinfectante con Luz UVC.pdf"
