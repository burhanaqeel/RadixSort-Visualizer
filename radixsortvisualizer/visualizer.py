import tkinter as tk
from tkinter import ttk
import json
import math


def counting_sort(arr, exp, pass_num, text_widget, all_passes):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

    pass_output = {f"{ordinal(pass_num)} pass": arr.copy()}
    text_widget.insert(tk.END, json.dumps(pass_output, indent=4) + "\n")

    all_passes.append(arr.copy())


def radix_sort(arr, text_widget, size_entry, array_entry):
    try:
        size = int(size_entry.get())
        if size <= 0:
            text_widget.insert(tk.END, "Error: Array size must be positive.\n")
            return
    except ValueError:
        text_widget.insert(tk.END, "Error: Please enter a valid number for array size.\n")
        return

    try:
        arr = [int(x) for x in array_entry.get().split()]
        if len(arr) != size:
            text_widget.insert(tk.END, f"Error: Input array has {len(arr)} elements, but you specified size {size}.\n")
            return
        if any(x < 0 for x in arr):
            text_widget.insert(tk.END, "Warning: Negative numbers detected. This implementation works best with non-negative integers.\n")
    except ValueError:
        text_widget.insert(tk.END, "Error: Invalid input. Please enter space-separated integers.\n")
        return

    if not arr:
        text_widget.insert(tk.END, "Error: Empty array.\n")
        return

    text_widget.insert(tk.END, f"The Array: {str(tuple(arr))}\n\n")

    max_num = max(arr)
    
    # Calculate number of digits in the largest number
    if max_num == 0:
        num_digits = 1
    else:
        num_digits = int(math.log10(max_num)) + 1
    
    all_passes = []
    
    # Perform counting sort for each digit place
    exp = 1
    for i in range(num_digits):
        text_widget.insert(tk.END, f"Processing {ordinal(i+1)} digit (from right)...\n")
        counting_sort(arr, exp, i+1, text_widget, all_passes)
        exp *= 10

    text_widget.insert(tk.END, "\nSo the Sorted Array is " + str(tuple(all_passes[-1])) + "\n")


def reset_visualizer(size_entry, array_entry, text_widget):
    size_entry.delete(0, tk.END)
    array_entry.delete(0, tk.END)
    text_widget.delete(1.0, tk.END)


def ordinal(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return f"{num}{suffix}"


def main():
    root = tk.Tk()
    root.title("Radix Sort Visualization")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 800
    window_height = 600
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    title_label = tk.Label(root, text="Radix Sort Visualizer", font=("Helvetica", 20, "bold"))
    title_label.pack(pady=(15, 5))
    
    subtitle_label = tk.Label(root, text="A step-by-step visualization of the Radix Sort algorithm", 
                             font=("Helvetica", 12))
    subtitle_label.pack(pady=(0, 10))

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    text_widget = tk.Text(frame, height=20, width=70, wrap=tk.WORD)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text_widget.yview)
    text_widget.configure(yscrollcommand=scrollbar.set)
    
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    input_frame = ttk.Frame(root)
    input_frame.pack(fill=tk.X, padx=20, pady=10)

    size_label = ttk.Label(input_frame, text="Enter size of the array:")
    size_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

    size_entry = ttk.Entry(input_frame)
    size_entry.grid(row=0, column=1, padx=5, pady=5)

    array_label = ttk.Label(input_frame, text="Enter the array (space-separated):")
    array_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    array_entry = ttk.Entry(input_frame, width=40)
    array_entry.grid(row=1, column=1, padx=5, pady=5)

    button_frame = ttk.Frame(root)
    button_frame.pack(fill=tk.X, padx=20, pady=(0, 20))

    sort_button = ttk.Button(button_frame, text="Start Sorting",
                             command=lambda: radix_sort([], text_widget, size_entry, array_entry))
    sort_button.pack(side=tk.LEFT, padx=10)

    reset_button = ttk.Button(button_frame, text="Reset",
                              command=lambda: reset_visualizer(size_entry, array_entry, text_widget))
    reset_button.pack(side=tk.LEFT, padx=10)

    # Add a sample input button
    def insert_sample():
        size_entry.delete(0, tk.END)
        array_entry.delete(0, tk.END)
        size_entry.insert(0, "5")
        array_entry.insert(0, "170 45 75 90 802")
        
    sample_button = ttk.Button(button_frame, text="Load Sample", command=insert_sample)
    sample_button.pack(side=tk.LEFT, padx=10)

    # Add a status bar
    status_bar = ttk.Label(root, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    root.mainloop()


if __name__ == "__main__":
    main() 