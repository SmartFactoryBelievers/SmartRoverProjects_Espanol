# Proyecto 6 
# Aprendiendo a programar, escribir funciones, usar salidas de control de motor, y agregar un complejo bucle
# Construya el Proyecto 6 circuito y hacer que el rover sea controlado por la luz ambiental  # Baje la luz y apunte una linterna al rover para dirigirlo 
#Desafío 1 
# Trate de cambiar las funciones de conducción para cambiar las direcciones de conducción 
#Desafío 2 
# Agregue nuevas funciones de manejo para cambiar su patrón de giro de búsqueda de luz 
#Desafío 3 
# Agregue la resistencia de 100 Ohm en serie con la fotorresistencia para aumentar la sensibilidad a la luz 
#Desafío 4 
# Con el operador de módulo, haga que el rover alterne los giros a la izquierda o a la derecha en la búsqueda de la luz 
#Desafío 5 
# Después de una cierta cantidad de tiempo, haz que el rover gire para buscar luz. 
#Importing libraries 
# Aquí queremos la función sleep para el tiempo y GPIO para el pin de Pi import time 
from time import sleep 
import RPi.GPIO as GPIO 
#Definamos variables para poder usarlas más tarde 
Left_Forward_Pin = 36 #el número de pin interno de Pi que se ajusta a 1 Left_Backward_Pin = 11 #el número de pin interno de Pi que se ajusta a 2 Right_Forward_Pin = 12 #el número de pin interno de Pi que se ajusta a 3 Right_Backward_Pin = 35 #el número de pin interno de Pi que se ajusta a 4 Photo_Pin = 38 #el número de pin interno de Pi que se ajusta a 5 
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
#Nuestro pin de entrada desde el botón 
GPIO.setup(Photo_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
#Escribamos algunas funciones de conducción que podamos usar más tarde
def drive_forward(time):  
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierdo adelante  GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Motor derecho adelante  sleep(time) 
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
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierdo adelante  GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Motor derecho hacia atrás sleep(time) 
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
# Para desafío 4, usaremos una variable ¨dummy¨ para ayudar con el operador de módulo count = 0 
# Reemplace las declaraciones True con la sentencia del operador módulo cómo %, que significa resto en división 
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
# Entonces, el módulo 2 realiza las pulsaciones pares e impares por dividiendo por 2 tiene un resto de 0 
# Para usar esto como una lógica, intentemos count % 2 == 0  
# Para desafío 5, estableceremos un tiempo máximo de búsqueda de luz para el bucle Max_Search_Time = 4 #segundos 
# Si el rover no ha encontrado luz por un tiempo, podemos salir del bucle con una declaración de interrupción
# break sale del bucle más interno y permite que el móvil regrese al primer mandato de sleep 
while True: # Externo continuo While bucle
 sleep(0.25) 
 count = count + 1 # Incrementa el contador para el módulo
  
 # Si el fototransistor detecta suficiente luz, conduzca hacia el luz  if GPIO.input(Photo_Pin): 
 # Para desafíos 1 y 2, cambie las instrucciones de conducción aquí drive_forward(Forward_Time) 
  
 # Si no hay suficiente luz, gira el rover
 else: 
 # Para desafío 5, podemos usar la función de temporizador para controlar la búsqueda de luz  Start_Time = time.time() 
 while not(GPIO.input(Photo_Pin)): 
 Elapsed_Time = round(time.time() - Start_Time,2) 
 print('Not enough light, searching for more') 
  
 if Elapsed_Time < Max_Search_Time: # Trate cambiando la declaración True a un comparativo (<) entre
 # Elapsed_Time y Max_Search_Time para desafío 5   
 if count % 2 == 0: # Trata cambiando el True declaración al módulo para desafío 4 
 drive_left_turn(Left_Turn_Time) 
sleep(Wait_Time) 
 else: # Para desafío 4, módulo usa estos mandatos de manejo en bucles impares 
 drive_right_turn(Right_Turn_Time) 
 sleep(Wait_Time) 
 else: 
 break # Salga del bucle después Max Search Time termina
