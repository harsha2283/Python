import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk(fg_color="#000000")

root.title("custom fonts")
root.iconbitmap("C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\dragon_1.ico")
root.geometry("400x200")


def change():
    myfont.configure(underline = False, overstrike=False, slant = "roman", size = 20)

myfont = ctk.CTkFont(family="arial",size=15,
                     weight="bold",slant="italic",
                     underline=True,
                     overstrike=True )

my_label = ctk.CTkLabel(root, text="This is a font check text",font=myfont)
my_label.pack(pady=40)

my_button = ctk.CTkButton(master=root,text="Font change",
                          fg_color="#7895CB",
                          command=change)
my_button.pack(pady=20)

root.mainloop()