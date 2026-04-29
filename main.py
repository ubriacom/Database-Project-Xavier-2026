import pymysql.cursors

def main():
	conn = create_connection('MuskieCo')    # establish DB connection
	if conn is None:
		exit()
		

	choice = get_user_choice()  # ask the user what operation they want to perform
	
	# call the method corresponding to that operation
	if choice == 1:
		information_processing(conn)
	elif choice == 2:
		merch_inv_records(conn)
	elif choice == 3:
		pass # TODO: replace with method call
	elif choice == 4:
		pass # TODO: replace with method call

	conn.close() 	# close DB connection


def create_connection(database_name):
	""" 
	Create a connection to the given database 
	Returns:
		conn: Connection object
	"""

	try:
		conn = pymysql.connect(
			user='root',
			password='Atlanticocean1', # TODO: add your password here 
			host='127.0.0.1',
			database=database_name) 
			# autocommit = false by default
	except pymysql.Error as err:
		print('Cannot connect to database:', err)
		return None

	return conn


def get_user_choice():
	""" 
	Gets the operation the user wants to perform 
	Returns:
		choice: the number corresponding to the operation
	"""

	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWhat task would you like to perform:\n" +
								"1. Information Processing\n" +
								"2. Maintaining Merchandise and Inventory Records\n" +
								"3. Maintaining Billing and Transaction Records\n" +
                                "4. Reports\n" + "\n"))
	return choice

def read_string(prompt):
	""" 
	Reads a string from the user 
	Returns:
		the string entered
	"""
	return input(prompt)


def read_int(prompt):
	""" 
	Reads an int from the user 
	Returns:
		the int entered
	"""

	return int(input(prompt))


def read_float(prompt):
	""" 
	Reads a float from the user 
	Returns:
		the float entered
	"""
	return float(input(prompt))

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
		





def merch_inv_records(conn):
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWhat merchandise and inventory records would you like to change?\n" +
						"1. Enter, Update, or Delete information about products\n" +
						"2. Enter, Update, or Delete information about discounts\n" +
						"3. Increase, Remove, or search inventory for a specific product\n" + "\n"))
	return choice








def record_invoice(conn):
	""" 
	Record a new invoice
	Params:
		conn: Connection object
	"""

	# attempt to add to the invoice table
	invoice_id = read_int("Invoice ID: ")
	customer_id = read_int("Customer ID: ")
	bill_addr = read_string("Billing Address: ")
	bill_city = read_string("billing city: ")
	bill_state = read_string("billing state: ")
	bill_country = read_string("billing country: ")
	bill_postal_code = read_string("billing postal code: ")

	sql_insert_invoice = """ 
		INSERT INTO Invoice VALUES 
		(%s, %s, NOW(), %s, %s, %s, %s, %s, 0);
	"""

	try:
		conn.begin() # same as START TRANSACTION;
		cur = conn.cursor()

		lines_affected = cur.execute(sql_insert_invoice, 
			(invoice_id, customer_id, bill_addr, bill_city,
				bill_state, bill_country, bill_postal_code))

		if lines_affected != 1:
			raise Exception("insert into invoice did not affect one line")

		# attempt to add to the invoice line table
		invoice_line_id = read_int("Invoice Line Id: ")
		track_id = read_int("Track id: ")
		unit_price = read_float("Unit Price: ")
		quantity = read_int("Quantity: ")

		sql_insert_invoice_line = """INSERT INTO InvoiceLine VALUES
				(%s, %s, %s, %s, %s);
				"""

		lines_affected = cur.execute(sql_insert_invoice_line, 
			(invoice_line_id, invoice_id, track_id, 
				unit_price, quantity))

		if lines_affected != 1:
			raise Exception("insert into invoice line did not affect one row")

		total = unit_price * quantity

		sql_update_invoice = """UPDATE Invoice 
				SET total = %s
				WHERE InvoiceId = %s;"""

		lines_affected = cur.execute(sql_update_invoice, 
									(total, invoice_id))
		if lines_affected != 1:
			raise Exception("updating total didn't affect one line")

	except Exception as err:
		print("Cannot record invoice: ", err)
		conn.rollback() # same as ROLLBACK in SQL

	else: # this only triggers if the entire try block was successful
		conn.commit() # same as COMMIT in SQL

if __name__ == '__main__':
	main()