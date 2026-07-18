#Expense Tracker Project

expensesList = [] #list of all expenses
print("Welcome to Expense Tracker : Mariana Garza")

while True: 
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Costs")
    print("4. Exit")

    choice= int(input("Please Enter Your Choice : "))

#ADD Expense
    if(choice == 1):
        date= input("When was it spent?: ")
        category= input("Type of Expense? (Food, Travel, Makeup, Books): ")
        description= input("Description details: ")
        amount= float(input("Enter the amount: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("Expense is added succesfully")

#2. VIEW ALL EXPENSES
    if(choice == 2):
        if( len(expensesList)==0 ):
            print("No Expenses Added.")
        else:
            print("===== These are all your expenses.=====")
            count= 1
            for eachExpense in expensesList:
                print(f"Expense Number {count} -> {eachExpense["date"]},{eachExpense["category"]}, {eachExpense["description"]}, {eachExpense["description"]} ")
                count= count+1

#3. View Total Spending
        if(choice == 3):
            for eachExpense in expensesList:
                total = total + eachExpense["amount"]  

        print("\n TOTAL EXPENSES = ", total)

#4. EXIT           
    elif(choice == 4):
        print("Thank you for using our system.")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN") 
            