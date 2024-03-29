import cv2

# Inicializando camera
camera = cv2.VideoCapture(0)
width = 640
height = 480

while True:

    # Capturando um quadro
    _, frame = camera.read()

    # Redimensionando o quadro
    resized_frame = cv2.resize(frame, (width, height))

    #Ajeitando as cores
    convert = cv2.cvtColor(resized_frame, cv2.COLOR_RGB2BGR)

    espelhada = cv2.flip(resized_frame, 1)

    # Exibindo (aparentemente vai direto para o pc)
    cv2.imshow('Camera', espelhada)

    # 'q' pra sair 
    if cv2.waitKey(1) == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
