import tkinter as tk

def calculate_growth():
    try:
        initial_value = float(entry_initial_value.get())
        growth_period = int(entry_growth_period.get())
        
        result = initial_value * (3 ** growth_period)
        result_label.config(text=f"Final Value: {result:.4f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numerical values.")

# Create the main window
window = tk.Tk()
window.title("Exponential Growth Calculator")

# Labels
label_initial_value = tk.Label(window, text="Initial Value (0-1):")
label_initial_value.pack(pady=5)

label_growth_period = tk.Label(window, text="Growth Period (Days):")
label_growth_period.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Entry widgets
entry_initial_value = tk.Entry(window)
entry_initial_value.pack(pady=5)

entry_growth_period = tk.Entry(window)
entry_growth_period.pack(pady=5)

# Button
calculate_button = tk.Button(window, text="Calculate", command=calculate_growth)
calculate_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
