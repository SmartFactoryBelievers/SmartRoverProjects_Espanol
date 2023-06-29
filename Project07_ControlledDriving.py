# Proyecto 7 
# Aprender a programar, escribir funciones, usar salidas de control de motor y agregar lógica compleja
# Construya el Proyecto 7 circuito y conducir el móvil presionando los botones A, B y C   
# ¿Establecer los controles para el rover para 3 mandatos y posiblemente más? 
#Desafío 1 
# Trate de cambiar las funciones de conducción para cambiar las direcciones de conducción para avanzar, mover hacia atrás o girar
#Desafío 2 
# Agregue nuevas funciones de conducción para cambiar los patrones de conducción para cada pulsación de botón 
#Desafío 3 
# Use un temporizador de pulsación de botón de proyecto 5 para agregar el Simon Says funciones de conducción 
#Desafío 4 
# ¿Ve cómo B usa un doble If para ver si se presiona y luego se suelta o se mantiene? 
# Puede intentar algo similar para A y C para crear diferentes comandos allí también? 
#Desafío 5 
# Reemplace la longitud 
3 conectores con el fototransistor - ahora los tres botones son dependientes de la luz. Trata a controlar el rover para permanecer en la luz. 
#Importing libraries 
# Aquí queremos la función sleep para el tiempo y GPIO para el pin de Pi import time 
from time import sleep 
import RPi.GPIO as GPIO 
#Definamos variables para poder usarlas más tarde 
Left_Forward_Pin = 36 #el número de pin interno de Pi que se ajusta a 1 Left_Backward_Pin = 11 #el número de pin interno de Pi que se ajusta a 2 Right_Forward_Pin = 12 #el número de pin interno de Pi que se ajusta a 3 Right_Backward_Pin = 35 #el número de pin interno de Pi que se ajusta a 4 A_Pin = 40 #el número de pin interno de Pi que se ajusta a 7 
C_Pin = 38 #el número de pin interno de Pi que se ajusta a 6 
#Aquí podemos definir las variables de tiempo para las funciones de conducción, en segundos Forward_Time = 2 
Backward_Time = 1 
Left_Turn_Time = 0.5 
Right_Turn_Time = 0.5
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
Wait_Time = 0.5 
#Configurando nuestros pines 
GPIO.setmode(GPIO.BOARD) 
#Nuestros pines de salida, empiezan apagado 
GPIO.setup(Left_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Left_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Right_Forward_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Right_Backward_Pin, GPIO.OUT, initial=GPIO.LOW) 
#Nuestro pin de entrada desde el botón 
GPIO.setup(A_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(C_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
#Escribamos algunas funciones de conducción que podamos usar más tarde para programar un pathdef drive_forwa rd(): 
def drive_forward(time):  
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierdo adelante 
 GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Motor derecho adelante 
 sleep(time) 
 GPIO.output(Left_Forward_Pin, GPIO.LOW) #Motor izquierdo adelante 
 GPIO.output(Right_Forward_Pin, GPIO.LOW) #Motor derecho adelante 
 print('fwd') 
 sleep(1) 
def drive_backward(time): 
 GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Motor izquierdo hacia atrás 
 GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Motor derecho hacia atrás 
 sleep(time) 
 GPIO.output(Left_Backward_Pin, GPIO.LOW) #Motor izquierdo hacia atrás 
 GPIO.output(Right_Backward_Pin, GPIO.LOW) #Motor derecho hacia atrás 
 print('bkwd') 
 sleep(1) 
def drive_left_turn(time): 
 GPIO.output(Left_Backward_Pin, GPIO.HIGH) #Motor izquierdo hacia atrás 
 GPIO.output(Right_Forward_Pin, GPIO.HIGH) #Motor derecho adelante 
 sleep(time) 
 GPIO.output(Left_Backward_Pin, GPIO.LOW) #Motor izquierdo hacia atrás 
 GPIO.output(Right_Forward_Pin, GPIO.LOW) #Motor derecho adelante 
 print('left turn') 
 sleep(1) 
  
def drive_right_turn(time): 
 GPIO.output(Left_Forward_Pin, GPIO.HIGH) #Motor izquierdo hacia atrás 
 GPIO.output(Right_Backward_Pin, GPIO.HIGH) #Motor derecho adelante 
 sleep(time) 
 GPIO.output(Left_Forward_Pin, GPIO.LOW) #Motor izquierdo hacia atrás
 GPIO.output(Right_Backward_Pin, GPIO.LOW) #Motor derecho adelante
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
 print('right turn') 
 sleep(1) 
  
# Aquí estamos creando una función de temporizador para registrar la duración de la pulsación del botón def button_press_timer(): 
 Start_Time = time.time() #empieza el temporizador  
 while GPIO.input(Button_Pin): #mientras se presiona el botón...  print("Button Pressed") 
 return round(time.time() - Start_Time,2) #para el temporizador # Para desafío 3, trata uncommenting los Press_Time declaraciones, y úsalo para los mandatos de conducción 
while True: #Bucle 
 sleep(0.5) 
  
 # Solo presionando A 
 if GPIO.input(A_Pin) and not GPIO.input(C_Pin): #Solo presionando A  # Para desafío 4, puede usar sleep delay y segundo if, else para ver si A fue presionado y soltado o retenido   
 sleep(0.5) 
 #Presione B y mantenga presion, verifique si todavía está presionado después del delay
 if GPIO.input(A_Pin) and not GPIO.input(A_Pin): 
 drive_forward(Forward_Time) 
 drive_backward(Backward_Time) 
 else: 
 Press_Time = button_press_timer(A_Pin) # Para desafío 3  drive_forward(Forward_Time) 
  
 # Solo presionando C 
 if GPIO.input(C_Pin) and not GPIO.input(A_Pin): #solo presionando C # Para desafío 4, puede usar sleep delay y segundo if, else para ver si C fue presionado y soltado o retenido   
  
 Press_Time = button_press_timer(C_Pin) # Para desafío 3   drive_backward(Backward_Time) 
  
 # Presionando B, podemos usar el tiempo para determinar si suelta o se mantiene presión  if GPIO.input(C_Pin) and GPIO.input(A_Pin): 
 sleep(0.5) 
 #Presione B y mantenga presion, verifique si todavía está presionado después del delay  if GPIO.input(C_Pin) and GPIO.input(A_Pin): 
 drive_left_turn(Left_Turn_Time) 
 # Presione B y mantenga presion, verifique que no está presionado después del delay  else: 
 drive_right_turn(Right_Turn_Time)
