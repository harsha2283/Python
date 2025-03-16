import customtkinter as ctk

class Mycheckboxframe(ctk.CTkFrame):

    def __init__(self, master, title, values_checkbox_names):
        super().__init__(master)
        self.values_checkbox_names = values_checkbox_names
        self.title = title
        self.check_boxes = []
        
        #title to the frame
        self.title = ctk.CTkLabel(master=self, text=self.title, fg_color="gray40", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")

        #checkboxes
        for i, value in enumerate(self.values_checkbox_names):
            checkbox = ctk.CTkCheckBox(master=self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky="w")
            self.check_boxes.append(checkbox)
    
    def get(self):
        checkboxes_ticked= []
        for checkbox in self.check_boxes:
            if checkbox.get() == 1:
                checkboxes_ticked.append(checkbox.cget(attribute_name="text"))
    
        return checkboxes_ticked

class MyRadioButtonFrame(ctk.CTkFrame):

    def __init__(self, master, title, values_radio_button_names):
        super().__init__(master)
        self.values_radio_button_names = values_radio_button_names
        self.title = title
        self.radio_buttons = []
        self.variable = ctk.StringVar(value="")

        #title frame with CTkLabel
        self.title = ctk.CTkLabel(master=self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")

        #Radio buttons
        for i, value in enumerate(self.values_radio_button_names):
            radio_button = ctk.CTkRadioButton(master=self, text=value, value=value, variable=self.variable)
            radio_button.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky="ew")
            self.radio_buttons.append(radio_button)
    
    def get(self):
        return self.variable.get()
    
    # def set(self,value):
    #     self.variable.set(value=value)



class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(string="My App")
        self.geometry(geometry_string="400x200")
        self.columnconfigure(index=(0,1), weight=1)
        self.rowconfigure(index=0, weight=1)

        #colour theme could be dark , light or system 
        '''A custom theme also can be made check the customtkinter documentation'''
        ctk.set_appearance_mode(mode_string="system")

        #Frame creation 
        self.check_box_frame_1 = Mycheckboxframe(master=self,title="Values", values_checkbox_names=["box 1", "box 2", "box 3"])
        self.check_box_frame_1.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")

        self.Radiobutton_frame = MyRadioButtonFrame(master=self, title="options", values_radio_button_names=["box 4", "box 5"])
        self.Radiobutton_frame.grid(row=0, column=1, padx=10, pady=(10,0), sticky="nsew")

        #fg_colour of the each frame can be changed 
        self.Radiobutton_frame.configure(fg_color="gray20")

        #button creation
        self.my_button = ctk.CTkButton(master=self, text="My button", command=self.button_callback, border_color="#3D8D7A", border_width=2)
        self.my_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)


    def button_callback(self):
        print(f"check_box_frame_1's ticked check boxes are {self.check_box_frame_1.get()}")
        print(f"Radiobutton_frame's ticked radio button is {self.Radiobutton_frame.get()}")


        

app = App()

app.mainloop()