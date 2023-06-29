# Proyecto 9 
# Use la cámara de Pi para capturar y analizar los niveles de luz
# Construya el Proyecto 9 circuito y parpadea el LED cuando se superan ciertos umbrales de luz 

# Apunte una linterna a la cámara para activar el LED
#Desafío 1 
# Trate de cambiar el valor del umbral de luz para tener el LED siempre encendido
#Desafío 2 
# Trate de cambiar el valor del umbral de luz para tener el LED siempre apagado
#Desafío 3 
# ¿Puede agregar otro pin para que suene el zumbador cuando la luz ambiental es demasiado baja? 
#Desafío 4 
# ¿Puede intercambiar los umbrales Max y Min luces para activar el LED en la oscuridad?
#Importing libraries 
# Aquí queremos sleep para el tiempo, GPIO para los pines de Pi y picamera para la cámara de Pi 
from time import sleep 
import RPi.GPIO as GPIO 
from picamera import PiCamera 
# También necesitaremos PiRGBArray y cv2 para ver los imágenes visualmente  from picamera.array import PiRGBArray 
import cv2 
# Numpy es un gran paquete de herramientas numéricas para ayudar con las matemáticas import numpy as np 
#Definamos variables para poder usarlas más tarde 
LED_Pin = 35 #el número de pin interno de Pi que se ajusta a 4 
Buzzer_Pin = 12 #el número de pin interno de Pi que se ajusta a 3 
#Configurando nuestros pines
GPIO.setmode(GPIO.BOARD) 
#Nuestros pines de salida, empiezan apagado 
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) 
#Configuración de la cámara para detección de luz 
camera = PiCamera() 
camera.resolution = (640, 480) 
camera.framerate = 30 
rawCapture = PiRGBArray(camera, size=(640, 480)) 
#Configurando Min y Max valores para el HSV análisis de imagen
# Al igual que RGB, HSV es un esquema de color de imagen pero no está definido por una relación de color 
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
# En su lugar, utilice Hue (Color), Saturation (Grayness), y Value (Lightness) # Hue es 0 a 180 mientras Saturation y Value son 0 a 255 
# Para desafío 4, trate de poner el tecer valor (Lightness) de Light_Min a 0 Light_Min = np.array([0,50,0], np.uint8) 
Light_Max = np.array([180,255,255], np.uint8) 
# Umbral de porcentaje de luz ambiental para encender el LED 
# Para desafíos 1 y 2, trate de cambiar este valor para afectar el LED Light_Threshold = 40 
#Contador de bucles, se usa para asentar la cámara con luz ambiental 
i=0 
# Usando el vídeo función de la cámara for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True) : 
 #Captura de imágenes de la cámara y conversión a formato HSV 
 sleep(3) 
 image = frame.array 
 hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
 #Establecer el límite inferior como el promedio de la luz ambiental  if i < 1: 
 Ambient_Light = np.mean(np.mean(hsv[:,:,2])) 
 #Para desafío 4, trate de configurar Light_Max al nivel ambiental en su lugar  Light_Max = np.array([180, 255, Ambient_Light], np.uint8)
 #Quitando píxeles con menos luminosidad que el promedio del ambiente  # Esto crea una máscara que se usa para demarcar regiones clave de una imagen  Light_Filter = cv2.inRange(hsv,Light_Min, Light_Max) 
  
 #Porcentaje de píxeles por encima del umbral de luz
 # número de píxeles en la imagen  
Light_Percent = round(sum(sum(Light_Filter ==255))/(640*480),2)   
 # Si se supera el umbral de porcentaje de luz, parpadea el LED  if Light_Percent > Light_Threshold/100: 
 print(str(Light_Percent) + ' of image above ambient light levels')  GPIO.output(LED_Pin, GPIO.HIGH) #LED encendida
 sleep(2) 
 GPIO.output(LED_Pin, GPIO.LOW) #LED apagado 
  
 # For desafío 3, si no hay suficiente luz, agregue un zumbador aquí   else: 
 print('Not enough light detected') 
 GPIO.output(Buzzer_Pin, GPIO.HIGH) #Zumbador encendido 
 sleep(2) 
 GPIO.output(Buzzer_Pin, GPIO.LOW) #Zumbador apagado
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
  
 #Borrando imagenes
 rawCapture.truncate(0) 
 # Iterar contador
 i = i + 1
