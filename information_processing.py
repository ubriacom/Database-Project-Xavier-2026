import pymysql.cursors

def information_processing(conn):
	choice =-1
	while choice < 1 or choice > 3:
		choice = int(input("\nWhat information processing would you like to perform?\n" +
											"1. Enter, Update, Delete, or Search information about stores\n" +
											"2. Enter, Update, Delete, or Search information about customers / members\n" +
											"3. Enter, Update, Delete, or Search information about staff\n" + "\n"))
	if choice == 1:
		store_info(conn)
	elif choice == 2:
		customer_info(conn)
	elif choice == 3:
		staff_info(conn)
		

def store_info(conn):
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWould you like to enter, update or delete information?\n" +
					 "1. Enter\n" +
					 "2. Update\n" +
					 "3. Delete\n" +
					 "4. Search\n" + "\n"))
	if choice == 1:
		pass
	elif choice == 2:
		pass
	elif choice == 3:
		pass
	elif choice == 4:
		pass


def customer_info(conn):
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWould you like to enter, update or delete information?\n" +
					 "1. Enter\n" +
					 "2. Update\n" +
					 "3. Delete\n" +
					 "4. Search\n" + "\n"))
	if choice == 1:
		pass
	elif choice == 2:
		pass
	elif choice == 3:
		pass
	elif choice == 4:
		pass
		

def staff_info(conn):
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWould you like to enter, update or delete information?\n" +
					 "1. Enter\n" +
					 "2. Update\n" +
					 "3. Delete\n" +
					 "4. Search\n" + "\n"))
	if choice == 1:
		pass
	elif choice == 2:
		pass
	elif choice == 3:
		pass
	elif choice == 4:
		pass