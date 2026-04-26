#personal_finance_manager
import sys

def show_details():
    print("account details")
    for k,v in details.items():
        print(f"Name:{k}, Age:{v['age']}, Balance:{v['balance']}")


def add_user():
        name=input("Enter your name: ").lower().strip()
        try:
            age=int(input("Enter your age: "))
            balance=int(input("Enter your balance: "))
        except ValueError:
            print("invalid input. Please use numbers for age and balance")
            return
        if name in details:
            print("Account already exists")
            return
        else:
            details[name]={"age":age,"balance":balance}
            print("Account created successfully")
        return name,age,balance


def add_expense():
    name = input("Enter your name: ").lower().strip()
    if name not in details:
        print("Account does not exist")
        return

    mode = input("credit or debit? ").lower().strip()

    try:
        expense = int(input("Enter the amount: "))

        if mode == "debit":
            details[name]["balance"] -= expense
        else:
            details[name]["balance"] += expense

        print(f"Success! Current balance: {details[name]['balance']}")
    except ValueError:
        print("Invalid input. Please enter a whole number for the amount.")


def delete_entry():
    name=input("Enter your name: ").lower().strip()
    if name in details:
        confirm=input(f"are you sure you want to delete this account? {name} (y/n) ? ")
        if confirm.lower()=="y":
            details.pop(name)
    else:
        print("account does not exist")

def quit():
    print("Thank you for using personal finance tracker")
    sys.exit()


details={"karan":{"age":26,"balance":45000},
        "aswin":{"age":23,"balance":50000},
         "athul":{"age":25,"balance":36000}}

while True:
    print("Personal Finance Tracker")
    print("main menu")
    print("1.Show account details.\n 2.Add new user\n 3.Add expense \n 4.delete entry \n 5.Quit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            show_details()
        case "2":
            add_user()
        case "3":
            add_expense()
        case "4":
            delete_entry()
        case "5":
            quit()