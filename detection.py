import cv2.data
import cv2
import keras._tf_keras.keras.models as models
from keras._tf_keras.keras.models import model_from_json, Sequential, Model
import numpy as np
import webbrowser  
import pyautogui
import time
import psutil

json_file = open("newemotion.json", "r")
model_json = json_file.read()
json_file.close()
model = models.model_from_json(model_json)


model.load_weights("newemotion.weights.h5")

haar_file=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

face_cascade=cv2.CascadeClassifier(haar_file)

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1,48,48,1)
    return feature/255.0

webcam=cv2.VideoCapture(0)
labels = ['angry', 'happy', 'neutral', 'sad']
wait = 0
while cv2.waitKey(100) != ord(' '):
    i,im=webcam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(im,1.3,5)
    try: 
        for (p,q,r,s) in faces:
            image = gray[q:q+s,p:p+r]
            cv2.rectangle(im,(p,q),(p+r,q+s),(255,255,0),2)
            image = cv2.resize(image,(48,48))
            img = extract_features(image)
            pred = model.predict(img)
            prediction_label = labels[pred.argmax()]
          
            cv2.putText(im, 'You are % s' %(prediction_label), (p-120, q-10),cv2.FONT_HERSHEY_SIMPLEX,2, (0,0,0),3)
            cv2.putText(im, '        Press space ', (p-120, q+r+30),cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,0),3)
            cv2.putText(im, '       for the playlist ' , (p-120, q+r+70),cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,0),3)
        cv2.imshow("Emotify",im)
       
            
            


    except cv2.error:
        pass

webcam.release()
cv2.destroyAllWindows()



Chrome = webbrowser.Chrome

url=' '
if prediction_label== 'angry':
    url = 'https://open.spotify.com/playlist/37i9dQZF1EIgNZCaOGb0Mi?si=601a23872ba9495b'
    webbrowser.open_new_tab(url)
if prediction_label=='happy':
    url= 'https://open.spotify.com/playlist/37i9dQZF1EVJSvZp5AOML2?si=347e46d5bcf24ee4'
    webbrowser.open_new_tab(url)
if prediction_label=='neutral':
    url= 'https://open.spotify.com/playlist/37i9dQZF1EVHGWrwldPRtj?si=1f640c1687b74ea7'
    webbrowser.open_new_tab(url)
if prediction_label=='sad':
    url= 'https://open.spotify.com/playlist/37i9dQZF1DXbrUpGvoi3TS?si=b2827cdca12a44a0'
    webbrowser.open_new_tab(url)


program_name = 'Spotify.exe'

timeout = time.time() + 90

while True:


    for process in psutil.process_iter():

        try:

            if process.name() == program_name:
                time.sleep(2)  # Wait for Spotify to load
                pyautogui.moveTo(490,538)
                pyautogui.click()
                
                break

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):

            pass

    else:

        # If the program is not open, check if we have timed out

        if time.time() > timeout:

            print("Timed out!")

            break

        else:


            time.sleep(1)

            continue


    

    break





