import customtkinter as ctk

#class to create a radio button
class MyRadioButtonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values) -> None:
        super().__init__(master)
        self.values = values
        self.title = title
        self.radiobuttions = []
        self.grid_columnconfigure(0, weight=1)
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray40", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0),sticky="ew")

        for i,value in enumerate(self.values):
            Radiobutton =  ctk.CTkRadioButton(self, text=value, value=value, variable=self.variable, hover_color="white")
            Radiobutton.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky="w")
            self.radiobuttions.append(Radiobutton)

    def get(self):
        return self.variable.get()
    
    #set
    def set(self, value):
        self.variable.set(value)


#Class to create the checkbox
class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self,master,title,values:list):
        super().__init__(master)
        self.title = title
        self.values = values 
        self.checkboxes = []
        self.columnconfigure(0,weight=1)

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray40", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="w")

        #dynamically using the checkboxes
        for i, value in enumerate(self.values,start=0):
            checkbox = ctk.CTkCheckBox(self, text=value,hover_color="yellow")
            checkbox.grid(row=i+1,column=0, padx=10, pady=(10,0), sticky="w")
            self.checkboxes.append(checkbox)
    
    def get(self):

        checked_checkboxes:list = []
        try:
            for checkbox in self.checkboxes:
                if checkbox.get() == 1:
                    checked_checkboxes.append(checkbox.cget("text"))
        except:
            print(f"Error: the error is generated from get() of class 'MyCheckboxFrame'")
        return checked_checkboxes



class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Learning CTk")
        self.geometry("400x200")
        self._set_appearance_mode("dark")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        #Desgining a button
        self.button = ctk.CTkButton(self, text="My button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        #checkbox frame
        self.checkbox_frame_1 = MyCheckboxFrame(self, "person_details",values=["name", "age", "gender"])
        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10,0),sticky="ensw")
        # self.checkbox_frame_1.configure(fg_color="transparent")
        self.checkbox_frame_2 = MyRadioButtonFrame(self, "company deatils", values=["company", "white collar", "BU"])
        self.checkbox_frame_2.grid(row=0, column=1, padx=(0,10), pady=(10,0),sticky="ewns")
        self.checkbox_frame_2.configure(fg_color="transparent")

    #methods
    #A call back function which runs when the button is click
    def button_callback(self):

        try:
            print("Checked checkboxes: ",self.checkbox_frame_1.get())
            print("Checked Radioboxes: ",self.checkbox_frame_2.get())
        except:
            print("Error: error id from the button_callback() from 'class App'")



app=App()
app.mainloop()

