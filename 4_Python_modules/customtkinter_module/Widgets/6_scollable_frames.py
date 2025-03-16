import customtkinter as ctk 

ctk.set_appearance_mode(mode_string="dark")
ctk.set_default_color_theme(color_string="blue")


root = ctk.CTk(fg_color="#0C0C0C")

root.title("Scrollable_frame")
root.iconbitmap("C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\cool.ico")
root.geometry(geometry_string="400x400")

my_frame = ctk.CTkScrollableFrame(master=root,
                                  label_text="Frame",
                                  fg_color="#3C3D37",
                                  width=200,
                                  height=50,
                                  label_font=("Arial",15,"bold"),
                                  corner_radius=10,
                                  label_text_color="#ECDFCC",
                                  label_anchor="center",
                                  label_fg_color="#1E201E",
                                  scrollbar_button_hover_color="#FF9D23",
                                  )
my_frame.pack(pady=50)
# my_frame.grid(row=0,column=0,padx=10,pady=10)


Buttons = ["Harsha", "Ambika", "Amma", "Nana", "Annaya", "Vadina", "Friends", "Akka", "Devudhu"]
for button in Buttons:
    button = ctk.CTkButton(master=my_frame, 
                           text=button, 
                           fg_color="#F97311", 
                           text_color="#0C0C0C",
                           hover_color="#647E68",
                           corner_radius=10, 
                           )
    button.pack(pady=5)


root.mainloop()

