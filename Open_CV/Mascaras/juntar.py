import cv2

# Le imagem do arquivo
dinho = cv2.imread('../img/dinho.jpg')
leo = cv2.imread('../img/messi.jpg')

hang_loose = dinho[366:510, 361:473]
flipped_hang = cv2.flip(hang_loose, 1)
leo_face = cv2.resize(leo[30:343, 119:327], None, fx=0.33, fy=0.33)
dinho[366:510, 361:473] = flipped_hang
dinho[411-102:412, 697-68:698] = leo_face
gaussian_dinho = cv2.GaussianBlur(dinho, (3, 3), 0)
gray_dinho = cv2.cvtColor(gaussian_dinho, cv2.COLOR_BGR2GRAY)
edges_dinho = cv2.Canny(gray_dinho, 200, 200)

cv2.imshow('Dinho', edges_dinho)
cv2.imwrite('../img/new_dinho.jpg', edges_dinho)
cv2.waitKey(0)
cv2.destroyAllWindows()