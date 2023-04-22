import pandas as pd

def save():
    savings = float(input("Enter Savings: "))
    return savings 

def menu():
    print("Welcome to the menu")
    print("1. Add saving")
    print("2. Run rest of program")

def main():
    filename = 'savings.csv'
    menu()
    choice = input("Enter Choice: ")
    saving = pd.read_csv(filename)

    if choice == "1":
        saving_amount = save()
        add_save = pd.DataFrame({"Savings": [saving_amount]})
        saving = pd.concat([saving, add_save], ignore_index=True)
        last_save = saving['Savings'].iloc[-1]
        running_total = saving['Savings'].sum()

        print(f"Your total savings are: {running_total}")
        print(f"Your last savings amount is: {last_save}")
        
        saving.to_csv(filename, index=False)
    else:
        last_save = saving['Savings'].iloc[-1]
        running_total = saving['Savings'].sum()

        print(f"Your total savings are: {running_total}")
        print(f"Your last savings amount is: {last_save}")

if __name__ == "__main__":
    main()
