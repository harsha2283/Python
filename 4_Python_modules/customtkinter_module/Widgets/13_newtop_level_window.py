import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk(fg_color="#000000")

root.title("Top up window")
root.iconbitmap("C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\dragon_1.ico")
root.geometry("400x120")

def newwindow():
    new_window = ctk.CTkToplevel(master=root,fg_color="gray30")
    new_window.title("New Window")
    new_window.geometry("400x200")
    new_window.resizable(width=False, height=False)

    def close():
        new_window.destroy()
        new_window.update()
    

    #creating a button in the new window
    new_button= ctk.CTkButton(master=new_window, text="close the new window",
                              command=close)
    new_button.pack(pady=30)


my_button = ctk.CTkButton(master=root, text="Top up window",command=newwindow)
my_button.pack(pady=20)

root.mainloop()

