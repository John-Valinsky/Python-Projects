from tkinter import messagebox

def calculate_tithe():
    try:
        income = float(entry_income.get())
        tithe_percentage = float(entry_percentage.get())
        tithe_amount = (tithe_percentage / 100) * income
        label_result.config(text=f"Tithe Amount: ₹{tithe_amount:,.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for income and percentage.")

# Main window
root = tk.Tk()
root.title("Tithe Calculator")
root.geometry("300x200")
root.resizable(False, False)

# Income entry
tk.Label(root, text="Enter Income:").pack(pady=5)
entry_income = tk.Entry(root)
entry_income.pack()

# Percentage entry
tk.Label(root, text="Tithe Percentage (%):").pack(pady=5)
entry_percentage = tk.Entry(root)
entry_percentage.insert(0, "10")  # Default 10%
entry_percentage.pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate_tithe).pack(pady=10)

# Result label
label_result = tk.Label(root, text="Tithe Amount: ₹0.00", font=("Arial", 12, "bold"))
label_result.pack(pady=5)

# Run app
root.mainloop()
