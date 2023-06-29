# Proyecto 4 
# Aprender a programar, escribir funciones y usar salidas
# Construya el Proyecto 4 circuito y conducir el rover en su ruta diseñada 
#Desafío 1 
# Trate de cambiar la variable de tiempo para crear una nueva ruta de conducción
#Desafío 2 
# Reordenar las funciones de conducción para crear una nueva ruta de conducción 
#Desafío 3 
# Cree su propia ruta de conducción personalizada utilizando las diferentes funciones de conducción y argumentos de tiempo
#Importing libraries 
# Aquí queremos la función sleep para el tiempo y GPIO para el pin de Pi from time import sleep 
import RPi.GPIO as GPIO 
#Definamos variables para poder usarlas más tarde 
Left_Forward_Pin = 36 #el número de pin interno de Pi que se ajusta a 1 Left_Backward_Pin = 11 #el número de pin interno de Pi que se ajusta a 2 Right_Forward_Pin = 12 #el número de pin interno de Pi que se ajusta a 3 Right_Backward_Pin = 35 #el número de pin interno de Pi que se ajusta a 4 
#Aquí podemos definir las variables de tiempo para las funciones de conducción, en segundos # Para desafío 1, podemos probar diferentes valores aquí para conducir nuevos patrones Forward_Time = 2 
Backward_Time = 1 
Left_Turn_Time = 0.5 
Right_Turn_Time = 0.5 
Wait_Time = 1 
#Configurando nuestros pines 
GPIO.setmode(GPIO.BOARD) 
#Nuestros pines de salida, empieza apagado 
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) 
#Escribamos algunas funciones de conducción que podemos usar más tarde para programar una ruta de conducción. def drive_forward(time):  
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierda adelante  
GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Motor derecho adelante  sleep(time)
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
 GPIO.output(Left_Forward_Pin, GPIO.LOW) #motor izquierdo apagado 
 GPIO.output(Right_Forward_Pin, GPIO.LOW) #motor derecho apagado 
 print('forward') 
 sleep(1) 
def drive_left_turn(time): 
 GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Motor izquierdo hacia atrás  
GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Motor derecho adelante   sleep(time) 
 GPIO.output(Left_Backward_Pin, GPIO.LOW) #motor izquierdo apagado 
 GPIO.output(Right_Forward_Pin, GPIO.LOW) #motor derecho apagado 
 print('left turn') 
 sleep(1) 
  
def drive_right_turn(time): 
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierdo adelante  GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Motor derecho hacia atrás  sleep(time) 
 GPIO.output(Left_Forward_Pin, GPIO.LOW) #motor izquierdo apagado 
 GPIO.output(Right_Backward_Pin, GPIO.LOW) #motor derecho apagado
 print('right turn') 
 sleep(1) 
  
# ¿Puede terminar la función para los pines y estados? # Esta es una función de conducción hacia atrás, los dos pines hacia atrás deben ser Altos y después Bajos # Uncomment el código cuando está completo 
def drive_backward(time): 
 GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Motor izquierdo hacia atrás  GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Motor derecho hacia atrás  sleep(time) 
 GPIO.output(Left_Backward_Pin, GPIO.LOW) #motor izquierdo apagado  
 GPIO.output(Right_Backward_Pin, GPIO.LOW) #motor derecho apagado 
 print('backward') 
 sleep(1) 
#Aquí podemos usar un bucle for para controlar la cantidad de veces que se ejecuta el código # Cambiando el valor de range() aumenta el número de bucles realizados for n in range(1): 
  
 # Usamos las funciones de conducción definidas anteriormente para crear una ruta de conducción  # Para desafíos 2 y 3, trata a cambiar las funciones de conducción y orden aquí  sleep(Wait_Time) 
 drive_forward(Forward_Time) 
 drive_left_turn(Left_Turn_Time) 
 drive_backward(Backward_Time) 
 drive_right_turn(Right_Turn_Time)
