#GUI to solve quadratic equations
import tkinter.messagebox
from tkinter import *



class QuadraticEquations:
    def __init__(self):
        self.graphics()

    def find_solutions(self):
        finding_solution = True
        while finding_solution:
            quadratic = self.quadratic_input.get()
            linear = self.linear_input.get()
            constant = self.constant_input.get()

            if len(quadratic) == 0:

                tkinter.messagebox.showerror(message="This is not a quadratic equation")
                finding_solution = False
                break

            if len(linear) == 0:
                linear = 0

            if len(constant) == 0:
                constant = 0



            try:
                quadratic = float(quadratic)
            except ValueError:
                tkinter.messagebox.showerror(message="A wrong value was entered")
                finding_solution = False

            try:
                linear = float(linear)
            except ValueError:
                tkinter.messagebox.showerror(message="A wrong value was entered")
                finding_solution = False

            try:
                constant = float(constant)
            except ValueError:
                tkinter.messagebox.showerror(message="A wrong value was entered")
                finding_solution = False

            a = quadratic
            b = linear
            c = constant
            discriminant = (b**2)-(4*a*c)

            if discriminant < 0:
                tkinter.messagebox.showerror(message="The equation has no real roots")
            elif discriminant == 0:
                solution = (-b) / (2 * a)
                output = f"The equation has two repeated real roots\nThe solution is {solution}"
                tkinter.messagebox.showerror(message=output)
            else:
                sqrt_discriminant = discriminant ** 0.5
                solution1 = (-b + sqrt_discriminant) / (2 * a)
                solution2 = (-b - sqrt_discriminant) / (2 * a)
                output = f"The equation has two different real roots\nThe solutions are {solution1} and {solution2}"
                tkinter.messagebox.showerror(message=output)
            finding_solution = False

    def graphics(self):
        self.root= Tk()
        self.root.title("Quadratic Equations Solver")
        self.root.minsize(width=400,height=400)
        self.root.maxsize(width=400, height=400)
        self.quadratic_input = Entry(self.root,width=3)
        self.quadratic_input.place(x=75,y=100)
        self.quadratic_label = Label(text="x²")
        self.quadratic_label.place(x=120,y=100)


        self.linear_input = Entry(self.root, width=3)
        self.linear_input.place(x=150, y=100)
        self.linear_label = Label(text="x")
        self.linear_label.place(x=200, y=100)

        self.plus_label = Label(text="+")
        self.plus_label.place(x=220,y=100)

        self.constant_input = Entry(self.root, width=3)
        self.constant_input.place(x=250, y=100)

        self.calculate_button = Button(self.root,text="Find Solutions",command=self.find_solutions)
        self.calculate_button.place(x=130,y=200)

        self.root.mainloop()

if __name__ == "__main__":
    qe = QuadraticEquations()