# -------------------------------
# Simple Expense Tracker Program
# -------------------------------

expenses = []   # List to store all expenses


def add_expense():
    print("\n--- Add New Expense ---")
    
    name = input("Enter expense name: ").strip()
     
    # Validate amount input
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("❌ Invalid amount! Please enter a valid number.")
    
    # Standard categories
    categories = ["Food", "Travel", "Shopping", "Other"]
    print("Choose category: Food / Travel / Shopping / Other")
    
    category = input("Enter category: ").capitalize()
    if category not in categories:
        print("⚠️ Unknown category. Assigned to 'Other'.")
        category = "Other"

    # Create expense entry
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("✔ Expense added successfully!\n")


def view_expenses():
    print("\n===== ALL EXPENSES =====")

    if not expenses:
        print("No expenses recorded yet.\n")
        return

    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['name']:15} | ₹{e['amount']:7.2f} | Category: {e['category']}")

    print("-------------------------------\n")


import matplotlib.pyplot as plt

def expense_report():
    print("\n===== EXPENSE REPORT =====")

    if not expenses:
        print("No expenses to generate report.\n")
        return

    # Total expense calculation
    total = sum(e["amount"] for e in expenses)

    # Organizing category totals
    category_totals = {}
    for e in expenses:
        cat = e["category"]
        category_totals[cat] = category_totals.get(cat, 0) + e["amount"]

    print(f"Total Expenses: ₹{total:.2f}\n")

    print("Category-wise Breakdown (With Percentages):")
    percentages = {}
    for cat, amt in category_totals.items():
        percent = (amt / total) * 100
        percentages[cat] = percent
        print(f"- {cat:12}: ₹{amt:.2f} ({percent:.2f}%)")

    print("\n===== FEEDBACK =====")

    # Finding biggest spending category
    major_spender = max(category_totals, key=category_totals.get)
    major_percent = percentages[major_spender]

    if major_percent > 50:
        print(f"⚠️ You spent {major_percent:.1f}% on {major_spender}. Try reducing this category.")
    elif major_percent > 30:
        print(f"ℹ️ {major_percent:.1f}% of total expenses went to {major_spender}. Watch this category.")
    else:
        print("✅ Your spending is well-balanced across categories!")

    # Additional tips
    if percentages.get("Food", 0) > 35:
        print("🍽️ Food expenses are high. Meal planning may help save money.")
    if percentages.get("Travel", 0) > 30:
        print("🚌 Travel costs are high. Consider cheaper transport options.")
    if percentages.get("Shopping", 0) > 30:
        print("🛍️ Shopping costs are high. Consider reducing non-essential purchases.")

    print("-------------------------------\n")

    # PIE CHART DISPLAY
    labels = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(7, 7))
    plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Expense Breakdown by Category")
    plt.axis("equal")  # Makes pie chart circular
    plt.show()


def main():
    while True:
        print("=====================================")
        print("          EXPENSE TRACKER")
        print("=====================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Generate Expense Report")
        print("4. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-4): ")

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
            print("❌ Invalid choice. Please try again.\n")


# Run the program
main()
