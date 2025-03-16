import customtkinter as ctk

ctk.set_appearance_mode(mode_string="dark")
ctk.set_default_color_theme(color_string="blue")

app = ctk.CTk()

app.geometry(geometry_string="400x600")
app.title("CTkComboBox")
app.iconbitmap(bitmap="C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\cool.ico")

def color_picker_1(choice):
    if choice == "Tent Green":
        out_label.configure(text= choice,text_color="#D2FF72")
    elif choice == "Ocean Blue":
        out_label.configure(text= choice,text_color="#2192FF")
    elif choice == "Desert Red":
        out_label.configure(text= choice,text_color="#EB5A3C")
    else:
        pass

def color_picker_2():
    if mycombo.get() == "Tent Green":
        out_label.configure(text= mycombo.get(),text_color="#D2FF72")
    elif mycombo.get() == "Ocean Blue":
        out_label.configure(text= mycombo.get(),text_color="#2192FF")
    elif mycombo.get() == "Desert Red":
        out_label.configure(text= mycombo.get(),text_color="#EB5A3C")
    else:
        pass

def color_picker_3():
    mycombo.set(value="Green")    
    out_label.configure(text=mycombo.get(), text_color="#3EA70B")

mylabel = ctk.CTkLabel(master=app, text="pick a color", 
                       font=("Stencil",30,"bold"),
                       text_color="#FFF7D1")
mylabel.pack(pady=30)

Neon_colours = ["Tent Green","Ocean Blue","Desert Red"]
'''tent green = #D2FF72
   Ocean blue = #2192FF
   Desert red = #EB5A3C
'''

#Combo
mycombo = ctk.CTkComboBox(master=app, values=Neon_colours,
                          width=200,
                          height=30,
                          font=("Cascadia Code SemiLight",18),
                          dropdown_font=("Cascadia Code SemiLight",18,"bold"),
                          corner_radius=20,
                          border_width=1,
                          border_color="#A27B5C",
                          button_color="#A27B5C",
                          hover=True,
                          button_hover_color="#98DED9",
                          dropdown_hover_color="#A27B5C",
                          fg_color="#3F4E4F",
                          dropdown_fg_color="#3F4E4F",
                          text_color="#E9A6A6",
                          justify="center",
                          dropdown_text_color="#E9A6A6"
                          )
mycombo.pack(pady=15)

#My button
mybutton = ctk.CTkButton(master=app, 
                         text="Pick a color",
                         command= color_picker_2,
                         fg_color="#A27B5C")
mybutton.pack(pady=15)

#custom button
custom_button = ctk.CTkButton(master=app, text="Color Green", command=color_picker_3,
                              fg_color="#A27B5C")
custom_button.pack(pady=20)

#Label
out_label = ctk.CTkLabel(master=app, text="", 
                         font=("Stencil",20,"bold"),
                         fg_color="gray25",
                         corner_radius=10,
                         )
out_label.pack(pady=15)

app.mainloop()