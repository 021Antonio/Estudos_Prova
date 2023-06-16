import cv2

# Le imagem do arquivo
image = cv2.imread('../img/dinho.jpg')

# Aplicando um filtro gaussiano com kernel 7x7
gaussian_dinho = cv2.GaussianBlur(image, (7, 7), 0)

# Aplicando um filtro de mediana com kernel 7x7
median_dinho = cv2.medianBlur(image, 7)

cv2.imshow('Dinho', image)
cv2.imshow('Gaussian Dinho', gaussian_dinho)
cv2.imshow('Median Dinho', median_dinho)
cv2.waitKey(0)
cv2.destroyAllWindows()