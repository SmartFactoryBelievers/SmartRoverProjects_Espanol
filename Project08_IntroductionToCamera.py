# Proyecto 08 
# Probando la cámara del Pi y aprender sobre las diferentes configuraciones de imagen # Construya el Proyecto 8 circuito y experimenta con la cámara
#Desafío 1 
# Trate de cambiar la resolución de la cámara al mínimo 64, 64 y vea cómo se ve la  imagen 
#Desafío 2 
# Trate de cambiar la resolución de la cámara al máximo 2592, 1944 y # el framerate a 15 y vea cómo se ve la imagen 
#Desafío 3 
# Trate de cambiar la rotación de la cámara para darle la vuelta (0) o izquierda o derecha (90, 2 70) 
#Desafío 4 
# Trate de agregar un texto en la parte superior de la imagen y cambia los colores y el tamaño 
#Desafío 5 
# Trate de ver todas las opciones de contraste y luminosidad
# y anotar la imagen con sus niveles actuales 
#Desafío 6 
# Haga el looping de todas las opctiones IMAGE_EFFECTS, EXPOSURE_MODES, y AWB_MODES # y anote la imagen con sus niveles actuales 
#Importing libraries 
# Aquí queremos sleep para el información de tiempo para la cámara del Pi from picamera import PiCamera, Color 
from time import sleep 
# Configuración de la cámara 
camera = PiCamera() 
# Cambiar el número de píxeles y la claridad de la cámara 
# Para desafío 1 y 2, vea cómo se ve la baja y la alta resolución camera.resolution = (2592, 1944) 
# Cambie la velocidad en que la cámara graba imágenes 
camera.framerate = 15 
# Rotar la imagen por x grados 
# Anote que la cámara está boca abajo, por que 180 grados es el lado derecho 
# Para desafío 3, prueba otros ángulos de rotación 
camera.rotation = 270
Copyright © Deloitte Development LLC 2022. All Rights Reserved. Developed in collaboration with the National Math + Science Initiative. 
# Para desafío 4, intenta anotar la imagen 
# Agregar texto encima de la imagen
camera.annotate_text = 'Hello World!' 
# Cambie el tamaño del texto en la parte superior de la imagen entre 6 y 160 
camera.annotate_text_size = 50 
# Cambie el color del texto de delante y de detrás 
camera.annotate_foreground = Color('red') 
camera.annotate_background = Color('blue') 
# Cambie el contraste entre 0 y 100
camera.contrast = 75 
# Cambie el luminosidad de la imagen entre 0 y 100
camera.brightness = 75 
# Para ver el flujo de imágenes de la cámara 
camera.start_preview() 
sleep(5) 
camera.stop_preview() 
# Para desafío 5, trate de iterar por los niveles de luminosidad en lugar de contraste camera.start_preview() 
for i in range(100): 
 camera.brightness = i 
 camera.annotate_text = '%s' %i 
 sleep(0.1) 
camera.stop_preview() 
# Para desafío 6, trate de iterar por IMAGE_EFFECTS, EXPOSURE_MODES, y AWB_MODES 
camera.start_preview() 
for effect in camera.EXPOSURE_MODES: 
 camera.annotate_text = '%s' %effect 
 camera.exposure_mode = effect 
 sleep(1) 
camera.stop_preview() 
camera.close()
