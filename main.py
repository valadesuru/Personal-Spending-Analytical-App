#stores all of the user's transactions in a dictionary (nested dictionary)
expenditures = {}
#a counter to keep track of the number of transactions - also used as the key for the expenditures dictionary
num_of_transactions = 1

while True:
    user_choice = input("Please choose an option:\n1. Add a transaction\n2. View transactions\n3. Total spending\n4. View spending by category\n5. Exit\n")

    #asks the user for the date, amount, category, and where the transaction went to and stores it in the expenditures dictionary
    if user_choice == "1":
        date = input("Enter the date of the transaction (DD-MM-YYYY): ")
        amount = round(float(input("Enter the amount of the transaction: ")), 2)
        category = input("Enter the category of the transaction (e.g., food, entertainment, bills): ")
        where = input("Enter where the transaction went to (e.g., store name, online platform): ")
        expenditures[num_of_transactions] = {"amount": amount, "category": category, "where": where}

    #prints the user's expenditures without showing the number of transcations which have occurred
    elif user_choice == "2":
        for transaction in expenditures.values():
            print(transaction)

    #prints the total spending by summing up the amounts of all transactions in the expenditures dictionary
    elif user_choice == "3":
        total_spending = sum(transaction["amount"] for transaction in expenditures.values())
        print(f"Total spending: ${total_spending:.2f}")

    #checks the expenditures dictionary and adds up the amounts for each category, then prints the total spending for each category
    elif user_choice == "4":
        category_spending = {}
        for transaction in expenditures.values():
            category = transaction["category"]
            amount = transaction["amount"]
            if category in category_spending:
                category_spending[category] += amount
            else:
                category_spending[category] = amount

        print("Spending by category:")
        for category, amount in category_spending.items():
            print(f"  {category}: ${amount:.2f}")

    #enables the user to exit the program
    elif user_choice == "5":
        print("Exiting the program. Goodbye!")
        break

    num_of_transactions += 1
