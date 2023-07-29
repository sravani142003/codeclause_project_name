import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack()

        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.display_label = tk.Label(self.display_frame, textvariable=self.display_var, font=("Arial", 20))
        self.display_label.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.button_frame, text=text, font=("Arial", 20), padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.expression)
                self.expression = str(result)
                self.display_var.set(self.expression)
            except Exception as e:
                self.expression = ""
                self.display_var.set("Error")
        else:
            if value == 'C':
                self.expression = ""
            elif value == 'DEL':
                self.expression = self.expression[:-1]
            else:
                self.expression += value
            self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
