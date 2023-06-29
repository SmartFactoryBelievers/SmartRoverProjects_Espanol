# Proyecto 12 
# Usando la cámara del Pi para capturar y analizar los niveles de luz
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
# Construya el Proyecto 12 circuito y conducir el rover para buscar la luz 
#Desafío 1 
# Trate de cambiar los umbrales de izquierda y derecha para forzar diferentes patrones 
#Desafío 2 
# Trate de usar la función de módulo y el contador de bucles para pasar de avance a retroceso cada pocos ciclos
#Desafío 3 
# ¿Puede agregar un temporizador al bucle para hacer un giro después de 30 segundos de búsqueda? 
#Desafío 4 
# ¿Puede establecer la duración del tiempo de conducción en función de la proporción de luz de izquierda a derecha? 
#Importing libraries 
# Aquí queremos sleep para el tiempo, GPIO para los pines de Pi y picamera para la cámara de Pi. 
from time import sleep 
import time 
import RPi.GPIO as GPIO 
from picamera import PiCamera 
# También necesitaremos PiRGBArray y cv2 para ver los imágenes visualmente from picamera.array import PiRGBArray 
import cv2 
# Numpy es un gran paquete de herramientas numéricas para ayudar con las matemáticas import numpy as np 
#Definamos variables para poder usarlas más tarde 
Left_Forward_Pin = 36 #el número de pin interno de Pi que se ajusta a 1 Left_Backward_Pin = 11 #el número de pin interno de Pi que se ajusta a 2 Right_Forward_Pin = 12 #el número de pin interno de Pi que se ajusta a 3 Right_Backward_Pin = 35 #el número de pin interno de Pi que se ajusta a 4 
#Aquí podemos definir las variables de tiempo para las funciones de conducción, en segundos Forward_Time = 2 
Backward_Time = 1 
Left_Turn_Time = 0.5 
Right_Turn_Time = 0.5 
Wait_Time = 1 
#Configurando nuestros pines
GPIO.setmode(GPIO.BOARD) 
#Nuestros pines de salida, empiezan apagado  
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) 
#Escribamos algunas funciones de conducción que podamos usar más tarde 
def drive_forward(time):  
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierdo adelante  GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Motor derecho adelante  sleep(time) 
 GPIO.output(Left_Forward_Pin, GPIO.LOW) #motor izquierdo apagado  
 GPIO.output(Right_Forward_Pin, GPIO.LOW) #motor derecho apagado  print('forward') 
 sleep(1) 
def drive_left_turn(time): 
 GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Motor izquierdo hacia atrás  GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Motor derecho adelante  sleep(time) 
 GPIO.output(Left_Backward_Pin, GPIO.LOW) #motor izquierdo apagado  
 GPIO.output(Right_Forward_Pin, GPIO.LOW) #motor derecho apagado  print('left turn') 
 sleep(1) 
  
def drive_right_turn(time): 
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierdo adelante GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Motor derecho hacia atrás  sleep(time) 
 GPIO.output(Left_Forward_Pin, GPIO.LOW) #motor izquierdo apagado  
 GPIO.output(Right_Backward_Pin, GPIO.LOW) #motor derecho apagado  print('right turn') 
 sleep(1) 
def drive_backward(time): 
 GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Motor izquierdo hacia atrás  GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Motor derecho hacia atrás  sleep(time) 
 GPIO.output(Left_Backward_Pin, GPIO.LOW) #motor izquierdo apagado  
 GPIO.output(Right_Backward_Pin, GPIO.LOW) #motor derecho apagado   print('backward') 
 sleep(1) 
  
#Configuración de la cámara 
camera = PiCamera() 
camera.rotation = 180 
camera.resolution = (640, 480) 
camera.framerate = 30 
rawCapture = PiRGBArray(camera, size=(640, 480)) 
#Configurando Min y Max valores para Hue, Saturation (Grayness), y Value (Lightness) Light_Min = np.array([0,50,155], np.uint8)
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
Light_Max = np.array([255,255,255], np.uint8) 
# Porcentaje de luz ambiental de un lado al otro, umbral para girar el rover # Para desafío 1, trata a ajustar estos valores para forzar más o menos giros Left_Threshold = 51 
Right_Threshold = 51 
# Para desafío 2, usaremos una variable ¨dummy¨ para ayudar con el operador de módulo count = 0 
# Reemplace las declaraciones True con la frase del operador módulo cómo %, que significa resto en división 
# Entonces, el módulo 2 realiza las pulsaciones pares e impares por dividiendo por 2 tiene un resto de 0 
# Para usar esto como lógico, intentemos contar % 2 == 0 
# Para desafío 2, podemos usar la función de temporizador para controlar la búsqueda de luz Start_Time = time.time() 
Max_Search_Time = 30 #segundos 
# Para desafío 4, podemos inicializar una variable para la intensidad de la luz para escalar las duraciones de los turnos
Light_Intensity = 1 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True) : 
 #Capturando imágenes de la cámara y conversión a formato HSV 
 sleep(3) 
 Image = frame.array 
 hsv = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV) 
  
 # Analizando el valor (lightness)capa de la imagen (3rd layer)  Light = hsv[:,:,2] 
  
 # Calculando la luz total de cada lado del imagen
 Left_Light = sum(sum(Light[:,0:320])) 
 Right_Light = sum(sum(Light[:,320:])) 
  
 # Determinación del porcentaje de luz de cada lado de la imagen
 Left_Light_Perc = Left_Light / sum(sum(Light)) 
 Right_Light_Perc = Right_Light / sum(sum(Light)) 
 print('L = ' + str(Left_Light_Perc) + ' and R = ' + str(Right_Light_Perc)) 
 # Para desafío 3, determinar el tiempo transcurrido del movimiento hacia adelante Elapsed_Time = round(time.time() - Start_Time,2) 
  
 # Para desafío 4, encontremos la relación entre la luz máxima y la luz mínima  # Podemos establecer esto como la intensidad con np.max([Left_Light_Perc, Right_Light_Perc ]) 
 # and np.min([Left_Light_Perc, Right_Light_Perc]), respectivamente
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
 Light_Intensity = np.max([Left_Light_Perc, Right_Light_Perc]) / np.min([Left_Ligh t_Perc, Right_Light_Perc]) 
  
  
 # Si el lado izquierda es más claro que el umbral, gire a la izquierda 
 if Left_Light_Perc > Left_Threshold/100: 
 drive_left_turn(Left_Turn_Time * Light_Intensity) 
  
 # Si el lado derecha es más claro que el umbral, gire a la derecha   else: 
 if Right_Light_Perc > Right_Threshold/100: 
 drive_right_turn(Right_Turn_Time * Light_Intensity) 
  
 # Si ninguno de los lados supera el umbral, conduzca hacia adelante (¿o hacia atrás?)   
else: 
  
 if Elapsed_Time < Max_Search_Time: # Trata cambiar el True a un comparitive (<) entre
 # Elapsed_Time y Max_Search_Time para desafío 3   
 if count % 2 == 0: # Trata a cambiar el True to al módulo para desafío 2 
 drive_forward(Forward_Time) 
 else: # Para desafío 2, módulo usa estos mandatos de manejo en bucles impares 
 drive_backward(Backward_Time) 
  
 count = count + 1 # Incrementa el contador para el módulo  
 else: # Si se excedió el tiempo máximo de, girar y buscar en otra parte para desafío 3 
 drive_left_turn(Left_Turn_Time * 2) 
 # Restablecer el temporizador 
 Start_Time = time.time() 
 print('here') 
  
 sleep(Wait_Time)  
  
 #Borrando imágenes 
 rawCapture.truncate(0) 
