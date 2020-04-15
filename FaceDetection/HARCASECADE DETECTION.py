

import cv2
import smtplib
cap = cv2.VideoCapture('http://192.168.43.246:8080/video')
face_model = cv2.CascadeClassifier('frontalface_harscascade.xml')

while True:
    status , photo = cap.read()
    face_cor = face_model.detectMultiScale(photo)
    if len(face_cor) == 0:
        pass
    else:   
        x1  = face_cor[0][0]
        y1 = face_cor[0][1]
        x2 = x1 + face_cor[0][2]
        y2 = y1 + face_cor[0][3]

        photo = cv2.rectangle(photo , (x1,  y1) , (x2, y2), [0,255,0], 3)
        photo = cv2.putText(photo,str(len(face_cor)),(50, 50), cv2.FONT_HERSHEY_SIMPLEX,1,(255, 0, 0),3,cv2.LINE_AA)
        
       
        cv2.imshow('photo' , photo)
        if cv2.waitKey(10) == 13:
            break
    
    
    
cv2.destroyAllWindows()
cap.release()

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo() #setting up the connection with server 
    smtp.starttls() # encrypting the traffice 
    smtp.ehlo()
    #use your email id and password 
    #can also be stored in env variables and access from there
    smtp.login('senderemailid','password')
    subject = 'Attendance'
    body = 'Strength  of Class : '+str(len(face_cor))
    
    msg= f'Subject:{subject}\n\n{body}'
        
    smtp.sendmail('senderemailid','recieveremailid',msg)






