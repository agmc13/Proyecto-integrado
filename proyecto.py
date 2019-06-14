#Librerias necesarias para telegram.
import requests
import time
#Librerias necesarias para el reconocimiento de personas.
import numpy as np
import cv2

#inicializar variable contador.
counter = 0
#inicializar variable cuenta atras.
countdown = 0
#token del bot creado para telegram.
token = "769477933:AAF3F2QgyTIvGpz_EUAwREhwbwoYtsIB3JQ"
#ID del grupo de telegram.
ID_canal= "-350293082"

def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        pad_w, pad_h = int(0.15*w), int(0.05*h)
		# Aqui se crea la forma que va a tener el rectangulo que saldra cuando se detecte a una persona.
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 0, 255), 2)
        return True


if __name__ == '__main__':
	#Creamos la variable de HOG que se encargan de detectar objetos  que ente caso seran personas. 
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
	#Se captura el primer fotograma de la camara para que sirva de referencia.
    cap=cv2.VideoCapture(0)

    while True:
		#se empieza a capturar la imagen de la camara.
        _,frame=cap.read()

		#aqui buscara a traves de los datos de la escala dados a una persona.
        found,w=hog.detectMultiScale(frame, winStride=(4, 4),padding=(8, 8), scale=1)
		#si encuentra algo coincidente hara el dibujo del rectangulo.
        draw_detections(frame,found)
        
		# con imshow mostrará la ventana de la imagen que se esta emitiendo.
        cv2.imshow('reconocimiento',frame)

        if(draw_detections(frame,found) == True):
            counter += 1

        print(counter)
        #Al pulsar la tecla "q" finalizara el programa.
        k = 0xFF & cv2.waitKey(1)
        if k == ord('q'):
            break

        #Bucle if para que cuando el contador llegue a 10 envie un mensaje de texto por telegram.
        if (counter > 5):
            r = requests.post('https://api.telegram.org/bot'+ token +'/sendMessage',
              data={'chat_id': ID_canal, 'text': 'conflicto en el area del recreo a las '+ time.strftime("%I:%M:%S")+ ' horas' })
            print(r.text)
            counter = 0

        #bucle if para reiniciar cada 10 segundos la variable counter.
        if (countdown < 7):
            countdown +=1
        else:
            counter = 0
            countdown = 0

    cv2.destroyAllWindows()