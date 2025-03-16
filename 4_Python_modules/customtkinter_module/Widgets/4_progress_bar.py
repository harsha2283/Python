import customtkinter as ctk


ctk.set_appearance_mode(mode_string="dark")
ctk.set_default_color_theme(color_string="blue")

root = ctk.CTk(fg_color="#171717")

root.title(string="CTkprogressBar")
root.iconbitmap(bitmap="C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\cool.ico")
root.geometry(geometry_string="600x300")

def clicker():
    my_progressbar.step()
    mylabel.configure(text=(int(my_progressbar.get()*100)))
    if (int(my_progressbar.get()*100)) <=100 and (int(my_progressbar.get()*100))>=50:
        my_progressbar.configure(progress_color="#4E9F3D")
    elif (int(my_progressbar.get()*100)) <50 and (int(my_progressbar.get()*100))>=0:
        my_progressbar.configure(progress_color="#DA0037")

def start():
    my_progressbar.start()

def mode_change():
    my_progressbar.configure(mode="determinate")
    
#progress bar
my_progressbar = ctk.CTkProgressBar(master=root, orientation= "horizontal",
                                    progress_color="#DA0037",
                                    mode="indeterminate",
                                    determinate_speed=2.5,
                                    indeterminate_speed=1,
                                    corner_radius=2,
                                    height=10,
                                    width=300,
                                    )
my_progressbar.pack(pady=30)

#setting the intial value of the progress bar 
my_progressbar.set(value=0)

my_button =ctk.CTkButton(master=root, text="Increment Bar",command=clicker,
                         fg_color="#444444",
                         hover_color="#444444",
                         text_color="#EDEDED",                         
                         )
my_button.pack(pady=10)

mode_button =ctk.CTkButton(master=root, text="Mode Change",command=mode_change,
                         fg_color="#444444",
                         hover_color="#444444",
                         text_color="#EDEDED",                         
                         )
mode_button.pack(pady=10)

start_button =ctk.CTkButton(master=root, text="Start",command=start,
                         fg_color="#444444",
                         hover_color="#444444",
                         text_color="#EDEDED",                         
                         )
start_button.pack(pady=10)

stop_button =ctk.CTkButton(master=root, text="Stop",command=my_progressbar.stop,
                         fg_color="#444444",
                         hover_color="#444444",
                         text_color="#EDEDED",                         
                         )
stop_button.pack(pady=10)

mylabel=ctk.CTkLabel(master =root, text="",font=("Cascadia Code",10,"bold"))
mylabel.pack(pady=10)

root.mainloop()