#concept was learnt from
#website: https://customtkinter.tomschimansky.com/documentation/color
#youtube: https://www.youtube.com/watch?v=Y01r643ckfI&list=PLfZw_tZWahjxJl81b1S-vYQwHs_9ZT77f

# import customtkinter as ck

# app = ck.CTk()

# app.mainloop()

import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
    
        self.title("Learning CTk")
        self.geometry("400x150")
        self.grid_columnconfigure((0,1),weight=1)
        
        #Desgining a button
        self.button = ctk.CTkButton(self, text="My button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        #creating a checkbox 
        self.checkbox_1 = ctk.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0,20), sticky="w")
        self.checkbox_2 = ctk.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0,20), sticky="w")

    #A call back function which runs when the button is click
    def button_callback(self):
        print("button Pressed")
            

app = App()
app.mainloop()

###############code written without the class##############
# #A call back function which runs when the button is click
# def button_callback():
#     print("button Pressed")

# app = ctk.CTk()

# #title of the app window
# app.title("Learning CTk")

# #dimensions fo the window
# app.geometry("400x150")

# #this is to position the button in the middle of the grid
# app.grid_columnconfigure((0,1),weight=1)
# # app.grid_rowconfigure(0,weight=1)

# #Desgining a button
# button = ctk.CTkButton(app, text="Button", command=button_callback)
# button.grid(row=0,column=0, padx=20,pady=20, sticky="ew", columnspan=2)

# #creating a checkbox 
# checkbox_1 = ctk.CTkCheckBox(app, text="checkbox 1")
# checkbox_1.grid(row=1, column=0, padx=20, pady=(0,20), sticky="w")
# checkbox_2 = ctk.CTkCheckBox(app, text="checkbox 2")
# checkbox_2.grid(row=1, column=1, padx=20, pady=(0,20), sticky="w")

# app.mainloop()
