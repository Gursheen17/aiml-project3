import tkinter as tk
from tkinter import messagebox
import matplotlib
matplotlib.use('TkAgg')  # IMPORTANT for Spyder

import matplotlib.pyplot as plt
from collections import defaultdict

# Data storage
expenses = []
categories = defaultdict(float)

# Add Expense
def add_expense():
    try:
        amount = float(entry_amount.get())
        category = category_var.get()

        if amount <= 0:
            messagebox.showerror("Error", "Enter valid amount!")
            return

        expenses.append(amount)
        categories[category] += amount

        history_box.insert(tk.END, f"{category} → ₹{amount}")
        update_summary()

        entry_amount.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Invalid input!")

# Update Summary
def update_summary():
    total = sum(expenses)

    try:
        budget = float(entry_budget.get())
    except:
        budget = 0

    savings = budget - total

    summary_label.config(
        text=f"Total Expense: ₹{total:.2f} | Savings: ₹{savings:.2f}"
    )

    generate_ai_tip(total, budget)

# AI Suggestions
def generate_ai_tip(total, budget):
    if budget == 0:
        tip = "⚠️ Please set a budget!"
    elif total > budget:
        tip = "🚨 Budget exceeded! Reduce spending."
    elif total > 0.75 * budget:
        tip = "⚠️ Near budget limit!"
    elif total > 0.4 * budget:
        tip = "💡 Moderate spending."
    else:
        tip = "✅ Great saving habit!"

    tip_label.config(text=tip)

# Pie Chart
def show_pie_chart():
    if not categories:
        messagebox.showerror("Error", "No data!")
        return

    plt.figure()
    plt.pie(list(categories.values()), labels=list(categories.keys()), autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.tight_layout()
    plt.show(block=True)

# Bar Graph
def show_bar_graph():
    if not categories:
        messagebox.showerror("Error", "No data!")
        return

    plt.figure()
    plt.bar(list(categories.keys()), list(categories.values()))
    plt.title("Category-wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show(block=True)

# Trend Graph
def show_trend():
    if not expenses:
        messagebox.showerror("Error", "No data!")
        return

    plt.figure()
    plt.plot(expenses, marker='o')
    plt.title("Expense Trend")
    plt.xlabel("Entries")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show(block=True)

# Clear All
def clear_all():
    expenses.clear()
    categories.clear()
    history_box.delete(0, tk.END)
    summary_label.config(text="")
    tip_label.config(text="")

# GUI Setup
root = tk.Tk()
root.title("Smart Expense Analyzer 🍫")
root.geometry("750x600")
root.config(bg="#3e2723")

# Title
tk.Label(root, text="Smart Expense Analyzer 🍫",
         font=("Arial", 20, "bold"),
         bg="#3e2723", fg="#efebe9").pack(pady=10)

# Budget Input
tk.Label(root, text="Set Budget:",
         bg="#3e2723", fg="#efebe9").pack()
entry_budget = tk.Entry(root, bg="#d7ccc8")
entry_budget.pack(pady=5)

# Input Frame
frame = tk.Frame(root, bg="#5d4037")
frame.pack(pady=10)

tk.Label(frame, text="Amount:", bg="#5d4037", fg="#efebe9").grid(row=0, column=0, padx=10, pady=5)
entry_amount = tk.Entry(frame, bg="#d7ccc8")
entry_amount.grid(row=0, column=1)

tk.Label(frame, text="Category:", bg="#5d4037", fg="#efebe9").grid(row=1, column=0, padx=10, pady=5)

category_var = tk.StringVar()
category_var.set("Food")

category_menu = tk.OptionMenu(frame, category_var,
                              "Food", "Travel", "Shopping", "Bills", "Other")
category_menu.config(bg="#8d6e63", fg="white")
category_menu.grid(row=1, column=1)

# Buttons
btn_frame = tk.Frame(root, bg="#3e2723")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Expense", bg="#8d6e63", fg="white",
          command=add_expense).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Pie Chart", bg="#8d6e63", fg="white",
          command=show_pie_chart).grid(row=0, column=1, padx=10)

tk.Button(btn_frame, text="Bar Graph", bg="#8d6e63", fg="white",
          command=show_bar_graph).grid(row=0, column=2, padx=10)

tk.Button(btn_frame, text="Trend Graph", bg="#8d6e63", fg="white",
          command=show_trend).grid(row=0, column=3, padx=10)

tk.Button(btn_frame, text="Clear", bg="#a1887f", fg="white",
          command=clear_all).grid(row=0, column=4, padx=10)

# Summary
summary_label = tk.Label(root, text="",
                        bg="#3e2723", fg="#efebe9",
                        font=("Arial", 12))
summary_label.pack(pady=10)

# AI Tip
tip_label = tk.Label(root, text="",
                    bg="#3e2723", fg="#efebe9",
                    font=("Arial", 12, "italic"))
tip_label.pack(pady=5)

# History
tk.Label(root, text="History",
         bg="#3e2723", fg="#efebe9",
         font=("Arial", 14, "bold")).pack()

history_box = tk.Listbox(root, width=70, height=10, bg="#d7ccc8")
history_box.pack(pady=10)

root.mainloop()