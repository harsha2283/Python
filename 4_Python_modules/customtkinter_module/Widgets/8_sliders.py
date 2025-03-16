import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


root = ctk.CTk(fg_color="#000000")
root.title("Slider")
root.geometry("500x150")
root.iconbitmap(bitmap="C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\dragon_2.ico")


#function
def slider_out(value):
    my_label.configure(text=f"{int(value)}")
    print(f"slider value is {my_slider.get()}")

my_slider = ctk.CTkSlider(master=root, 
                          from_ = 0,
                          to=100,
                          command=slider_out,
                          number_of_steps=10,
                          button_color="#4B5945",
                          progress_color="#85A947",
                          button_hover_color="#B2C9AD",
                          state="normal",
                          fg_color="#727D73"
                          )
my_slider.pack(pady=10)

#Define starting point 
my_slider.set(output_value=0)

my_label = ctk.CTkLabel(master=root, text="",fg_color="#B3D8A8",
                        text_color="#000000",
                        corner_radius=10,
                        font=("arial",20,"bold"))
my_label.pack(pady=20)


root.mainloop()

