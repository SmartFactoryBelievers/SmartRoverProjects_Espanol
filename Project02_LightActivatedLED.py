# Proyecto 2 
# Aprender a programar y utilizar entradas y salidas
# Construya el Proyecto 2 circuito y controle un LED con un botón 
#Desafío 1 
# Trate de cambiar las variables LED_On y LED_Off para cambiar el patrón de parpadeo 
#Desafío 2 
# Reemplace el LED de color con un zumbador o un LED blanco para probar otras salidas 
#Desafío 3 
# Reemplace el botón pulsador con el fototransistor y cúbrelo con la mano - ¿qué sucede? 
#Desafío 4 
# Trate de cambiar el "If" declaración de True a False - ahora que hace el botón? 
#Importing libraries 
# Aquí queremos la función sleep para el tiempo y GPIO para el pin de Pi from time import sleep 
import RPi.GPIO as GPIO 
#Definamos variables para poder usarlas más tarde
Button_Pin = 38 #el número de pin interno de Pi que se ajusta a 6 LED_Pin = 12 #el número de pin interno de Pi que se ajusta a 3
# Para desafío 1, podemos probar diferentes valores aquí para parpadear en nuevos patrones LED_On = 3 #duración de ED parpadea, segundos
LED_Off = 1 #duración entre parpadeas, segundos
#Configurando nuestros pines 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) #pin de salida, apagado GPIO.setup(Button_Pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pin de entrada, encendido
while True: #Bucle
  
 # Aquí usamos el condicional If que evalúa una expresión lógica  # Verificar si se pulsa el botón y leyendo ese valor del pin  # Si el pin del botón dice True (on), se ejecuta ese código
 if GPIO.input(Button_Pin) == False: #Cuando se presiona el botón, parpadea el LED
  sleep(LED_Off) #Deja LED apagado por un duración definida 
 GPIO.output(LED_Pin, GPIO.HIGH) #encender LED
 sleep(LED_On) #deja LED encendido por duración definida
 GPIO.output(LED_Pin, GPIO.LOW) #LED apagado
 
 # Si no se presiona el botón, el código irá a la instrucción else  
else: 
 print('Button not pressed') 
 sleep(1)
