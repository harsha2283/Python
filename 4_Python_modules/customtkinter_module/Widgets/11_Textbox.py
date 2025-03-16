import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk(fg_color="#000000")

root.title("Textbox")
root.geometry("700x300")
root.iconbitmap("C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\dragon_1.ico")

data = ''

#Callbacck functions
def delete_button_callback():
    my_textbox.delete(index1=0.0,index2='end')

def copy_button_callback():
    global data
    data = my_textbox.get(index1=0.0, index2="end")

def paste_button_callback():
    if data:
        my_textbox.insert("end",data)
    else:
        my_textbox.insert("end","There is nothing copied to paste")

my_textbox = ctk.CTkTextbox(master=root, 
                            width=600,
                            height=150,
                            border_spacing=5,
                            text_color="#000000",
                            fg_color="#FA744F",
                            font=("arial", 20,"bold"),
                            wrap="word",
                            scrollbar_button_color="#000000",

                            )
my_textbox.pack(pady=20)

my_frame = ctk.CTkFrame(master=root,fg_color="#000000",
                        )
my_frame.pack(pady=10)

Delete_button=ctk.CTkButton(master=my_frame,text="Delete",
                            command=delete_button_callback)
Delete_button.grid(row=0, column=0)

Copy_button=ctk.CTkButton(master=my_frame,text="Copy",
                          command=copy_button_callback)
Copy_button.grid(row=0, column=1, padx=10)

paste_button=ctk.CTkButton(master=my_frame,text="Paste",
                           command=paste_button_callback)
paste_button.grid(row=0, column=2)

root.mainloop() 

