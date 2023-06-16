import cv2

# Le imagem do arquivo
image = cv2.imread('../img/dinho.jpg')

# Rotaciona a imagem em 90 graus
rotated_dinho= cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
#dinho2= cv2.rotate(image, 45)

# Espelha a imagem horizontalmente
flipped_dinho = cv2.flip(image, 1)

#cv2.imshow('Dinho', image)
cv2.imshow('Rotated Dinho', rotated_dinho)
#cv2.imshow('Rotacion Dinho', dinho2)
cv2.imshow('Flipped Dinho', flipped_dinho)

cv2.waitKey(0)
cv2.destroyAllWindows()