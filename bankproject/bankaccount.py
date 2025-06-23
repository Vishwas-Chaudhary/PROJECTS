# Simple Banking Transaction System by Vishwas Chaudhary
# For any questions regarding this project please feel free to contact me :: vishwaschaudhary941@gmail.com
# path on pc::::D:\PRGS\projects\bankproject\bankaccount.py
from tkinter import *
from tkinter import messagebox, simpledialog


class BankSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank Management System")
        self.master.geometry("450x400")
        self.master.configure(bg="#D8E2DC")

        self.users = {}

        # Title Label
        self.title_label = Label(self.master, text="Welcome to Bank Management System", font=('Arial', 16, 'bold'), bg="#D8E2DC", fg="#3D405B")
        self.title_label.pack(pady=10)

        # Create Account Frame
        self.create_account_frame = Frame(self.master, bg='#D8E2DC')
        self.create_account_frame.pack(pady=20)

        # Labels and Entries for Create Account
        self.name_label = Label(self.create_account_frame, text="Name:", font=('Arial', 12), bg='#D8E2DC')
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.name_entry = Entry(self.create_account_frame, font=('Arial', 12), width=25)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.age_label = Label(self.create_account_frame, text="Age:", font=('Arial', 12), bg='#D8E2DC')
        self.age_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.age_entry = Entry(self.create_account_frame, font=('Arial', 12), width=25)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        self.salary_label = Label(self.create_account_frame, text="Salary:", font=('Arial', 12), bg='#D8E2DC')
        self.salary_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.salary_entry = Entry(self.create_account_frame, font=('Arial', 12), width=25)
        self.salary_entry.grid(row=2, column=1, padx=10, pady=5)

        self.pin_label = Label(self.create_account_frame, text="PIN:", font=('Arial', 12), bg='#D8E2DC')
        self.pin_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.pin_entry = Entry(self.create_account_frame, show="*", font=('Arial', 12), width=25)
        self.pin_entry.grid(row=3, column=1, padx=10, pady=5)

        # Create Account Button
        self.create_account_button = Button(self.create_account_frame, text="Create Account", font=('Arial', 12, 'bold'), bg='#4CAF50', fg='#FFFFFF', relief='raised', command=self.create_account)
        self.create_account_button.grid(row=4, column=1, pady=15, sticky=E)

        # Login Frame
        self.login_frame = Frame(self.master, bg="#D8E2DC")
        self.login_frame.pack(pady=10)
        self.login_name_label = Label(self.login_frame, text="Name:", font=("Arial", 12), bg="#D8E2DC")
        self.login_name_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.login_name_entry = Entry(self.login_frame, font=("Arial", 12), width=25)
        self.login_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.login_pin_label = Label(self.login_frame, text="PIN:", font=("Arial", 12), bg="#D8E2DC")
        self.login_pin_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.login_pin_entry = Entry(self.login_frame, show="*", font=("Arial", 12), width=25)
        self.login_pin_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = Button(self.login_frame, text="Login", font=('Arial', 12, 'bold'), bg='#4CAF50', fg='#FFFFFF', relief='raised', command=self.login)
        self.login_button.grid(row=2, column=1, padx=10, pady=15, sticky=E)

        # User Details Frame
        self.user_details_frame = Frame(self.master, bg="#D8E2DC")
        
        # Display Labels for User Details
        label_style = {"fg": "#3D405B", "font": ("Arial", 12, "bold"), "bg": "#D8E2DC"}
        self.name_label2 = Label(self.user_details_frame, text="Name:", **label_style)
        self.name_label2.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.age_label2 = Label(self.user_details_frame, text="Age:", **label_style)
        self.age_label2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.salary_label2 = Label(self.user_details_frame, text="Salary:", **label_style)
        self.salary_label2.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.current_balance_label = Label(self.user_details_frame, text="Current Balance:", **label_style)
        self.current_balance_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        # Action Buttons
        self.deposit_button = Button(self.user_details_frame, text="Deposit", command=self.deposit, bg="#FFC857", font=('Arial', 10, 'bold'))
        self.deposit_button.grid(row=4, column=0, padx=10, pady=10)
        self.withdraw_button = Button(self.user_details_frame, text="Withdraw", command=self.withdraw, bg="#E63946", fg="white", font=('Arial', 10, 'bold'))
        self.withdraw_button.grid(row=4, column=1, padx=10, pady=10)
        self.view_transaction_button = Button(self.user_details_frame, text="View Transaction Log", command=self.view_transaction_log, bg="#3A86FF", fg="white", font=('Arial', 10, 'bold'))
        self.view_transaction_button.grid(row=4, column=2, padx=10, pady=10)
        self.logout_button = Button(self.user_details_frame, text="Logout", command=self.logout, bg="gray", fg="white", font=('Arial', 10, 'bold'))
        self.logout_button.grid(row=5, column=2, padx=10, pady=10)

    def create_account(self):
        name, age, salary, pin = self.name_entry.get(), self.age_entry.get(), self.salary_entry.get(), self.pin_entry.get()
        if not name or not age.isdigit() or not salary.isdigit() or not pin.isdigit() or len(pin) != 4:
            messagebox.showerror("Error", "Please provide valid input in all fields.")
            return

        self.users[pin] = {'name': name, 'age': age, 'salary': salary, 'balance': 0, 'transactions': []}
        self.name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.salary_entry.delete(0, END)
        self.pin_entry.delete(0, END)
        messagebox.showinfo("Success", "Account created successfully!")

    def login(self):
        name, pin = self.login_name_entry.get(), self.login_pin_entry.get()
        user_data = self.users.get(pin)
        if user_data and user_data['name'] == name:
            self.user_details_frame.pack(pady=20)
            self.name_label2['text'] = f"Name: {user_data['name']}"
            self.age_label2['text'] = f"Age: {user_data['age']}"
            self.salary_label2['text'] = f"Salary: {user_data['salary']}"
            self.current_balance_label['text'] = f"Current Balance: {user_data['balance']}"
            self.login_frame.pack_forget()
        else:
            messagebox.showerror("Error", "Invalid credentials.")

    def deposit(self):
        pin = simpledialog.askstring("Deposit", "Enter PIN:")
        amount = simpledialog.askinteger("Deposit", "Enter amount:")
        user_data = self.users.get(pin)
        if user_data and amount:
            user_data['balance'] += amount
            user_data['transactions'].append(f"Deposit: +{amount}")
            self.current_balance_label.config(text=f"Current Balance: {user_data['balance']}")
        else:
            messagebox.showerror("Error", "Invalid PIN or amount.")

    def withdraw(self):
        pin = simpledialog.askstring("Withdraw", "Enter PIN:")
        amount = simpledialog.askinteger("Withdraw", "Enter amount:")
        user_data = self.users.get(pin)
        if user_data and amount and user_data['balance'] >= amount:
            user_data['balance'] -= amount
            user_data['transactions'].append(f"Withdraw: -{amount}")
            self.current_balance_label.config(text=f"Current Balance: {user_data['balance']}")
        else:
            messagebox.showerror("Error", "Invalid transaction.")

    def view_transaction_log(self):
        pin = simpledialog.askstring("View Transactions", "Enter PIN:")
        user_data = self.users.get(pin)
        if user_data:
            transactions = '\n'.join(user_data['transactions']) or "No transactions yet."
            messagebox.showinfo("Transaction Log", transactions)
        else:
            messagebox.showerror("Error", "Invalid PIN.")

    def logout(self):
        self.user_details_frame.pack_forget()
        self.login_frame.pack(pady=10)
        messagebox.showinfo("Logout", "Logged out successfully!")


root = Tk()
app = BankSystem(root)
root.mainloop()
