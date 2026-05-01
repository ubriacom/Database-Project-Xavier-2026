import pymysql.cursors

def merch_inv_records(conn):
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWhat merchandise and inventory records would you like to change?\n" +
						"1. Enter, Update, or Delete information about products\n" +
						"2. Enter, Update, or Delete information about discounts\n" +
						"3. Increase, Remove, or search inventory for a specific product\n" + "\n"))
	return choice


def product_info(conn):
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWould you like to enter, update or delete information?\n" +
					 "1. Enter\n" +
					 "2. Update\n" +
					 "3. Delete\n" +
					 "4. Search\n" + "\n"))
	if choice == 1:
		enter_product(conn)
	elif choice == 2:
		update_product(conn)
	elif choice == 3:
		delete_product(conn)
	elif choice == 4:
		search_product(conn)
	

def discount_info(conn):
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWould you like to enter, update or delete information?\n" +
					 "1. Enter\n" +
					 "2. Update\n" +
					 "3. Delete\n" +
					 "4. Search\n" + "\n"))
	if choice == 1:
		enter_discount(conn)
	elif choice == 2:
		update_discount(conn)
	elif choice == 3:
		delete_discount(conn)
	elif choice == 4:
		search_discount(conn)
	

def enter_product(conn):
	pass


def update_product(conn):
	pass

def delete_product(conn):
	pass

def search_product(conn):
	pass



def enter_discount(conn):
	pass

def update_discount(conn):
	pass

def delete_discount(conn):
	pass

def search_discount(conn):
	pass