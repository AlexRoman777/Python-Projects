import tkinter as tk

calculation = ""  # The calculation string, which will be evaluated later on


def add_to_calculation(symbol):
    '''Adds the symbol to the calculation string'''
    global calculation  # Use the global variable
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    '''Evaluates the calculation string'''
    global calculation
    try:  # Try to evaluate the calculation string
        result = str(eval(calculation))  # Use eval() to calculate the string
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
        print(result)  # Print the result to the console as well
    except SyntaxError:  # If there is a syntax error, clear the field
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    '''Clears the field'''
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.title("Calculator")
root.geometry("250x250")
# Center the window on the screen
root.eval('tk::PlaceWindow . center')


text_result = tk.Text(root, height=3, width=16, font=("Arial", 24))
text_result.grid(columnspan=4, padx=5, pady=5)

# Use lambda to pass the number to the function
button_01 = tk.Button(root, text="1", command=lambda: add_to_calculation(1))
button_02 = tk.Button(root, text="2", command=lambda: add_to_calculation(2))
button_03 = tk.Button(root, text="3", command=lambda: add_to_calculation(3))
button_04 = tk.Button(root, text="4", command=lambda: add_to_calculation(4))
button_05 = tk.Button(root, text="5", command=lambda: add_to_calculation(5))
button_06 = tk.Button(root, text="6", command=lambda: add_to_calculation(6))
button_07 = tk.Button(root, text="7", command=lambda: add_to_calculation(7))
button_08 = tk.Button(root, text="8", command=lambda: add_to_calculation(8))
button_09 = tk.Button(root, text="9", command=lambda: add_to_calculation(9))
button_00 = tk.Button(root, text="0", command=lambda: add_to_calculation(0))

button_plus = tk.Button(
    root, text="+", command=lambda: add_to_calculation("+"))  # Use lambda to pass the symbol
button_minus = tk.Button(
    root, text="-", command=lambda: add_to_calculation("-"))
button_multiply = tk.Button(
    root, text="*", command=lambda: add_to_calculation("*"))
button_divide = tk.Button(
    root, text="/", command=lambda: add_to_calculation("/"))
button_equal = tk.Button(
    root, text="=", command=evaluate_calculation, width=10, font=("Arial", 14))
button_clear = tk.Button(
    root, text="Clear", command=clear_field, width=10, font=("Arial", 14))
button_par1 = tk.Button(
    root, text="(", command=lambda: add_to_calculation("("))
button_par2 = tk.Button(root, text=")",
                        command=lambda: add_to_calculation(")"))

button_01.grid(row=1, column=0)
button_02.grid(row=1, column=1)
button_03.grid(row=1, column=2)

button_04.grid(row=2, column=0)
button_05.grid(row=2, column=1)
button_06.grid(row=2, column=2)

button_07.grid(row=3, column=0)
button_08.grid(row=3, column=1)
button_09.grid(row=3, column=2)

button_par1.grid(row=4, column=0)
button_00.grid(row=4, column=1)
button_par2.grid(row=4, column=2)

button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=2, columnspan=2)

root.mainloop()
