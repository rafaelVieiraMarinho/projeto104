import cv2

img = cv2.imread("./solar-system.jpg") 

#tarefa 5 projeto
#faça o nome de todos os planetas na imagem

cv2.putText(img,  
           "Sol",
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )

cv2.putText(img,  
           "terra",
           (300, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )


cv2.putText(img,  
           "saturno",
           (730, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.6,  
           color=(0,0,255)
           )
cv2.imshow("resultado",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)

#obs: FAÇA NO VSCODE