import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk(fg_color="#000000")
 
root.title("Input Dialogue")
root.iconbitmap("C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\dragon_1.ico")
root.geometry("300x200")

def input():
    dialog_box = ctk.CTkInputDialog(text="what is your name? ",title="Pop" )
    data = dialog_box.get_input()
    if data:
        my_label.configure(text=f"Hello {data}")
    else:
        my_label.configure(text=f"You Frogot to type Anything?")

my_button = ctk.CTkButton(master=root, text="Pop up",
                          command=input,
                          )
my_button.pack(pady=30)

my_label = ctk.CTkLabel(master=root, text="")
my_label.pack(pady=20)

root.mainloop()