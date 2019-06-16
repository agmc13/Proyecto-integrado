#!C:\Users\Alfonso\python37\python.exe
print("Content-Type: text/html\n")
import numpy as np
import cv2

counter = 0
width = 800

def testIntersectionIn(x, y):

    res = -450 * x + 400 * y + 157500
    if((res >= -550) and  (res < 550)):
        print (str(res))
        return True
    return False

def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        pad_w, pad_h = int(0.15*w), int(0.05*h)
		# Aqui se crea la forma que va a tener el rectangulo que saldra cuando se detecte a una persona.
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (10, 10, 200), 2)


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
        found,w=hog.detectMultiScale(frame, winStride=(2, 2),padding=(4, 4), scale=100)
		#si encuentra algo coincidente hara el dibujo del rectangulo.
        draw_detections(frame,found)
        
		# con imshow mostrará la ventana de la imagen que se esta emitiendo.
        cv2.imshow('reconocimiento',frame)

        if(draw_detections(frame,found)):
            counter += 1
           
        cv2.putText(frame, "In: {}".format(str(counter)), (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        print(counter)
        #por ahora al pulsar la tecla "q" finalizara el programa.
        k = 0xFF & cv2.waitKey(1)
        if k == ord('q'):
            break
    cv2.destroyAllWindows()