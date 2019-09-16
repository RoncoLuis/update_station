import cv2
#Script de prueba para usar la libreria de open-cv
"""
img = cv2.imread('../img/p001_qr-code.png') #el segundo argumente 0=gris,1=color
print(img)

cv2.imshow('qr-image',img)
cv2.waitKey(0) #seg. para cerrar la ventana. En cero no se cierra
cv2.destroyAllWindows()

"""
#probando camara web
cam = cv2.VideoCapture(1) #0 es la camara por default

while(True):
    ret,frame = cam.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()