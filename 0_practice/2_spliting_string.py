import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("800x600")
app.title("Background Image Example")

bg_image = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\Harsha vardhan reddy\\Pictures\\wallpapers\\524342.jpg"),
                                     size=(800, 600))

bg_label = customtkinter.CTkLabel(app, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = customtkinter.CTkLabel(app, text="CustomTkinter with Background Image", font=customtkinter.CTkFont(size=20, weight="bold"))
label.place(relx=0.5, rely=0.1, anchor="center")

button = customtkinter.CTkButton(app, text="Click Me")
button.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()