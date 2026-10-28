print("\n_______ATM MACHINE______")
while(True):
	print("\nWITHDRAW PROCESS TO CLICK NO 1:")
	print("\nDEPOSIT PROCESS TO CLICK NO 2:")
	print("\nSHOW BALANCE PROCESS CLICK NO 3:")
	
	set_pin=7397
	available_balance=int(input("\nPLEASE ENTER YOUR BALANCE:"))
	process=int(input("\nEnter the process:"))
	match process:
		case 1:
			your_pin=int(input("\nPLEASE ENTER YOUR PIN:"))
			withdraw_amount=int(input("\nEnter the withdraw amount:"))
			if set_pin==your_pin:
				if withdraw_amount>0:
					available_balance=available_balance-withdraw_amount
					print("\nprocess successfully")
					print("\nyour current balance is:",available_balance)
					print("\n Thank you for useing our survice:")
		case 2:
				your_pin=int(input("\nEnter your pin:"))
				
				if set_pin==your_pin:
					deposit_amount=int(input("\nEnter the deposit amount:"))
					if deposit_amount>0:
						available_balance+=deposit_amount
						print("\ndeposit process is successful")
						print("\nyour current balance is:",available_balance)
						print("\nThank you for useing our survice")
				else:
						print("\nplease enter currect pin number")
		case 3:
			your_pin=int(input("\nEnter your pin:"))
			
			if set_pin==your_pin:
				print("\nAvailable balance in your bank account is:",available_balance)
				print("\nThank you for useing our survice")
			else:
				print("\nEnenter your pin properly")
		
 					
						
						
				
					
					
				
					
			

	
