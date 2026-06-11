
import backend_calc as cl

DATA = {
    "username " : "admin",
    "pin" : "1234",
    "total_balance": 10000
}



def user_info(acc_no,ifsc_code):
    if acc_no and ifsc_code:
        return f"Account no : {acc_no}  IFSC code : {ifsc_code}"
    elif acc_no:
        return f"Account no : {acc_no}"
    
def withdraw(amount):
    if amount > DATA["total_balance"]:
        return("Insuffecient balance")
    
    else:
        DATA["total_balance"] = cl.withdraw_calc(DATA["total_balance"],amount)
        return f"withdrwal successfull , remaining balance {DATA["total_balance"]}"
    

def deposit(amount):
    DATA["total_balance"] = cl.deposit_calc(DATA["total_balance"],amount)
    return f"deposit successfull {DATA["total_balance"]}"

def check_balance():
    return f"total balance {DATA["total_balance"]}"

def main():
    pin_no = input("Enter your pin number : ")

    
    if pin_no == DATA["pin"]:
        print("authentication successfull")

        acc_no = input("Enter your account number : ")
        ifsc_code = input("Enter your IFSC code : ")
        print(f"user info{user_info(acc_no,ifsc_code)}")

        choice = input("Do you want to withdraw the amount (yes/no): ").lower()
        if choice == "yes":
            amount = int(input("Enter the amount : "))
            print(withdraw(amount))

        choice1 = input("Do you want to deposit(yes/no)").lower()
        if choice1 == "yes":
            amount = int(input("Enter the amount:"))
            print(deposit(amount))

        choice2 = input("Do you want to check the balance (yes/no):").lower()
        if choice2 == "yes":
            print("Total balance : ",DATA["total_balance"])

    else:
        print("account blocked")



if __name__ == "__main__":
    main()