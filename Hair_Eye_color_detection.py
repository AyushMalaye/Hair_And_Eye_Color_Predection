# Importing Necessary Libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import random
import numpy
import numpy as np

# Loading the Model
from keras.models import load_model
model=load_model('Hair_eye_color_Detection.h5')

# Initializing the GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Hair And Eye Color Detection')
top.configure(background='#CDCDCD')

# Initializing the Labels (1 for age and 1 for Sex)
label1=Label(top,background="#CDCDCD",font=('arial',15,"bold"))
label2=Label(top,background="#CDCDCD",font=('arial',15,'bold'))
sign_image=Label(top)

# Definig Detect fuction which detects the age and gender of the person in image using the model
def Detect(file_path):
    global label_packed
    image=Image.open(file_path)
    image=image.resize((80,80))
    image=numpy.expand_dims(image,axis=0)
    image=np.array(image)
    image=np.delete(image,0,1)
    image=np.resize(image,(60,60,3))
    print (image.shape)
    hair_f=["Black", "Brown", "Blonde or Strawberry"," Gray or Partially Gray ","Red or Auburn", "Bald ","Not Available", "Salt and Pepper", "White", "Sandy", "Unknown"]
    eye_f =["Brown" , "Blue", "Hazel" ,"Green", "Black"," Not Available", "Gray", "Maroon", "Unknown"]
    image=np.array([image])/255
    pred=model.predict(image)
    eye=int(np.round(pred[1][0]))
    hair=int(np.round(pred[0][0]))
    # hair = random.randrange(0, 11)
    # eye = random.randrange(0, 8)
    print("Predicted eye color is "+ eye_f[eye])
    print("Predicted hair color is "+hair_f[hair])
    label1.configure(foreground="#011638",text=eye_f[eye])
    label2.configure(foreground="#011638",text=hair_f[hair])

# Defining Show_detect button function
def show_Detect_button(file_path):
    Detect_b=Button(top,text="Detect Image",command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background="#364156",foreground='white',font=('arial',10,'bold'))
    Detect_b.place(relx=0.79,rely=0.46)

# Definig Upload Image Function
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        show_Detect_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an Image",command=upload_image,padx=10,pady=5)
upload.configure(background="#364156",foreground='white',font=('arial',10,'bold'))
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand=True)
label1.pack(side="bottom",expand=True)
label2.pack(side="bottom",expand=True)
heading=Label(top,text="Hair And Color Detection",pady=20,font=('arial',20,"bold"))
heading.configure(background="#CDCDCD",foreground="#364156")
heading.pack()
top.mainloop()