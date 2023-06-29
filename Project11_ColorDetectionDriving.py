# Proyecto 11 
# Usando la cámara del Pi para capturar y analizar los colores de los objetos # Construya el Proyecto 11 circuito y conduce el rover de acuerdo con las señales de colores 
#Desafío 1 
# Trate de cambiar los colores asociados con los mandatos de manejo, como cambiar el rojo y el verde 
#Desafío 2 
# Trate de agregar un operador de módulo para alternar entre giros a la izquierda y a la derecha en señales azules
#Desafío 3 
# Trate de configurar las variables de tiempo de manejo en función de la prominencia del color del argmax 
#Desafío 4 
# Trate de agregar una variable de memoria para el último color identificado y conducir siguiendo el patrón, como rojo y luego verde 
#Importing libraries 
# Aquí queremos sleep para el tiempo, GPIO para los pines de Pi y picamera para la cámara de Pi 
from time import sleep 
import RPi.GPIO as GPIO 
from picamera import PiCamera 
# Numpy es un gran paquete de herramientas numéricas para ayudar con las matemáticas import numpy as np 
#Definamos variables para poder usarlas más tarde 
Left_Forward_Pin = 36 #el número de pin interno de Pi que se ajusta a 1 Left_Backward_Pin = 11 #el número de pin interno de Pi que se ajusta a 2 Right_Forward_Pin = 12 #el número de pin interno de Pi que se ajusta a 3 Right_Backward_Pin = 35 #el número de pin interno de Pi que se ajusta a 4 Button_Pin = 38 #el número de pin interno de Pi que se ajusta a 5 
#Aquí podemos definir las variables de tiempo para las funciones de conducción, en segundos Forward_Time = 2 
Backward_Time = 1 
Left_Turn_Time = 0.5 
Right_Turn_Time = 0.5 
Wait_Time = 1 
#Configurando nuestros pines 
GPIO.setmode(GPIO.BOARD) 
#Nuestros pines de salida, empiezan apagado  
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW)
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) 
#Nuestros pines de entrada, empiezan abajo 
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
#Escribamos algunas funciones de conducción que podamos usar más adelante 
def drive_forward(time):  
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierdo adelante GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Motor derecho adelante  sleep(time) 
 GPIO.output(Left_Forward_Pin, GPIO.LOW) #motor izquierdo apagado  
 GPIO.output(Right_Forward_Pin, GPIO.LOW) #motor derecho apagado
 print('forward') 
 sleep(1) 
def drive_left_turn(time): 
 GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Motor izquierdo hacia atrás  GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Motor derecho adelante  sleep(time) 
 GPIO.output(Left_Backward_Pin, GPIO.LOW) #motor izquierdo apagado  
 GPIO.output(Right_Forward_Pin, GPIO.LOW) #motor derecho apagado 
 print('left turn') 
 sleep(1) 
  
def drive_right_turn(time): 
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierdo adelante GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Motor derecho hacia atrás  sleep(time) 
 GPIO.output(Left_Forward_Pin, GPIO.LOW) #motor izquierdo apagado  
 GPIO.output(Right_Backward_Pin, GPIO.LOW) #motor derecho apagado 
 print('right turn') 
 sleep(1) 
def drive_backward(time): 
 GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Motor izquierdo hacia atrás  GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Motor derecho hacia atrás  sleep(time) 
 GPIO.output(Left_Backward_Pin, GPIO.LOW) #motor izquierdo apagado 
 GPIO.output(Right_Backward_Pin, GPIO.LOW) #motor derecho apagado
 print('backward') 
 sleep(1) 
  
# Para desafío 2, usaremos una variable ¨dummy¨ para ayudar con el operador de módulo count = 0 
# Reemplace la True declaraciones con la sentencia del operador módulo cómo %, que significa resto en división
# Entonces, el módulo 2 realiza las pulsaciones pares e impares por dividiendo por 2 tiene un resto de 0
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
# Para usar esto como una lógica, intentemos count % 2 == 0  
# Para desafío 3, estableceremos la intensidad de color variable para escalar los tiempos de conducción
Color_Intensity = 1 
# Configuración de la cámara para el análisis y para enfatizar los colores 
camera = PiCamera() 
camera.resolution = (640, 480) 
camera.framerate = 30 
sleep(2) #deja que la cámara asiente 
camera.iso = 100 
camera.shutter_speed = camera.exposure_speed 
camera.exposure_mode = 'off' 
gain_set = camera.awb_gains 
camera.awb_mode = 'off' 
camera.awb_gains = gain_set 
# Preparación para el análisis de imágenes y eliminación del ruido
#Las imágenes se almacenan en una matriz 3D y cada píxel tiene valores de rojo, verde y azul Image = np.empty((640,480,3),dtype=np.uint8) 
Noise = np.empty((640,480,3),dtype=np.uint8) 
RGB_Text = ['Red','Green','Blue'] #Matriz para nombrar colores 
# Quitando el ruido camera.capture(Noise,'rgb') 
Noise = Noise-np.mean(Noise) 
#Bucle con diferentes imágenes para determinar los colores de los objetos 
print('Ready to take photo') 
while True: 
  
 #Pulse el botón para capturar una imagen
 if GPIO.input(Button_Pin) == True: 
 sleep(2) 
 print('Photo taken') 
 camera.capture(Image,'rgb') 
 RGB_Array = [] 
  
 # Para cada uno de rojo, verde y azul, calcula el color más prominente por los promedios  
 for col in range(0,3): 
 RGB_Array.append(np.mean(Image[:,:,col]-np.mean(Image)- np.mean(Noise[:,:,col])))  
 Color = RGB_Text[np.argmax(RGB_Array)] 
 print(Color) 
  
 # Para desafío 3, comparemos el color más prominente con el segundo más  # Podemos usar esta relación para establecer la Color_Intensity variable
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
 # con max como np.max(RGB_Array) y mid como np.median(RGB_Array)  # Sin embargo, los canales de color pueden ser negativos, así que usemos un máximo para mantener el positivo 
 Color_Intensity = np.max([np.max(RGB_Array) / np.median(RGB_Array), 2])   
 # Para desafío 4, busquemos un patrón como Rojo y luego Color  #Podemos usar un if declaración para ver si el Last_Color era rojo  # Reemplazar está True declaración con una lógica para verificar, recuerda que es ==, not = here  if Last_Color == 'Red': 
  
 # Activar las salidas del controlador de motor según el color del objeto determinado  if Color == 'Red': #Hacia atrás para un objeto rojo
 drive_backward(Backward_Time * Color_Intensity) 
 sleep(Wait_Time) 
  
 if Color == 'Green': #Adelante para un objeto verde
 drive_forward(Forward_Time * Color_Intensity) 
 sleep(Wait_Time) 
 if Color == 'Blue': #Gire para el objeto azul 
  
 if count % 2 == 0: # Trata cambiado el True declaración al módulo para desafío 2 
 drive_left_turn(Left_Turn_Time * Color_Intensity)   
 else: # Para desafío 2, módulo usa estos mandatos de manejo en bucles impares 
 drive_right_turn(Right_Turn_Time * Color_Intensity)   
 sleep(Wait_Time) 
 count = count + 1 # Incrementa el contador para el módulo   
 # Para desafío 4, usa Last_Color después de las salidas 
 Last_Color = Color 
 print('Ready to take photo') 
