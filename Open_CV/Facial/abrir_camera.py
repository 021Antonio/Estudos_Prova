import cv2

def exibir_video_camera():
    # Inicializar o objeto de captura de vídeo
    cap = cv2.VideoCapture(0)  # 0 representa a câmera padrão, mas pode ser alterado para outras câmeras

    while True:
        # Ler um frame do vídeo
        ret, frame = cap.read()

        # Verificar se o frame foi lido corretamente
        if not ret:
            print("Erro ao ler o frame")
            break

        # Exibir o frame em uma janela chamada "Video"
        cv2.imshow("Video", frame)

        key = cv2.waitKey(1)
        
        if key == 27:
            print("Saindo")
            break
        

    # Liberar o objeto de captura de vídeo e fechar as janelas
    cap.release()
    cv2.destroyAllWindows()

# Chamar a função para exibir o vídeo da câmera
exibir_video_camera()
