import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import Image
import cv2
import pyzbar.pyzbar as zbar
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
tkWindow = Tk()
tkWindow.geometry('400x400')
tkWindow.title('Scan QR ID ')
def scanqr():
   stopped = False
   delay = 1
   while (True):
       ret = cv2.waitKey(20) & 0xFF
       if ret == ord('c'):  # continue
           stopped = False
           delay = 1
       if ret == ord('q'):
           break
       if stopped or (ret == ord('s')):  # stop
           stopped = True
           delay = 30
           continue
       # Capture frame-by-frame
       ret, frame = cap.read()
       decodedObjects = zbar.decode(frame)
       if len(decodedObjects) > 0:
           stopped = True
           y = 50
           for obj in decodedObjects:
               # print("Data", obj.data)
               print(obj.data.decode("utf-8"))
               cv2.putText(frame, obj.data.decode("utf-8"), (50, y), font, 2, (255, 0, 0), 3)
               y += 50

       # Display the resulting frame
       cv2.imshow('frame', frame)
# When everything done, release the capture
button = Button(tkWindow,
               text='Scan Now',
               command=scanqr)
title=tkinter.Label(tkWindow,text="Hierank Business School",font=('bold',22))
title.pack()
canvas= Canvas(tkWindow, width= 300, height= 205)
canvas.pack()
hie=(Image.open('hie.png'))
#Load an image in the script
img= (Image.open("hie.png",))
#Resize the Image using resize method
resized_image= img.resize((250,200), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)
button.pack()
title.pack()
tkWindow.mainloop()
cap.release()
cv2.destroyAllWindows()
