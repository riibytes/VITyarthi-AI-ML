# Simple Expense Tracker Program

expenses = []   # list to store expenses

def add_expense():
    print("\nAdd New Expense")

    name = input("Enter expense name: ")

    # amount validation
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except:
            print("Invalid amount, try again.")

    print("Categories: Food, Travel, Shopping, Other")
    category = input("Enter category: ").capitalize()

    if category not in ["Food", "Travel", "Shopping", "Other"]:
        category = "Other"

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added.\n")


def view_expenses():
    print("\nAll Expenses:\n")

    if len(expenses) == 0:
        print("No expenses yet.\n")
        return

    for i in range(len(expenses)):
        e = expenses[i]
        print(i+1, ".", e["name"], "| Rs.", e["amount"], "| Category:", e["category"])

    print()


import matplotlib.pyplot as plt

def expense_report():
    print("\nExpense Report:\n")

    if len(expenses) == 0:
        print("No expenses to show.\n")
        return

    total = 0
    for e in expenses:
        total += e["amount"]

    print("Total Expenses = Rs.", total)
    print()

    category_totals = {}

    for e in expenses:
        cat = e["category"]
        if cat not in category_totals:
            category_totals[cat] = 0
        category_totals[cat] += e["amount"]

    # print category wise amounts
    for cat in category_totals:
        amt = category_totals[cat]
        percent = (amt / total) * 100
        print(cat, "=", amt, "(", round(percent, 2), "% )")

    print()

    # some basic feedback
    biggest = max(category_totals, key=category_totals.get)

    print("You spent the most on:", biggest)

    # pie chart
    labels = list(category_totals.keys())
    values = list(category_totals.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Expense Breakdown")
    plt.show()


def main():
    while True:
        print("----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Expense Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_report()
        elif choice == "4":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice.\n")


main()