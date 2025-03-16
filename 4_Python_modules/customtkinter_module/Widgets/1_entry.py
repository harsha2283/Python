import customtkinter as ctk 

#set theme and colour options 
ctk.set_appearance_mode(mode_string="dark")
ctk.set_default_color_theme(color_string="blue")


app = ctk.CTk()

app.title("CTkEntry")
app.iconbitmap("C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\cool.ico")
app.geometry(geometry_string="400x400")


def submit():
    my_label.configure(text= f"Hello {my_entry.get()}")
    my_entry.configure(state="disabled")

def clear():
    my_entry.configure(state="normal")
    my_entry.delete(first_index=0, last_index="end")    

#label 
my_label = ctk.CTkLabel(app, text="", 
                        font=("calbri",20,"bold"),
                        fg_color="#A5BFCC",
                        text_color="black",
                        corner_radius=5)
my_label.pack(pady=40)

# entry

my_entry = ctk.CTkEntry(master=app, 
                        placeholder_text="Enter the name", 
                        placeholder_text_color="#3A3960",
                        width=200,
                        height=10,
                        font=("Helvetica", 20),
                        corner_radius=10,
                        text_color="#213555",
                        fg_color=("#3E7B27","#85A947"),
                        border_width=5,
                        border_color="black")
my_entry.pack(pady=20)

#submit button
my_button = ctk.CTkButton(master=app, text="submit", command=submit)
my_button.pack(pady=10)

#clear button
clearbutton = ctk.CTkButton(master=app, text="clear",command=clear)
clearbutton.pack(pady=10)

app.mainloop()