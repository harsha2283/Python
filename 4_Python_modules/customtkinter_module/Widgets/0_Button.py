import customtkinter as ctk 
import random

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

#creating the root or base for the app
root = ctk.CTk(fg_color="#000000")

root.geometry("400x400")
root.iconbitmap('C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\cool.ico')
root.title("CTkButton")

def call_button_disiable():
    list_bool:bool = [True, False]
    if random.choice(list_bool) == True:
        my_label.configure(text=my_button.cget("text"), fg_color= ("#7886C7"))
    else:
        my_label.configure(text="False", fg_color=("#9DC08B"))
    label_text = my_label.cget("text")
    print(f"Random returned {label_text}")

#creating a button 
my_button = ctk.CTkButton(root,
                          text = "Python learning",
                          width=50,
                          height=60,
                          command=call_button_disiable,
                          fg_color="#A3D1C6",
                          hover_color="#F7CFD8",
                          text_color="Black",
                          corner_radius=10,
                          font=("times new roman", 20, "bold"),
                          border_width=2.5,
                          border_color="black",
                          state="normal"
                          )
my_button.pack(pady=80) 


my_label = ctk.CTkLabel(root,
                        text_color="white",
                        text="white",
                        font=("calbri", 15, "bold"),
                        fg_color="gray30",
                        corner_radius=10)
my_label.pack(pady=20)

root.mainloop()