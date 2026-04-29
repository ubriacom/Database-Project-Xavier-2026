import pymysql.cursors

def main():
	conn = create_connection('MuskieCo')    # establish DB connection
	if conn is None:
		exit()
		

	choice = get_user_choice()  # ask the user what operation they want to perform
	
	# call the method corresponding to that operation
	if choice == 1:
		record_invoice(conn) # TODO: replace this line with a new method call
	elif choice == 2:
		pass # TODO: replace this line with a new method call

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
	while choice < 1 or choice > 2:
		choice = int(input("What task would you like to perform:\n" +
								"1. Record a new invoice\n" +
								"2. TODO: replace this option\n"
								"3. Third option\n"
                                "4. Fourth option\n"))
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