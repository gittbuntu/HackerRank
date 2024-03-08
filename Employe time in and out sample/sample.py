import tkinter as tk
from datetime import datetime
import psycopg2

# Function to calculate time difference
def calculate_time_difference(time_in_str, time_out_str):
    time_in = datetime.strptime(time_in_str, '%H:%M')
    # print(time_in)
    time_out = datetime.strptime(time_out_str, '%H:%M')
    # print(time_out)
    time_diff = time_out - time_in
    return str(time_diff)

date = str(datetime.today())
date = date[0:10]
# print(date)

# Function to save record to PostgreSQL database
def save_to_database(name, time_in, time_out, reason, time_difference, date):
    connection = psycopg2.connect(
        dbname="employee_timing_data",
        user="employeetiming",
        password="employeetiming",
        host="localhost"
    )

    cursor = connection.cursor()
    cursor.execute("INSERT INTO employee_records (name, time_in, time_out, reason, time_difference, date) VALUES (%s, %s, %s, %s, %s, %s)",
                   (name, time_in, time_out, reason, time_difference, date))
    connection.commit()
    connection.close()

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    time_in = time_in_entry.get()
    time_out = time_out_entry.get()
    reason = reason_var.get()
    
    time_difference = calculate_time_difference(time_in, time_out)
    
    save_to_database(name, time_in, time_out, reason, time_difference, date)
    result_label.config(text=f"Name = {name}\nReason = {reason}\nTime = {time_difference}\nDate = {date}\nRecord saved successfully.")

# Function to print a single record
def print_record():
    name = name_entry.get()
    time_in = time_in_entry.get()
    time_out = time_out_entry.get()
    reason = reason_var.get()
    time_difference = calculate_time_difference(time_in, time_out)
    
    print(f"Name: {name}")
    print(f"Time In: {time_in}")
    print(f"Time Out: {time_out}")
    print(f"Reason: {reason}")
    print(f"Time Difference: {time_difference}")

# Create main window
root = tk.Tk()
root.title("Employee Time Record Form")

# Create form labels and entries
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Time In (HH:MM):").grid(row=1, column=0)
time_in_entry = tk.Entry(root, width=40)
time_in_entry.grid(row=1, column=1)

tk.Label(root, text="Time Out (HH:MM):").grid(row=2, column=0)
time_out_entry = tk.Entry(root, width=40)
time_out_entry.grid(row=2, column=1)


tk.Label(root, text="Reason:").grid(row=3, column=0)
reason_options = ["Present", "Lunch", "Others"]  # Add your reasons here
reason_var = tk.StringVar(root)
reason_var.set(reason_options[0])
reason_dropdown = tk.OptionMenu(root, reason_var, *reason_options)
reason_dropdown.grid(row=3, column=1)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=4)

# Print button
print_button = tk.Button(root, text="Print", command=print_record)
print_button.grid(row=4, column=1, columnspan=2)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()

