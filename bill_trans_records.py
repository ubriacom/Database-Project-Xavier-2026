import pymysql.cursors

def bill_trans_records(conn):
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWhat records do you need from transactions and billing?\n" +
					 "1. Generate reward notices for members that are due at the end of each month\n" +
					 "2. Generate rewards checks for employees at the end of each quarter\n" +
					 "3. Transaction information including total price\n" + "\n"))
		if choice == 1:
			pass
		elif choice ==2:
			pass
		elif choice == 3:
			pass
		

