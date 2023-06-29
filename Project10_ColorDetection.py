# Proyecto 10
# Usando las cámaras del Pi para capturar y analizar los colores de los objetos # Construya el circuito Proyecto 10 e indica el color de los objetos con LED y el zumbador 
#Desafío 1 
# Trate de intercambiar las salidas de LED y el zumbador en el código y luego también en el Smart Rover
#Desafío 2 
# Trate de escribir una función para manejar el LED y el zumbador para que pueda llamarse después de cada color 
#Desafío 3 
# Trate de agregar un margen para el argmax para Color debe exceder para ser considerado un cierto color 
#Desafío 4 
# Trate de agregar una variable de memoria para el último color identificado
# una nueva salida de LED o zumbador tiene un patrón, como rojo y luego verde 
#Importing libraries 
# Aquí queremos sleep para el tiempo, GPIO para los pines de Pi y picamera para la cámara de Pi. 
 from time import sleep 
import RPi.GPIO as GPIO 
from picamera import PiCamera 
# Numpy es un gran paquete de herramientas numéricas para ayudar con las matemáticas import numpy as np 
#Definamos variables para poder usarlas más tarde 
LED_Pin = 35 #el número de pin interno de Pi que se ajusta a 4 
Buzzer_Pin = 12 #el número de pin interno de Pi que se ajusta a 3 
Button_Pin = 38 #el número de pin interno de Pi que se ajusta a 6 
#Configurando nuestros pines
GPIO.setmode(GPIO.BOARD) 
#Nuestros pines de salida, empiezan apagado  
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Buzzer_Pin, GPIO.OUT, initial=GPIO.LOW) 
#Nuestros pines de entrada, empiezan abajo
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
# Configuración de la cámara para el análisis y para enfatizar los colores
camera = PiCamera() 
camera.resolution = (640, 480)camera.framerate = 30 
sleep(2) #deja que la cámara se asiente
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
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
# Para desafío 2, creemos una función como la que hemos hecho antes para las salidas # Deber tener output_pin y argumentos de tiempo para convertirlos a High y después Low def your_function(output_pin, delay): 
 sleep(delay) 
 GPIO.output(output_pin, GPIO.HIGH) 
 sleep(delay) 
 GPIO.output(output_pin, GPIO.LOW) 
# Para desafío 3, establezcamos un umbral que el color máximo debe superar # Esto ayudará a la cámara a evitar errores Col_Margin = 0.8 
# Verifique que max * margin > mid 
# con max como np.max(RGB_Array) y mid como np.median(RGB_Array) 
#Bucle con diferentes imágenes para determinar los colores de los objetos al presionar el botón print('Ready to take photo') 
while True: 
  
 # Pulse el botón para capturar una imagen 
 if GPIO.input(Button_Pin) == True: 
 sleep(2) 
 print('Photo taken') 
 camera.capture(Image,'rgb') 
 RGB_Array = [] 
  
 # Para cada uno de rojo, verde y azul, calcula el color más prominente por los promedios   
 for col in range(0,3): 
 RGB_Array.append(np.mean(Image[:,:,col]-np.mean(Image)- np.mean(Noise[:,:,col]))) 
 
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
 # Para desafío 3, reemplace la True declaración con la declaración lógica para el margen 
 if np.max(RGB_Array) * Col_Margin > np.median(RGB_Array):  Color = RGB_Text[np.argmax(RGB_Array)] 
 print(Color) 
 else: 
 print('No prominent color found') 
  
 # Para desafío 4, busquemos un patrón como Rojo y luego Color  # Podemos usar el condicional if para ver si el Last_Color era Rojo  # Reemplace está declaración True con un lógico para verificar, recuerda que es ==, no =  if Last_Color == 'Red': 
  
 # Activar salidas if Color == 'Red': #LED para objeto rojo 
 GPIO.output(LED_Pin, GPIO.HIGH) #LED encendida 
 sleep(2) 
 GPIO.output(LED_Pin, GPIO.LOW) #LED apagado 
  
 if Color == 'Green': #Zumbador para objeto verde 
 GPIO.output(Buzzer_Pin, GPIO.HIGH) #Zumbador encendida
 sleep(2) 
 GPIO.output(Buzzer_Pin, GPIO.LOW) #Zumbador apagado 
  
 if Color == 'Blue': #LED y Zumbador para objeto azul
 GPIO.output(LED_Pin, GPIO.HIGH) #LED encendida 
 GPIO.output(Buzzer_Pin, GPIO.HIGH) #Zumbador encendida 
 sleep(2) 
 GPIO.output(LED_Pin, GPIO.LOW) #LED apagado 
 GPIO.output(Buzzer_Pin, GPIO.LOW) #Zumbador apagado 
  
 # Para desafío 4, actualice Last_Color después de las salidas 
 Last_Color = Color 
 print('Ready to take photo') 
