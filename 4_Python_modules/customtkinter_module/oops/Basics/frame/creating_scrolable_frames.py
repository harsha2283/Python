import customtkinter as ctk

class MyScrollableCheckBoxFrame(ctk.CTkScrollableFrame):
    
    def __init__(self, master, values, title):
        super().__init__(master, label_text=title)

        self.values = values
        self.title = title
        self.check_boxes = []
        self.grid_columnconfigure(index=0, weight=1)
        '''CTkScrollableFrame - will not need any new label it will take the title as a arguemnt for label name'''
        # #frame label 
        # self.title = ctk.CTkLabel(master=self, fg_color="gray30", text=self.title, corner_radius=6)
        # self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")

        for i, value in enumerate(self.values):
            check_box= ctk.CTkCheckBox(master=self, text=value)
            check_box.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky="w")
            self.check_boxes.append(check_box)

    def get(self):
        check_boxes_checked =[]
        for checkbox in self.check_boxes:
            if checkbox.get() == 1:
                check_boxes_checked.append(checkbox.cget("text"))
        
        return check_boxes_checked
    

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(string="My app")
        self.geometry("300x300") #row_size X column_size
        self.attributes('-topmost', True) # keeps window sticked at the top
        self.columnconfigure(index=0,weight=1)
        self.rowconfigure(index=0, weight=1)

        checkbox_values = ["value1","value2","value3","value4","value5","value6","value7","value8"]
        self.scrollable_checkbox_frame= MyScrollableCheckBoxFrame(master=self,title="inputs",values=checkbox_values)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=10, sticky ="nesw")
        
        self.my_button = ctk.CTkButton(master=self, text="check_box_button", command=self.button_callback)
        self.my_button.grid(row=1,column=0, padx=10, pady=10, sticky="ew", columnspan=2)
    
    def button_callback(self):
        print(f"The check boxes ticked are {self.scrollable_checkbox_frame.get()}")
        


app = App()

app.mainloop()