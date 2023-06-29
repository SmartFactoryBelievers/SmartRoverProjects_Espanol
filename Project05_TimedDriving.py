# Proyecto 5 
# Aprender a programar, escribir funciones, usar salidas de control de motor, y agregar funciones de devolución de llamada
# Construya el Proyecto 5 circuito y conducir el rover durante pulsaciones de botones, Simon Says estilo 
# Mantenga presión en el botón para conducir durante ese tiempo 
#Desafío 1 
# Trate de cambiar los funciones de conducción para cambiar las direcciones de conducción 
#Desafío 2 
# Agregue nuevas funciones de manejo para activar en el bucle para crear una nueva ruta de conducción
#Desafío 3 
# Use el operador de módulo para cambiar las direcciones de conducción en función de las pulsaciones de números pares o impares. 
#Desafío 4 
# Con el módulo, agregue nuevas funciones de manejo para prensas pares o impares 
#Importing libraries 
# Aquí queremos la función sleep para el tiempo y GPIO para el pin de Pi from time import sleep 
import RPi.GPIO as GPIO 
# Ahora también estamos usando la tiempo general para la función de temporizador import time 
#Definamos variables para poder usarlas más tarde 
Left_Forward_Pin = 36 #el número de pin interno de Pi que se ajusta a 1 Left_Backward_Pin = 11 #el número de pin interno de Pi que se ajusta a 2 Right_Forward_Pin = 12 #el número de pin interno de Pi que se ajusta a 3 Right_Backward_Pin = 35 #el número de pin interno de Pi que se ajusta a 4 Button_Pin = 38 #el número de pin interno de Pi que se ajusta a 6 
#Configurando nuestros pines
GPIO.setmode(GPIO.BOARD) 
#Nuestros pines de salida, empieza apagado 
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) 
#Nuestro pin de entrada desde el botón 
GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
#Escribamos algunas funciones de conducción que podamos usar más tarde para programar un pathdef drive_forwa rd():
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
def drive_forward(time):  
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierda adelante GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Motor derecho adelante  sleep(time) 
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
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierda adelante  GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Motor derecho hacia atrás  sleep(time) 
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
# Aquí estamos creando una función de temporizador para registrar la duración de la pulsación del botón. def button_press_timer(): 
 Start_Time = time.time() #Empiece el reloj 
 while GPIO.input(Button_Pin): #mientras se presiona el botón...   print("Button Pressed") 
 return round(time.time() - Start_Time,2) #para el temporizador, devolver el tiempo transcurrido 
# Para desafíos 3 y 4, usaremos una variable ¨dummy¨ para ayudar con el operador de módulo count = 0 
# Reemplace la True declaraciones con la sentencia del operador módulo cómo %, que significa resto en división 
# Entonces, el módulo 2 realiza las pulsaciones pares e impares por dividiendo por 2 tiene un resto de 0 
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
# Para usar esto como una lógica, intentemos count % 2 == 0 
while True: #Bucle 
 sleep(0.25) 
  
 # Si se presiona el botón, usamos la función de temporizador para ver cuánto tiempo  if GPIO.input(Button_Pin): 
 Button_Time = button_press_timer() 
 print('Button pressed ' + str(Button_Time) + ' seconds') 
  
 if count % 2 == 0: # Trate de cambiar las declaraciones True al módulo para desafíos 3 y 4 
 #Para desafíos 1 y 2, trata a añadir nuevas funciones de conducción aquí  drive_forward(Button_Time) 
  
 else: # Para ser utilizado en desafíos 3 y 4 
 drive_backward(Button_Time) 
 # Agregue otras funciones de manejo aquí para presionar botones impares  
 count = count + 1 # Incrementamos el contador para la siguiente pulsación de botón
