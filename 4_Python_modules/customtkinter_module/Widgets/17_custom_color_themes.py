import customtkinter as ctk

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\Themes\\my_theme.json")

root= ctk.CTk()
root.title(string="Custom Theme")
root.geometry(geometry_string="300x300")
root.iconbitmap(bitmap="C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\dragon_2.ico")

my_button = ctk.CTkButton(master=root, 
                          text="Button")
my_button.pack(pady=10)

my_label = ctk.CTkLabel(master=root, 
                        text="Label")
my_label.pack(pady=10)



root.mainloop()