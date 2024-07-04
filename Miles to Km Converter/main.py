from tkinter import *
import pyperclip

class MileKmConverter:
    def __init__(self):
        self.setup_window()
        self.final_setup()
        self.window.mainloop()

    def setup_window(self):
        self.window = Tk()
        self.window.title("Mile to Km Converter")
        self.window.config(padx=20, pady=20)
        self.window.minsize(width=350, height=100)
        self.window.maxsize(width=350, height=100)

    def get_miles(self):
        miles = self.entry.get()
        km1 = float(miles) * 1.6
        #shows precision up to 3 decimal places
        km = f"{km1:.3f}"
        self.result_label.config(text=km)
        pyperclip.copy(km1)
    def final_setup(self):
        self.entry = Entry()
        self.entry.focus()
        self.entry.insert(END, "0")
        self.entry.grid(row=0, column=1)

        self.miles_label = Label(text="Miles")
        self.miles_label.grid(row=0, column=2)

        self.equal_label = Label(text="is equal to")
        self.equal_label.grid(row=1, column=0)

        self.result_label = Label(text="0")
        self.result_label.grid(row=1, column=1)

        self.km_label = Label(text="Km")
        self.km_label.grid(row=1, column=2)

        self.calculate_button = Button(text="Calculate", command=self.get_miles)
        self.calculate_button.grid(row=2, column=1)

if __name__ == "__main__":
    converter = MileKmConverter()