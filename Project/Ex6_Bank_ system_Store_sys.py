import sys
import json
import time


def overwrite_data():    
    with open(file_path, 'w') as file:
        json.dump(data, file)


file_path = "Bank_amount.json"
data = {
    "t_balance" : 0
}

try:
    with open(file_path, 'x') as file:
        json.dump(data, file)
except FileExistsError:
    pass


try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Data file not found, can't continue to proceed further!")
    sys.exit()
except PermissionError:
    print("System don't have persmission to access the data file, can't proceed further!")
    sys.exit()



pause_time = 1.25
print("Welcome to Simple Bank System!")
while True:

    print("HOMEPAGE\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")

    try:
        option = int(input('Choose an option (1-4): '))
    except ValueError:
        print("Invalid Input! Words is not valid. Please select a number between 1 to 4.\n")
        continue

    if option == 1:
        print(f"\nYour Bank Balance is: ${data["t_balance"]:,}")

        while True:
            try:
                num = int(input('Enter 0 to Go Back: '))
            except ValueError:
                print("Invalid Input! Please enter 0 (zero), to Go Back HOMEPAGE.\n")
                continue
                
            if num == 0:
                print('Returned to HOMEPAGE\n')
                break
            else:
                print("Invalid Input! Please enter 0 (zero), to Go Back HOMEPAGE.\n")

    elif option == 2:
        while True:
            print('\nEnter $0, to go back')
            try:
                amount_depo = int(input('Enter the amount to deposit: $'))
            except ValueError:
                print("Invalid Input! Words is not valid. Please use values to deposit the amount.\n")
                continue

            if amount_depo == 0:
                print('Returned back to HOMEPAGE\n')
                break
            elif amount_depo > 0:
                data["t_balance"] += amount_depo
                print(f"${amount_depo:,} deposited successfully!\n")
                overwrite_data()
                for i in [3]:
                    dot=''
                    for _ in range(i):
                        dot += "."
                        print(dot, end="\r", flush=True)
                        time.sleep(pause_time)
                break
            else:
                print("Invalid! Negative input can't be used!\n")
                
                
    elif option == 3:
        while True:
            print('\nEnter $0, to go back')
            try:
                amount_withdr = int(input('Enter the amount to withdraw: $'))
            except ValueError:
                print("Invalid Input! Words is not valid. Please use values to withdraw the amount.\n")
                continue

            if amount_withdr == 0:
                print('Returned back to HOMEPAGE\n')
                break

            #Maintain Order always. First need to check the balance then withdrawal process.
            elif data["t_balance"] < amount_withdr:
                    print("Sorry, cannot be withdrawn due to insufficient balance in your account.\n")
            elif amount_withdr > 0:
                data["t_balance"] -= amount_withdr
                print(f"${amount_withdr:,} withdrawn successfully!\n")
                overwrite_data()
                for i in [3]:
                    dot=''
                    for _ in range(i):
                        dot += "."
                        print(dot, end="\r", flush=True)
                        time.sleep(pause_time)
                break

            else:
                print("Invalid! Negative input can't be used!\n")
                

    elif option == 4:
        overwrite_data()

        print('\nThank you for using The Simple Bank system!\n')
        break

    else:
        print("Invalid Choice! Please select a number between 1 to 4.\n")
