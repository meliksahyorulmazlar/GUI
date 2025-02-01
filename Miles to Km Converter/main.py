# from tkinter import *
import pyperclip
import customtkinter as ctk

class MileKmConverter:
    def __init__(self):
        self.setup_window()
        self.final_setup()
        self.window.mainloop()

    def setup_window(self):
        self.window = ctk.CTk()
        self.window.geometry("+-5+0")
        self.window.resizable(0,0)
        self.window.title("Miles to Kilometers Converter")
        # self.window.config(padx=20, pady=100)
        # self.window.minsize(width=350, height=100)
        # self.window.maxsize(width=350, height=100)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=1)
        

    def get_miles(self):
        try:
            miles = float(self.entry.get())
        except ValueError:
            self.result.configure(text="Please use Numbers only")
            return
        km1 = float(miles) * 1.6
        #shows precision up to 3 decimal places
        km = f"{km1:.3f}"
        self.result.configure(text=km) # For consistency, always use 'configure' instead.
        pyperclip.copy(km)

    def final_setup(self):
        
        # self.entry = Entry()
        # self.entry.focus()
        # self.entry.insert(END, "0")
        # self.entry.grid(row=0, column=1)

        # self.miles_label = Label(text="Miles")
        # self.miles_label.grid(row=0, column=2)

        # self.equal_label = Label(text="is equal to")
        # self.equal_label.grid(row=1, column=0)

        # self.result_label = Label(text="0")
        # self.result_label.grid(row=1, column=1)

        # self.km_label = Label(text="Km")
        # self.km_label.grid(row=1, column=2)

        # self.calculate_button = Button(text="Calculate", command=self.get_miles)
        # self.calculate_button.grid(row=2, column=1)
        
        
        self.entry=ctk.CTkEntry(self.window,placeholder_text="Miles",width=250,height=40,border_color="blue",border_width=1,bg_color="transparent",fg_color="#202020")
        self.entry.grid(row=0,column=0,padx=15,pady=(50,24))
        self.entry.focus()
        self.button=ctk.CTkButton(self.window,text="Convert",width=100,height=40,command=self.get_miles)
        self.button.grid(row=0,column=1,padx=0,pady=(50,24))
        barFrame=ctk.CTkFrame(self.window,width=250,height=40,border_color="blue",border_width=1,bg_color="transparent",fg_color="#202020")
        barFrame.grid(row=0,column=2,padx=15,pady=(50,24))
        barFrame.columnconfigure(0, weight=1)
        barFrame.rowconfigure(0, weight=1)
        self.result=ctk.CTkLabel(barFrame,width=250,height=40,anchor="w",text="Kilometers")
        self.result.grid(row=0,column=0,padx=2,pady=2,sticky="nsew")
        barLabel=ctk.CTkLabel(self.window,text="1 Mile = 1.6Km")
        barLabel.grid(row=1,column=1,pady=(0,20))
        

if __name__ == "__main__":
    converter = MileKmConverter()