import tkinter as tk
from tkinter import ttk
import pyodbc
from datetime import datetime

def submit_transaction():
    # Retrieve values from the entry fields
    transaction_date = entry_date.get()
    particulars = entry_particulars.get()
    debit_amount = entry_debit_amount.get()
    credit_amount = entry_credit_amount.get()
    narration = entry_narration.get()
    remarks = entry_remarks.get()
    added_by = entry_added_by.get()

    # Connect to the SQL Server database
    connection_string = "DRIVER={SQL Server};SERVER=MESSI\SQLEXPRESS;DATABASE=AccountingSoftware;UID=MESSI\khana;PWD=''"
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Insert the data into the database
    insert_query = """
        INSERT INTO Transactions (TransactionDate, Particulars, DebitAmount, CreditAmount, Narration, Remarks, AddedBy, InsertedAt, UpdatedAt)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    current_time = datetime.now()
    cursor.execute(insert_query, (transaction_date, particulars, debit_amount, credit_amount, narration, remarks, added_by, current_time, current_time))
    connection.commit()

    # Close the database connection
    cursor.close()
    connection.close()

    print("Transaction Date:", transaction_date)
    print("Particulars:", particulars)
    print("Debit Amount:", debit_amount)
    print("Credit Amount:", credit_amount)
    print("Narration:", narration)
    print("Remarks:", remarks)
    print("Added By:", added_by)

    # Clear the entry fields after submitting
    entry_particulars.delete(0, tk.END)
    entry_debit_amount.delete(0, tk.END)
    entry_credit_amount.delete(0, tk.END)

    # Add the submitted values to the treeview table
    tree.insert("", "end", values=(transaction_date, particulars, debit_amount, credit_amount))

# Create the main window
window = tk.Tk()
window.title("Accounting Software")

# Create and place Entry widgets for each field
entry_date = tk.Entry(window)
entry_particulars = tk.Entry(window)
entry_debit_amount = tk.Entry(window)
entry_credit_amount = tk.Entry(window)
entry_narration = tk.Entry(window)
entry_remarks = tk.Entry(window)
entry_added_by = tk.Entry(window)

# Place the Entry widgets in the window using grid
entry_date.grid(row=0, column=1)
entry_particulars.grid(row=1, column=1)
entry_debit_amount.grid(row=2, column=1)
entry_credit_amount.grid(row=3, column=1)
# ... (repeat for other Entry widgets)

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=submit_transaction)

# Place the submit button in the window using grid
submit_button.grid(row=4, column=0, columnspan=2)

# Create the treeview table
columns = ("Transaction Date", "Particulars", "Debit Amount", "Credit Amount")
tree = ttk.Treeview(window, columns=columns, show="headings")

# Set the column headings
for col in columns:
    tree.heading(col, text=col)

# Place the treeview table in the window using grid
tree.grid(row=5, column=0, columnspan=2)

# Start the main event loop
window.mainloop()
