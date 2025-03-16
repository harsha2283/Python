import customtkinter as ctk

root = ctk.CTk()

root.title("Option menu")
root.geometry(geometry_string="400x200")
root.iconbitmap(bitmap="C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\dragon_2.ico")

Themes = ["system", "dark", "light"]
colors = ["blue", "dark-blue", "green"]

def Mode_switch():
    if myoption.get() == 'dark':
        ctk.set_appearance_mode(myoption.get())
        mylabel.configure(text=f"{myoption.get()} mode")
    elif  myoption.get() =="system":
        ctk.set_appearance_mode(myoption.get())
        mylabel.configure(text=f"{myoption.get()} mode")
    else:
        ctk.set_appearance_mode(myoption.get())
        mylabel.configure(text=f"{myoption.get()} mode")

mylabel = ctk.CTkLabel(master=root, 
                       text_color="#000000",
                       text="Theme", fg_color="#95D2B3",corner_radius=10)
mylabel.pack(pady=10)

myoption = ctk.CTkOptionMenu(master=root,values=Themes,
                             fg_color="#9BDF46",
                             text_color="#000000",
                             button_color="#25A55F",
                             font=("arial", 20, "bold"),
                             
                             )
myoption.pack(pady=20)

mybutton = ctk.CTkButton(master=root, text="change mode",
                         command=Mode_switch,
                         text_color="#000000")
mybutton.pack(pady=10)
 
root.mainloop()