import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#creating the root or base for the app
root = ctk.CTk()

root.geometry("400x200")
root.iconbitmap('headphone_headphones_support_microphone_icon.ico')
root.title("cutom Button")

def call_button_disiable():
    my_button = ctk.CTkButton(root, state="disabled")
    print("Button disabled")

#creating a button 
my_button = ctk.CTkButton(root,
                          text = "Python learning",
                          width=60,
                          height=30,
                          command=call_button_disiable,
                          fg_color="#9bdefc",
                          hover_color="#dcff00",
                          text_color="Black",
                          corner_radius=50
                          )
my_button.grid(row=2,column=2,padx=150,pady=80)
 

root.mainloop()