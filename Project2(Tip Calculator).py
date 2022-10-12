print("Welcome to the tip calculator. ")
bill = float(input("What was your total bill? $")) 
tip = int(input("How much tip would you like to give? 10,12,15, or 20?"))
bill_with_tip = tip / 100 * bill + bill  
tip_as_percent = tip / 100 
total_tip_amount = bill * tip_as_percent 
split = int(input("How many people did you want to spilt the bill? ")) 
total_bill = (bill + total_tip_amount) / split
print("Each person should pay: ${} ".format(total_bill))