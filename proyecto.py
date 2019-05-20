import numpy as np
import cv2


def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh


def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        pad_w, pad_h = int(0.15*w), int(0.05*h)
		# Aqui se crea la forma que va a tener el rectangulo que saldra cuando se detecte a una persona.
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 0, 255), 2)


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
		#por ahora al pulsar la tecla "q" finalizara el programa.
        k = 0xFF & cv2.waitKey(1)
        if k == ord('q'):
            break
    cv2.destroyAllWindows()