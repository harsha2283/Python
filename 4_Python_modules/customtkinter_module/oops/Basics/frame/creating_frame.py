import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("My Frame")
        self.geometry(geometry_string="400x180")
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)

        #Frame creation
        self.checkbox_frame = ctk.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsw")

        #checkboxes
        self.checkbox_1 = ctk.CTkCheckBox(master=self.checkbox_frame,text="Check box 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10,0),sticky="w")
        self.checkbox_2 = ctk.CTkCheckBox(master=self.checkbox_frame,text="Check box 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10,0),sticky="w")

        #button
        self.my_button = ctk.CTkButton(master=self, text="+", command=self.button_callback)
        self.my_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("pressed button with sign '+'")


#creating a instance
app = App()

app.mainloop()
