# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:21:04 2019

@author: Ayush Jain
"""
import numpy as np
import pandas as pd
import pickle

dataset=pd.read_csv("final.csv")
X=dataset.iloc[:,[0,1,3,4,5,6,8,9]].values
Y=dataset.iloc[:,10].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelen1=LabelEncoder()
labelen2=LabelEncoder()
labelen3=LabelEncoder()

X[:,1]=labelen1.fit_transform(X[:,1])
X[:,2]=labelen2.fit_transform(X[:,2])
X[:,3]=labelen3.fit_transform(X[:,3])

filename = 'randomforestmodel.sav'
loaded_model = pickle.load(open(filename, 'rb'))



HEIGHT=600
WIDTH=900

def show_entry_fields():
   #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   t1=str(e1.get())
   t2=str(e2.get())
   t3=str(e3.get())
   t4=str(e4.get())
   t5=str(e5.get())
   t6=str(e6.get())
   t7=str(e7.get())
   t8=str(e8.get())
   
   list1=[]
   list1.append(float(t4))#4
   list1.append(t3)#3
   list1.append(t2)#2
   list1.append(t1)#1
   list1.append(float(t5))
   list1.append(float(t6))
   list1.append(float(t7))
   list1.append(float(t8))
   
   
   list1[1]=labelen1.transform(list1[1])
   list1[2]=labelen2.transform(list1[2])
   list1[3]=labelen3.transform(list1[3])
   list1=np.array(list1)
   list1=np.reshape(list1,(1,list1.shape[0]))
   output1=loaded_model.predict(list1)
   
   if(output1[0]==1):
       label1['bg']="RED"
       label1['text']="WARNING : DROUGHT"
       label1.place(relwidth=1,relheight=0.3)
       
       label2=tk.Label(lower_frame,font=15,anchor="w")
       label2['text']="+Never pour water down the drain when there may be another use for it."
       label2.place(rely=0.42,relwidth=1,relheight=0.1)


       label3=tk.Label(lower_frame,font=15,anchor="w")
       label3['text']="+Choose appliances that are more water and energy efficient."
       label3.place(rely=0.52,relwidth=1,relheight=0.1)

       label4=tk.Label(lower_frame,font=15,anchor="w",justify="left")
       label4['text']="+Check your well pump periodically. If the automatic pump turns on and off while water is not \n being used, you may have a leak."
       label4.place(rely=0.62,relwidth=1,relheight=0.2)

       label5=tk.Label(lower_frame,font=15,anchor="w",justify="left")
       label5['text']="+Consider using rainwater collection systems to water plants and gardens."
       label5.place(rely=0.80,relwidth=1,relheight=0.2)
       
   else:
       label1['bg']="BLUE"
       label1['text']="YOU ARE SAFE"
       label1.place(relwidth=1,relheight=0.3)
       
       label2=tk.Label(lower_frame,font=15,anchor="w")
       label2['text']=""
       label2.place(rely=0.42,relwidth=1,relheight=0.1)


       label3=tk.Label(lower_frame,font=15,anchor="w")
       label3['text']=""
       label3.place(rely=0.52,relwidth=1,relheight=0.1)

       label4=tk.Label(lower_frame,font=15,anchor="w",justify="left")
       label4['text']=""
       label4.place(rely=0.62,relwidth=1,relheight=0.2)

       label5=tk.Label(lower_frame,font=15,anchor="w",justify="left")
       label5['text']=""
       label5.place(rely=0.80,relwidth=1,relheight=0.2)

     
   
 
import tkinter as tk


   
root=tk.Tk()

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

Bimg=tk.PhotoImage(file="landscape.png")
Blable=tk.Label(root,image=Bimg)
Blable.place(relwidth=1,relheight=1)
                
                
frame=tk.Frame(root,bg="#80c1ff",bd=5)
frame.place(relx=0.5,rely=0.05,relwidth=0.8,relheight=0.5,anchor='n')

"""entry=tk.Entry(frame)
entry.place(relwidth=0.5,relheight=0.1)
"""
e1=tk.Entry(frame)
e1.place(relwidth=0.5,relheight=0.1)
label=tk.Label(frame,text="STATE",bg="#80c1ff",font=18)
label.place(relx=0.6,relwidth=0.4,relheight=0.1)

e2=tk.Entry(frame)
e2.place(rely=0.11,relwidth=0.5,relheight=0.1)
label=tk.Label(frame,text="DISTRICT",bg="#80c1ff",font=18)
label.place(rely=0.11,relx=0.6,relwidth=0.4,relheight=0.1
            )
e3=tk.Entry(frame)
e3.place(rely=0.22,relwidth=0.5,relheight=0.1)
label=tk.Label(frame,text="MONTH",bg="#80c1ff",font=18)
label.place(rely=0.22,relx=0.6,relwidth=0.4,relheight=0.1)

e4=tk.Entry(frame)
e4.place(rely=0.33,relwidth=0.5,relheight=0.1)
label=tk.Label(frame,text="AVERAGE TEMPERATURE",bg="#80c1ff",font=18)
label.place(rely=0.33,relx=0.6,relwidth=0.4,relheight=0.1)

e5=tk.Entry(frame)
e5.place(rely=0.44,relwidth=0.5,relheight=0.1)
label=tk.Label(frame,text="POTENTIAL EVAPOTRANSPIRATION",bg="#80c1ff",font=18)
label.place(rely=0.44,relx=0.6,relwidth=0.4,relheight=0.1)

e6=tk.Entry(frame)
e6.place(rely=0.55,relwidth=0.5,relheight=0.1)
label=tk.Label(frame,text="PRECIPITATION",bg="#80c1ff",font=18)
label.place(rely=0.55,relx=0.6,relwidth=0.4,relheight=0.1)
 
e7=tk.Entry(frame)
e7.place(rely=0.66,relwidth=0.5,relheight=0.1)
label=tk.Label(frame,text="VAPOUR PRESSURE",bg="#80c1ff",font=18)
label.place(rely=0.66,relx=0.6,relwidth=0.4,relheight=0.1)

e8=tk.Entry(frame)
e8.place(rely=0.77,relwidth=0.5,relheight=0.1)
label=tk.Label(frame,text="WET DAY FREQUENCY",bg="#80c1ff",font=18)
label.place(rely=0.77,relx=0.6,relwidth=0.4,relheight=0.1)


button=tk.Button(frame,text="Test button",command=show_entry_fields)
button.place(rely=0.9,relwidth=1,relheight=0.1)


lower_frame=tk.Frame(root,bd=5)
lower_frame.place(relx=0.5,rely=0.6,relwidth=0.8,relheight=0.35,anchor='n')

label1=tk.Label(lower_frame,font=" Times 32")


root.mainloop()