import customtkinter as ctk

ctk.set_appearance_mode(mode_string="dark")
ctk.set_default_color_theme(color_string="blue")

root = ctk.CTk()

root.iconbitmap(bitmap="C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\cool.ico")
root.geometry(geometry_string="400x400")
root.title(string="CTkCheckBox")

def game():
    if mycheckbox.get() == "on":
        my_label.configure(text="You had played the game of clicking checkbox")
        text_var.set(value="Awsome you played the game with me hurray!!!")
    else:
        my_label.configure(text="come on man let's play ")
    

def deselect_callback():
    mycheckbox.deselect()
    text_var.set(value="Would you like to play a game !")
    my_label.configure(text="")

def toggle_callback():
    if mycheckbox.get() == "on":
        mycheckbox.toggle()
        text_var.set(value="Would you like to play a game !")
    else:
        mycheckbox.toggle()
        my_label.configure(text="")



check_var = ctk.StringVar(value="off")

text_var = ctk.StringVar(value="Would you like to play a game !")
mycheckbox= ctk.CTkCheckBox(master=root, 
                            width=50,
                            height=20,
                            # text="Would you like to play a game",
                            variable=check_var,
                            onvalue="on",
                            offvalue="off",
                            fg_color="#16C47F",
                            hover_color="red",
                            hover=True,
                            text_color="#79D7BE",
                            textvariable=text_var,
                            )
mycheckbox.pack(pady=40)

#submit button
submit_button = ctk.CTkButton(master=root, text="Submit",command=game)
submit_button.pack(pady=10)

#button to deselect 
deselect_button = ctk.CTkButton(master=root, text="Deselect", command=deselect_callback)
deselect_button.pack(pady=10)

#select button 
select_button = ctk.CTkButton(master=root, text="Select", command=mycheckbox.select)
select_button.pack(pady=10)

#toggle button 
toggle_button = ctk.CTkButton(master=root, text="Toggle", command= toggle_callback)
toggle_button.pack(pady=10)

#label
my_label = ctk.CTkLabel(master=root, text="" )
my_label.pack(pady=10)

root.mainloop()