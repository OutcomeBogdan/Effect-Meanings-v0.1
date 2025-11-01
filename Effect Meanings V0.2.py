from customtkinter import *
from PIL import Image

win = CTk()
win.geometry('600x600')
win.title('Effect Meanings')

label = CTkLabel(win, text='Pick an Effect!', font=('Arial', 14, 'bold'))
label.grid(row=0,column=2,columnspan=3,pady=20,padx=10)

def btn_1_click():
    label_text.configure(text='''Fire: is the rapid oxidation of a fuel 
    in the exothermic chemical process of combustion, releasing heat, light, 
    and various reaction products. Flames, the most visible portion of the fire, 
    are produced in the combustion reaction when the fuel reaches its 
    ignition point temperature.''')

img1= Image.open('fire3.jpg')
img_ctk1 = CTkImage(light_image=img1, size=(100, 100))
btn_1 = CTkButton(win, text='Fire',width=100,image=img_ctk1,command=btn_1_click)
btn_1.grid(row=1,column=1,pady=20,padx=10)

def btn_2_click():
    label_text.configure(text='''Water: is the liquid that descends from the clouds as rain, 
    forms streams, lakes, and seas. it's a major constituent of all living matter 
    and that when pure is an odorless, tasteless, and very slightly compressible.
    liquid oxide of hydrogen H2O which appears bluish in thick layers, 
    it freezes at 0°C and boils at 100°C.''')
img2= Image.open('water5.jpg')
img_ctk2 = CTkImage(light_image=img2, size=(100, 100))
btn_2 = CTkButton(win, text='Water',width=100,image=img_ctk2,command=btn_2_click)
btn_2.grid(row=1, column=2,pady=20,padx=10)

def btn_3_click():
    label_text.configure(text='''Acid: A chemical that gives off tons in water 
    and forms salts by combining with certain metals. Which also has different types.
    Acids have a sour taste and turn certain dyes red. Some acids made by the body,
    such as gastric acid, can help organs work the way they should.
    An example of an acid is hydrochloric acid.''')
img3= Image.open('acid5.jpg')
img_ctk3 = CTkImage(light_image=img3, size=(100, 100))
btn_3 = CTkButton(win, text='Acid',width=100,image=img_ctk3,command=btn_3_click)
btn_3.grid(row=1,column=3,pady=20,padx=10)

def btn_4_click():
    label_text.configure(text='''Lava: is molten or partially molten rock (magma) 
    that has been expelled from the interior of a terrestrial planet 
    (such as Earth) or a moon onto its surface. Lava may be erupted at a volcano
    or through a fracture in the crust, on land or underwater, 
    usually at temperatures from 800 to 1,200 °C (1,470 to 2,190 °F).''')
img4= Image.open('lava.jpg')
img_ctk4 = CTkImage(light_image=img4, size=(100, 100))
btn_4 = CTkButton(win, text='Lava',width=100,image=img_ctk4,command=btn_4_click)
btn_4.grid(row=2, column=1,pady=20,padx=10)

def btn_5_click():
    label_text.configure(text='''Night: the time between sunset and sunrise 
    while it is dark outside. it has long been a symbol of mystery, darkness, 
    and the unknown. It holds a significant place in literature, art, and culture,
    often representing a time of introspection, transformation, and revelation.''')
img5= Image.open('night.jpg')
img_ctk5 = CTkImage(light_image=img5, size=(100, 100))
btn_5 = CTkButton(win, text='Night',width=100,image=img_ctk5,command=btn_5_click)
btn_5.grid(row=2,column=2,pady=20,padx=10)

def btn_6_click():
    label_text.configure(text='''Plasma: is a state of matter along with solids,
    liquids and gases. When a neutral gas is heated such that some of the electrons
    are freed from the atoms or molecules, it changes state and becomes a plasma.
    It consists of a partially-ionized gas, containing ions, electrons, 
    and neutral atoms.''')
img6= Image.open('plasma2.jpg')
img_ctk6 = CTkImage(light_image=img6, size=(100, 100))
btn_6 = CTkButton(win, text='Plasma',width=100,image=img_ctk6,command=btn_6_click)
btn_6.grid(row=2, column=3,pady=20,padx=10)

label_text = CTkLabel(win, text="There's supposed to be the text you're gonna see!", font=('Arial', 14, 'bold'))
label_text.grid(row=3,column=1,columnspan=3,pady=20,padx=10)
win.mainloop()