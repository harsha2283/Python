import customtkinter as ctk 
from typing import Union

class FloatSpinBox(ctk.CTkFrame):
    def __init__(self, *args, width:int = 100, height:int = 32, step_size : Union[int, float] = 1,command: callable=None,**kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size=step_size
        self.command= command

        self.configure(fg_color=("gray78", "gray28"))

        self.grid_columnconfigure(index=(0,2),weight=1)
        self.grid_columnconfigure(index=1,weight=1)

        #subtract button 
        self.subtract_button = ctk.CTkButton(master=self, text="-", width=height-6, height=height-6, command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3,0), pady=3)

        #entry
        self.entry = ctk.CTkEntry(self, width=(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, padx=3, pady=3,sticky="ew")

        #add button 
        self.add_button=ctk.CTkButton(self, text="+" ,width=height-6, height=height-6,command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0,3),pady=3)

        self.entry.insert(0,"0.0")#default value

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) + self.step_size
            self.entry.delete(first_index=0, last_index="end")
            self.entry.insert(index=0,string=str(value))
        except ValueError:
            return
        
    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) - self.step_size
            self.entry.delete(first_index=0, last_index="end") 
            self.entry.insert(index=0,string=str(value))
        except ValueError:
            return

    def get(self) -> Union[float, None]:
        try: 
            return float(self.entry.get())
        except ValueError:
            return None
    
    def set(self, value:float):
        self.entry.delete(first_index=0, last_index="end")
        self.entry.insert(index=0, string=str(float(value)))


#App
app = ctk.CTk()

spin_box1 = FloatSpinBox(app, width=1000, step_size=1)
spin_box1.pack(padx=20, pady=20)

# spin_box1.set(value=30)
print(spin_box1.get())

app.mainloop()
