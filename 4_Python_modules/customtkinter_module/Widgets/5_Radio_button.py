import customtkinter as ctk

ctk.set_appearance_mode(mode_string="dark")
ctk.set_default_color_theme(color_string="blue")

#root
root = ctk.CTk(fg_color="#000000")

root.title(string="CTkRadioButton")
root.geometry(geometry_string="400x400")
root.iconbitmap(bitmap="C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\cool.ico")


def button_callback_radio():
    if radio_var.get() == "yes":
        mylabel_1.configure(text="Please, come to office we need your support")
    elif radio_var.get() == "No":
        mylabel_1.configure(text="Okay! you can support remotely")
    elif radio_var.get() == "leave":
        mylabel_1.configure(text="Okay! you can take leave Chikki 🐒")
    else:
        mylabel_1.configure(text="You didn't answer my question")


mylabel = ctk.CTkLabel(master=root, text="Do you like to go to office on monday ?",
                       fg_color="#30475E",
                       corner_radius=10,
                       )
mylabel.pack(pady=30)

radio_var = ctk.StringVar(value=None)

#Radio button
myradio_button_1 = ctk.CTkRadioButton(master=root, text="Yes i do", value="yes",
                                    variable=radio_var,
                                    radiobutton_height=20,
                                    radiobutton_width=20,
                                    corner_radius=10,
                                    border_color="#DDDDDD",
                                    border_width_checked=2,
                                    border_width_unchecked=1,
                                    hover_color="#F05454",
                                    hover=True,
                                    fg_color="#ED6663",
                                    state="normal",
                                    )
myradio_button_1.pack(pady=10)

myradio_button_2 = ctk.CTkRadioButton(master=root, text="No no i don't ", value="No",
                                    variable=radio_var,
                                    radiobutton_height=20,
                                    radiobutton_width=20,
                                    corner_radius=10,
                                    border_color="#DDDDDD",
                                    border_width_checked=2,
                                    border_width_unchecked=1,
                                    hover_color="#F05454",
                                    hover=True,
                                    fg_color="#ED6663")
myradio_button_2.pack(pady=10)

myradio_button_3 = ctk.CTkRadioButton(master=root, text="i need leave for 1 week", value="leave",
                                    variable=radio_var,
                                    radiobutton_height=20,
                                    radiobutton_width=20,
                                    corner_radius=10,
                                    border_color="#DDDDDD",
                                    border_width_checked=2,
                                    border_width_unchecked=1,
                                    hover_color="#F05454",
                                    hover=True,
                                    fg_color="#ED6663")
myradio_button_3.pack(pady=10)

mybutton =ctk.CTkButton(master=root, text="submit", command=button_callback_radio)
mybutton.pack(pady=10)

mylabel_1 = ctk.CTkLabel(master=root, text="")
mylabel_1.pack(pady=10)
root.mainloop()