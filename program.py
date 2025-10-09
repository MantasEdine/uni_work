Total_Money_In_Your_Card = 4000.0  

while True:
    user_input = input("Enter how much you want to retrieve from the account: ")
    
    try:
      
        withdrawal_amount = float(user_input)
        
    
        if withdrawal_amount <= 0:
            print("Please enter a positive value.")
            continue 
            
      
        if withdrawal_amount > Total_Money_In_Your_Card:
            print("You don't have enough balance.")
            new_user_input = input(f"You can only withdraw {Total_Money_In_Your_Card} DZA. Do you still want to withdraw all of it? (yes/no): ")
            
            if new_user_input.lower() == "yes":
                print(f"Here is your money: {Total_Money_In_Your_Card} DZA")
                Total_Money_In_Your_Card = 0.0
                print(f"Now your balance is {Total_Money_In_Your_Card} DZA.")
                break
            elif new_user_input.lower() == "no":
                print("Okay, have a nice day!")
                continue 
            else:
                print("Please enter 'yes' or 'no' only.")
                continue 
        
   
        elif withdrawal_amount == Total_Money_In_Your_Card:
            print(f"Here is your money: {Total_Money_In_Your_Card} DZA")
            Total_Money_In_Your_Card = 0.0
            print(f"Keep in mind that your new balance is {Total_Money_In_Your_Card} DZA.")
            break
            
    
        elif withdrawal_amount < Total_Money_In_Your_Card:
            print(f"Here is your money: {withdrawal_amount} DZA")
            Total_Money_In_Your_Card -= withdrawal_amount
            print(f"Now you still have: {Total_Money_In_Your_Card} DZA.")
            break

    except ValueError:
        print("Please enter a logical numeric value.")

