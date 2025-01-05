import os                            # Importing modules: OS module to check file existance
from datetime import datetime        # Importing datetime class from datetime module
ExpenseFile = "expenses.txt"         # Declaring a constant global variable (text file having all the data)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def validate_date(date):                               # Function for Date Validation
    try:                                               # try-except block such that program won't crash
        datetime.strptime(date, "%Y-%m-%d")            # Checks if date string is in correct format
        return True
    except ValueError:                                 # value error if incorrect value inputted like a string value
        return False
  
def validate_amount(amount):                           # Function for Amount Validation
    try:                                               # try-except block such that program won't crash
        return float(amount)>0                         # Convert amount string into float and check if amount is positive or not
    except ValueError:                                 # value error if incorrect value inputted like a string value
       return False
        
        
def add_expense():                                        # Function to Add Expense
    date = input("Enter date (YYYY-MM-DD): ")             # Input Date
    if not validate_date(date):                           # Checks if Date is Valid or not
        print("Invalid date format! Use YYYY-MM-DD.")
        return                                            # Returns back to Main Menu
    category = input("Enter category: ")                  # Input category
    amount = input("Enter amount: ")                      # Input category
    if not validate_amount(amount):                       # Checks if Amount is Valid or not
        print("Amount must be a positive number!")
        return                                            # Returns back to Main Menu

    with open(ExpenseFile, "a") as file:                  # Opens file in Append mode
        file.write(f"{date},{category},{amount}\n")       # Writes Data in File
    print("Expense added successfully!")                  
    
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def view_expenses():                                                                     # Function to View Expense
    if not os.path.exists(ExpenseFile):                                                  # Checks if file exists
        print("No expenses recorded.")
        return                                                                           # Returns back to Main Menu

    category_type = input("Enter category to filter by (or press Enter for all): ")      # Take category input for filtering
    total_expense = 0                                                                    
    print("\nExpenses:")                                                                 # Header For table
    print(f"{'Date':<12}{'Category':<15}{'Amount':<10}")                                 # Alignment and space for table
    print("-" * 37)

    with open(ExpenseFile, "r") as file:                                                 # Opens file in read mode
        for line in file:                                                                # Iterating through file
            date, category, amount = line.strip().split(",")
            if not category_type or category_type.lower() == category.lower():           # Checks if category is entered or not, if entered then lowercase string is compared
                print(f"{date:<12}{category:<15}{amount:<10}")
                total_expense = total_expense + float(amount)                            # Updates total amount

    print("-" * 37)
    print(f"Total Expense: {total_expense:.2f}")                                         # Prints total expence with upto two decimal places

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def delete_expense():                                                     # Function to View Expense
    if not os.path.exists(ExpenseFile):                                   # Checks if file exists
        print("No expenses recorded.")
        return

    view_expenses()                                                       # Calls view_expense() Function for easier deletion
    
    date = input("Enter the date of the expense to delete: ")             # User Input
    category = input("Enter the category of the expense to delete: ")
    amount = input("Enter the amount of the expense to delete: ")

    found = False                                                         # Variable declared
    with open(ExpenseFile, "r") as file:                                  # File open in Read mode
        lines = file.readlines()                                          # Read all lines from file and make a list called lines.

    with open(ExpenseFile, "w") as file:                                  # File open in Write mode (Erases previous content)
        for line in lines:                                                # Iterate through each line
            if line.strip() == f"{date},{category},{amount}":             # Condition for data match
                found = True
            else:
                file.write(line)                                          # If condition not satisfied, previous data is written back into the file

    if found:
        print("Expense deleted successfully!")
    else:
        print("Expense not found!")
    
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def validate_month(month):                                                                             # Function to validate Month   
    try:
        datetime.strptime(month, "%Y-%m")                                                              # try-except block to check format
        return True
    except ValueError:
        return False
    
def view_monthly_Expense():                                                                            # Function to View Monthly Expense
    month = input("Enter month (YYYY-MM): ")
    if not validate_month(month):
        print("Invalid month format! Use YYYY-MM.")
        return

    total_expense = 0                                                                                  # Variable initialised
    category_totals = {}                                                                               # Empty dictionary created 

    if os.path.exists(ExpenseFile):                                                                    # hecks if file exist
        with open(ExpenseFile, "r") as file:                                                           # Opens file in Read mode
            for line in file:                                                                          # Iteration through file
                date, category, amount = line.strip().split(",")                                       # Input Values for variables
                if date.startswith(month):                                                             # Condition to check if date string starts with user entered month
                    total_expense += float(amount)                                                     # Adds amount to total expense
                    category_totals[category] = category_totals.get(category, 0) + float(amount)       # Update category_totals dictionary

    print(f"\nMonthly Summary for {month}:")
    print(f"Total Expense: {total_expense:.2f}")                                                       # Display total expense upto two decimal places
    print("By Category:")
    for category, amount in category_totals.items():                                                   # Loops through category total dictionary to display category
        print(f"{category}: {amount:.2f}")                                                             # Prints category and amount upto two decimal places

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def main_menu():                                   # Main Menu function
    if not os.path.exists(ExpenseFile):            # Checking if file exists
        with open(ExpenseFile, "w"):               # If not then file is created by opening file in write mode
            pass

    while True:                                    # Main Menu Structure (infinite loop)
        print("\nPersonal Expense Tracker")        # This code will always run as while condition remains true
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. View Monthly Expense")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()                          # Calls the add_expense() function
        elif choice == "2":
            view_expenses()                        # Calls the view_expense() function
        elif choice == "3":
            delete_expense()                       # Calls the delete_expense() function
        elif choice == "4":
            view_monthly_Expense()                 # Calls the view_monthly_expense() function
        elif choice == "5":
            print("Exiting... Goodbye!")
            break                                  # Exits the Main Menu function
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":                          # Command to execute Main Menu as soon as python code runs
    main_menu()

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx