import customtkinter as ctk 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk(fg_color="#000000")

root.title("Segmented Buttons")
root.iconbitmap("C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\dragon_1.ico")
root.geometry("300x120")

#segbutton function 
def Clicker(value):
    dict_day = {"Mon":"Monday", "Tue":"Tuesday", "Wed":"Wednesday", "Thu":"Thursday", "Fri":"Friday", "Sat":"Saturday", "Sun":"Sunday"}
    if value in dict_day.keys():
        my_label.configure(text=f"Today is {dict_day[value]}")
    else:
        pass

button_values=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

my_seg_button = ctk.CTkSegmentedButton(master=root,
                                       values=button_values,
                                       command=Clicker,
                                       selected_hover_color="#654520",
                                       selected_color="#825B32",
                                       )
my_seg_button.pack(pady=20)

#set default button 
my_seg_button.set(value="Mon")

#label
my_label = ctk.CTkLabel(master=root, text="select what is the current day !",fg_color="#8EB486",
                        corner_radius=10,
                        text_color="#000000",
                        )
my_label.pack(pady=10)

root.mainloop()