# Proyecto 1
# Aprendiendo a programar y usar salidas
# Construye el Proyecto 1 circuito y parpadea un LED
#Desafío 1 
# Trata de cambiar las variables LED_On y LED_Off para cambiar el patrón
#Desafío 2
# Reemplace el LED de color con un timbre o un LED blanco para probar otras salidas 
#Importing libraries 
# Son conjuntos definidos de código para usos específicos
# Aquí queremos la función sleep para el tiempo y GPIO para el pin de Pi from time import sleep 
import RPi.GPIO as GPIO 
#Definamos variables para poder usarlas más tarde
# Las variables son palabras que toman valores dentro del código
# De esta manera, podemos editar el valor al principio y los cambios fluirán por LED_Pin = 40 #el número de pin interno de Pi que se ajusta a 7 
# Para el desafío 1, podemos probar diferentes valores aquí para parpadear en nuevos patrones 
LED_On = 3 #duración de LED parpadea, segundos
LED_Off = 1 #duración entre parpadeas, segundos
#Configurando nuestro pin 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(LED_Pin, GPIO.OUT, initial=GPIO.LOW) #Pin de salida, empezar apagado
while True: #Bucle
 sleep(LED_Off) #Deja LED apagado por un duración definida 
 GPIO.output(LED_Pin, GPIO.HIGH) #encender LED
 sleep(LED_On) #Deja LED encendida por un duración definida 
 GPIO.output(LED_Pin, GPIO.LOW) #LED apagado
