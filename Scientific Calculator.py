import tkinter as tk
import math

# Function to perform the selected operation
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    
    if operation.get() == "Add":
        result.set(num1 + num2)
    elif operation.get() == "Subtract":
        result.set(num1 - num2)
    elif operation.get() == "Multiply":
        result.set(num1 * num2)
    elif operation.get() == "Divide":
        if num2 == 0:
            result.set("Cannot divide by zero")
        else:
            result.set(num1 / num2)
    elif operation.get() == "Square Root":
        result.set(math.sqrt(num1))
    elif operation.get() == "Power":
        result.set(num1 ** num2)
    elif operation.get() == "Sine":
        result.set(math.sin(num1))
    elif operation.get() == "Cosine":
        result.set(math.cos(num1))
    elif operation.get() == "Tangent":
        result.set(math.tan(num1))

# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")

# Create and pack the input fields
entry_num1 = tk.Entry(window)
entry_num1.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create a variable to hold the selected operation
operation = tk.StringVar()
operation.set("Add")

# Create and pack the operation menu
operation_menu = tk.OptionMenu(
    window,
    operation,
    "Add", "Subtract", "Multiply", "Divide",
    "Square Root", "Power", "Sine", "Cosine", "Tangent"
)
operation_menu.pack()

# Create a button to perform the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create a variable to display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()

# Start the Tkinter main loop
window.mainloop()