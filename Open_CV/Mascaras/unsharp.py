import cv2
import numpy as np

# Le imagem do arquivo
image = cv2.imread('../img/dinho.jpg')

# Definindo um kernel customizado
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], dtype=np.float32)

# Aplicando a convolução
filtered_dinho = cv2.filter2D(image, -1, kernel)

# Display the original and filtered images
cv2.imshow('Dinho', image)
cv2.imshow('Filtered Dinho', filtered_dinho)
cv2.waitKey(0)
cv2.destroyAllWindows()