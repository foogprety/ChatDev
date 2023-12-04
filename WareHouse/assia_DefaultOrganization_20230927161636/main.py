'''
Expense Tracker
This program allows users to input their expenses and visualize the data using a graphical user interface (GUI).
Author: ChatDev
Date: [current_date]
'''
import tkinter as tk
from tkinter import messagebox
class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.expenses = []
        self.create_widgets()
    def create_widgets(self):
        self.expense_label = tk.Label(self.root, text="Expense:")
        self.expense_label.pack()
        self.expense_entry = tk.Entry(self.root)
        self.expense_entry.pack()
        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()
        self.show_button = tk.Button(self.root, text="Show Expenses", command=self.show_expenses)
        self.show_button.pack()
    def add_expense(self):
        '''
        Add Expense
        This method is called when the "Add Expense" button is clicked. It retrieves the expense from the entry field,
        adds it to the expenses list, and displays a success message.
        '''
        expense = self.expense_entry.get()
        if expense:
            self.expenses.append(expense)
            messagebox.showinfo("Expense Tracker", "Expense added successfully!")
            self.expense_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Expense Tracker", "Please enter an expense.")
    def show_expenses(self):
        '''
        Show Expenses
        This method is called when the "Show Expenses" button is clicked. It displays all the expenses in a separate window.
        '''
        expenses_window = tk.Toplevel(self.root)
        expenses_window.title("Expenses")
        expenses_listbox = tk.Listbox(expenses_window)
        expenses_listbox.pack(fill=tk.BOTH, expand=True)
        for expense in self.expenses:
            expenses_listbox.insert(tk.END, expense)
        expenses_window.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()