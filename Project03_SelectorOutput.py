# Proyecto 3 
# Aprendiendo a programar, escribir funciones y usar entradas y salidas 
# Construya el Proyecto 3 circuito y control de un LED y un zumbador con un selector # Mantenga presión en los botones A, B y C en el selector 
#Desafío 1 
# Trate de cambiar las variables Pin_On y Pin_Off para cambiar el patrón de parpadeo 
#Desafío 2 
# Reemplace el LED de color con un zumbador o un LED blanco para probar otras salidas 
#Desafío 3 
# Trate de cambiar los pines de entrada A y C en el ciclo While para cambiar lo que hacen A y C cuando se presionan 
#Desafío 4 
# Trate de cambiar los pines de salida LED y zumbador en el ciclo While para cambiar lo que hacen A y C cuando se presionan
#Desafío 5
# Trate de cambiar el orden de las funciones LED y zumbador para un espectáculo de luces cuando presionas B
#Importing libraries 
# Aquí queremos la función sleep para el tiempo y GPIO para el pin de Pi from time import sleep 
import RPi.GPIO as GPIO 
#Definamos variables para poder usarlas más tarde 
A_Pin = 40 #el número de pin interno de Pi que se ajusta a 7 
C_Pin = 38 #el número de pin interno de Pi que se ajusta a 6 
LED_Pin = 12 #el número de pin interno de Pi que se ajusta a 3
Buzzer_Pin = 35 #el número de pin interno de Pi que se ajusta a 4 
# Para desafío 1, podemos probar diferentes valores aquí para parpadear en nuevos patrones Pin_On = 3 #duración del LED parpadea, segundos 
Pin_Off = 0.5 #duración entre parpadeas, segundos 
#Configurando nuestros pines
GPIO.setmode(GPIO.BOARD) 
#Nuestros pines de salida, comenzar apagados
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(Buzzer_Pin, GPIO.OUT, initial=GPIO.LOW) 
#Nuestros pines de entrada del selector 
GPIO.setup(A_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
GPIO.setup(C_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
#Escribamos algunas funciones que podamos usar para facilitar la codificación # Para un fragmento de código que utilizaremos, podemos convertirlo en una función para llamarlo más tarde # El nombre de la función está en azul, y luego los argumentos que toma están entre paréntesis 
#Aquí hay una función para ver si se presiona el botón 
# read_selector_button lee y devuelve el valor de In_Pin # Esto será útil para leer los pines de los botones A y C.
def read_selector_button(In_Pin): 
 return GPIO.input(In_Pin) 
#Aquí hay una función para encender un pin de salida
#output_pin_on toma el número pin y lo enciende después de un retraso definido def output_pin_on(Out_Pin, Delay): 
 sleep(Delay) 
 GPIO.output(Out_Pin, GPIO.HIGH) 
  
#Aquí hay una función para apagar un pin de salida, ¿puede completar las piezas que faltan? # Reemplace la ?? con las variables y luego un comment
def output_pin_off(Out_Pin, Delay): 
 sleep(Delay) #espera el retraso 
 GPIO.output(Out_Pin, GPIO.LOW) #apaga Out_Pin
while True: #Bucle
  
 # Aquí podemos usar las funciones que definimos para leer botones y controlar salidas  # Para los desafíos, trate de cambiar el botón y los pines de salida en el siguiente código   
 # Si se presiona A y no se presiona C, parpadear el LED
 if read_selector_button(A_Pin) and not(read_selector_button(C_Pin)):  output_pin_on(LED_Pin, Pin_Off) 
 output_pin_off(LED_Pin, Pin_On) 
  
 # Si se presiona C y no se presiona A, suena el zumbador 
 if read_selector_button(C_Pin) and not(read_selector_button(A_Pin)):  output_pin_on(Buzzer_Pin, Pin_Off) 
 output_pin_off(Buzzer_Pin, Pin_On) 
  
 # Si se presionan A y C por presionando B, ¿Podemos parpadear el zumbador y el LED al mismo tiempo?
 # Reemplace la ?? con los LED_Pin y Buzzer_Pin variables y luego uncomment  if read_selector_button(A_Pin) and read_selector_button(C_Pin):  output_pin_on(LED_Pin, Pin_Off) 
 output_pin_off(Buzzer_Pin, Pin_On) 
 output_pin_on(LED_Pin, Pin_Off) 
 output_pin_off(Buzzer_Pin, Pin_On) 
  
 # Espere 1 segundo para restablecer
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
 sleep(1)   
