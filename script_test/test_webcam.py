import cv2

def show_webcam(mirror=False):
    camera = cv2.VideoCapture(1)#0 es la camara por default
    while True:
        return_value,img = camera.read()
        if mirror:
            img = cv2.flip(img,1)
            cv2.imshow('Webcam',img)
            if cv2.waitKey(1) == 27:
                break
    cv2.destroyAllWindows()

    def main():
        show_webcam(mirror=True)

    if __name__ == '__main__':
        main()