import customtkinter as ctk


def button_callout():
    print("Button is pressed")

app = ctk.CTk()
app.title("Custom app")
app.geometry("500x200")

button = ctk.CTkButton(master=app,text="Click here",command=button_callout)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
app.grid_columnconfigure(index=0,weight=1)
app.mainloop()