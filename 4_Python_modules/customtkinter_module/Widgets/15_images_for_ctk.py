import customtkinter as ctk 
from PIL import Image

mode = ["dark", "light"]
 
theme_mode = mode[0]
ctk.set_default_color_theme("blue")

root = ctk.CTk()

root.title("images for ctk")
root.iconbitmap("C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\dragon_1.ico")
root.geometry("400x500")

def mode_change():
    global theme_mode
    if theme_mode == mode[1]:
        theme_mode = mode[0]
        my_label_1.configure(text=f"{mode[0]}")
        update_image('C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\images\\maha_shiva.jpg')
    elif theme_mode == mode[0]:
        theme_mode = mode[1]
        my_label_1.configure(text=f"{mode[1]}")
        update_image('C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\images\\Screenshot 2024-07-20 234836.png')
        

def update_image(image_path):
    global image_label
    my_image = ctk.CTkImage(light_image=Image.open(image_path),
                        dark_image=Image.open(image_path),
                        size=(400,400),)       
    my_label.configure(image=my_image)

# my_image = ctk.CTkImage(light_image=Image.open('C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\images\\Screenshot 2024-07-20 234836.png'),
#                         dark_image=Image.open('C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\images\\maha_shiva.jpg'),
#                         size=(400,400),)

my_label = ctk.CTkLabel(master=root, text="",)
my_label.pack(pady=0)
update_image('C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\images\\maha_shiva.jpg')


my_button = ctk.CTkButton(master=root, text=f"change theme",
                          command=mode_change)
my_button.pack(pady=10)

my_label_1 = ctk.CTkLabel(master=root, text=f"{theme_mode}",fg_color="#ffffff",corner_radius=10,
                          text_color="#000000", font=("arial", 20, "bold"))
my_label_1.pack(pady=5)

root.mainloop()