import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


root = ctk.CTk(fg_color="#000000")
root.title("Tabview")
root.geometry("700x500")
root.iconbitmap(bitmap="C:\\Users\\Harsha vardhan reddy\\Documents\\My_learning_plans\\python\\Git_clones\\Python\\4_Python_modules\\customtkinter_module\\Widgets\\icons\\dragon_2.ico")

#function to switch to tab 2 
def switch_2_TAB_2():
    my_tab.set("TAB 2")

#function to switch to tab 1
def switch_2_TAB_1():
    my_tab.set("TAB 1")

#create Tab view
my_tab = ctk.CTkTabview(master=root,
                        height=450,
                        width=600,
                        segmented_button_selected_color="#90D26D",
                        text_color="#000000",
                        segmented_button_selected_hover_color="#DEFBC2",
                        # font=("arial",20,"bold"),
                        fg_color="#F1D4E5"
                        )
my_tab.pack(pady=10)

#create tabs 
tab_1 = my_tab.add("TAB 1")
tab_2 = my_tab.add("TAB 2")

#put stuff in TAB 1
my_button = ctk.CTkButton(master=tab_1,text="tab_1_button",
                          command=switch_2_TAB_2)
my_button.pack(pady=50)

#put stuff in TAB 2
my_button = ctk.CTkButton(master=tab_2,text="tab_2_button",
                          command=switch_2_TAB_1)
my_button.pack(pady=50)

root.mainloop()