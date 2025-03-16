import customtkinter as ctk


# def button_callout():
#     print("Button with + is pressed")

# app = ctk.CTk()
# app.title("Custom app")
# app.geometry("400x200")

# #button
# button = ctk.CTkButton(master=app,text="+",command=button_callout)
# button.grid(row=0, column=0, padx=20, pady=20, sticky="ew",columnspan=2)
# app.grid_columnconfigure((0,1),weight=1)

# #checkbox
# checkbox_1 = ctk.CTkCheckBox(master=app,text="Checkout_1")
# checkbox_1.grid(row=1,column=0,padx=20,pady=(0,20),sticky="w")
# checkbox_2 = ctk.CTkCheckBox(master=app,text="Checkbox_2")
# checkbox_2.grid(row=1,column=1,padx=20,pady=(0,20), sticky="w")

# app.mainloop()

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
    
        self.title("My app")
        self.geometry("400x200")
        self.grid_columnconfigure((0,1), weight=1)

        self.button = ctk.CTkButton(master=self, text="Button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        self.checkbox_1= ctk.CTkCheckBox(master=self,text="check_box_1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        '''padx=(padding_from_left_side, padding_from_right_side), 
           pady=(padding_from_top, padding_from_bottom)
        '''
        self.checkbox_2= ctk.CTkCheckBox(master=self,text="check_box_2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

    def button_callback(self):
            print("button pressed")


app = App()

app.mainloop()
