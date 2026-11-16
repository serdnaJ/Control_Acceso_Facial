import cv2
import serial
import time


puerto_arduino = 'COM8' 
arduino = serial.Serial(puerto_arduino, 9600, timeout=1)
time.sleep(2) 


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

estado_anterior = None

print("Iniciando sistema de control de acceso... Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al acceder a la cámara.")
        break

   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    rostros = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(30, 30)
    )

    if len(rostros) > 0:
        
        for (x, y, w, h) in rostros:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        if estado_anterior != '1':
            print("acceso correcto")
            arduino.write(b'1') 
            estado_anterior = '1'
    else:
        if estado_anterior != '0':
            print("acceso denegado")
            arduino.write(b'0') 
            estado_anterior = '0'

    
    cv2.imshow('Control de Acceso Domotico Bancario', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


arduino.write(b'0')
cap.release()
cv2.destroyAllWindows()
arduino.close()