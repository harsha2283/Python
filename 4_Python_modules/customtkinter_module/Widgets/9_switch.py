import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root= ctk.CTk(fg_color="#000000")
root.title("Switch")
root.iconbitmap("C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\leo_2.ico")
root.geometry("300x300")

def switcher_out():
    if my_switch.get() == "on":
        my_label.configure(text=f"Yes Today is sunday")
    elif  my_switch.get() == "off":
        my_label.configure(text=f"No Today is not sunday")  

def clicker():
    if my_switch.get() == "on":
        my_switch.deselect()
        my_label.configure(text=f"No Today is not sunday")
    elif  my_switch.get() == "off":
        my_switch.select()
        my_label.configure(text=f"Yes Today is sunday")    

#string variable 
Switch_var = ctk.StringVar(value="on")

#switch
my_switch = ctk.CTkSwitch(master=root,
                          button_color="#247291",
                          button_hover_color="#73C7C7",
                          text="Today is sunday ?",
                          onvalue="on",
                          offvalue="off",
                          text_color="#96CEB4",
                          progress_color="#B3D8A8",
                          command=switcher_out,
                          font=("arial", 20, "bold"),
                          )
my_switch.pack(pady=40)

my_label = ctk.CTkLabel(master=root, text="No Today is not sunday",
                        fg_color="#578FCA",
                        corner_radius=10,
                        )
my_label.pack(pady=10)

my_button = ctk.CTkButton(master=root, text="Toggle", command=clicker,
                          fg_color="#21294C",
                          hover_color="#555C78",
                          font=("arial",20,"bold")
                          )
my_button.pack(pady=10)

root.mainloop()