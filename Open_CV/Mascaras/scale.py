import cv2

# Le imagem do arquivo
image = cv2.imread('../img/dinho.jpg')

# Redimensiona a imagem com altura e largura especificas
resized_dinho = cv2.resize(image, (400, 300))

# Redimensiona a imagem em uma escala 1/2
scaled_dinho = cv2.resize(image, None, fx=0.5, fy=0.5)

cv2.imshow('Dinho', image)
cv2.imshow('Resized Dinho', resized_dinho)
cv2.imshow('Scaled Dinho', scaled_dinho)
cv2.waitKey(0)
cv2.destroyAllWindows()