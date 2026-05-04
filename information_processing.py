import pymysql.cursors
from datetime import date


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


def information_processing(conn): # Gives the user a choice of which function they would like to do.
	choice =-1
	while choice < 1 or choice > 4:
		choice = int(input("\nWhat information processing would you like to perform?\n" +
							"1. Enter, Update, Delete, or Search information about stores\n" +
							"2. Enter, Update, Delete, or Search information about customers\n" +
							"3. Enter, Update, Delete, or Search information about members\n" +
							"4. Enter, Update, Delete, or Search information about staff\n" + "\n"))
	if choice == 1:
		store_info(conn)
	elif choice == 2:
		customer_info(conn)
	elif choice == 3:
		member_info(conn)
	elif choice == 4:
		staff_info(conn)
		

def store_info(conn): # Asks user which function they would like to do and then calls the function accordingly
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWould you like to enter, update or delete information?\n" +
					 "1. Enter\n" +
					 "2. Update\n" +
					 "3. Delete\n" +
					 "4. Search\n" + "\n"))
	if choice == 1:
		record_new_store(conn)
	elif choice == 2:
		update_store(conn)
	elif choice == 3:
		delete_store(conn)
	elif choice == 4:
		search_store(conn)


def customer_info(conn): # Asks user which function they would like to do and then calls the function accordingly
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWould you like to enter, update delete, or search information?\n" +
					 "1. Enter\n" +
					 "2. Update\n" +
					 "3. Delete\n" +
					 "4. Search\n" + "\n"))
	if choice == 1:
		enter_customer(conn)
	elif choice == 2:
		update_customer(conn)
	elif choice == 3:
		delete_customer(conn)
	elif choice == 4:
		search_customer(conn)
		

def member_info(conn): # Asks user which function they would like to do and then calls the function accordingly
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWould you like to enter, update delete, or search information?\n" +
					 "1. Enter\n" +
					 "2. Update\n" +
					 "3. Delete\n" +
					 "4. Search\n" + "\n"))
		if choice == 1:
			enter_member(conn)
		elif choice == 2:
			update_member(conn)
		elif choice == 3:
			delete_member(conn)
		elif choice == 4:
			search_member(conn)


		

def staff_info(conn): # Asks user which function they would like to do and then calls the function accordingly
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWould you like to enter, update or delete information?\n" +
					 "1. Enter\n" +
					 "2. Update\n" +
					 "3. Delete\n" +
					 "4. Search\n" + "\n"))
	if choice == 1:
		enter_staff(conn)
	elif choice == 2:
		update_staff(conn)
	elif choice == 3:
		delete_staff(conn)
	elif choice == 4:
		search_staff(conn)




def record_new_store(conn): # adds a new store
    managerID = read_int("Manager ID: ")
    address = read_string("Address: ")
    phone_number = read_string("Phone Number in (123)-456-7890 format: ")
		
    sql_insert_store = """ 
		INSERT INTO Store (ManagerID, Address, PhoneNumber) 
		VALUES (%s, %s, %s);
	"""
	
    try:
        conn.begin()
        cur = conn.cursor()

        lines_affected = cur.execute(sql_insert_store, 
			(managerID, address, phone_number))
		
        if lines_affected != 1:
            raise Exception("insert into store did not affect one line")
	
    except Exception as error:
        print("Invlaid Value: " + str(error))
		
    else:
        conn.commit()
		

def update_store(conn): # Updates an existing store.
    managerID = read_int("Manager ID: ")
    address = read_string("Address: ")
    phone_number = read_string("Phone Number in (123)-456-7890 format: ")
    storeID = read_int("Store ID: ")
	
    sql_update_store = """
        UPDATE STORE SET ManagerID = (%s), Address = (%s), PhoneNumber = (%s)
		WHERE StoreID = (%s);
    """
    conn.begin()
    cur = conn.cursor()
    cur.execute(sql_update_store, (managerID, address, phone_number, storeID))
    conn.commit()

def delete_store(conn): # Deletes an existing store
    storeID = read_int("Store ID: ")

    sql_delete_store = """ 
        DELETE FROM Store WHERE StoreID = (%s);
    """
    conn.begin()
    cur = conn.cursor()
    cur.execute(sql_delete_store, (storeID,))
    conn.commit()

def search_store(conn): # Searches existing stores.
    storeID = read_int("Store ID: ")
	
    sql_search_store = """
        SELECT * FROM Store WHERE StoreID = (%s);
    """
    conn.begin()
    cur = conn.cursor()
    cur.execute(sql_search_store, (storeID,))
    conn.commit()

    results = cur.fetchall()
    for row in results:
        print(row)


def enter_customer(conn): # Enters a new customer
	sql_enter_customer = """
	INSERT INTO Customer () VALUES (); 
	"""

	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_enter_customer)
	conn.commit()


def update_customer(conn): # Updates an existing customer
	old_customerID = read_int("\nWhat is the current customer ID: ")
	new_customerID = read_int("\nWhat is the new customer ID: ")

	sql_update_customer = """
	UPDATE Customer SET CustomerID = %s WHERE CustomerID = %s;
	"""

	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_update_customer, (new_customerID, old_customerID))
	conn.commit()

def delete_customer(conn): # Deletes an existing customer.
	customerID = read_int("\nWhat is the customer ID you want to delete: ")

	sql_delete_customer = """
	DELTE FROM Customer WHERE CustomerID = %s;
	"""

	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_delete_customer, (customerID,))
	conn.commit()

def search_customer(conn): # Searches customers based on their ID
	customerID = read_int("\nWhat is the customer ID to search for: ")
	sql_search_customer = """
	SELECT * FROM Customer WHERE CustomerID = %s
	"""

	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_search_customer, (customerID,))
	conn.commit()

def enter_member(conn): # Enters a new member
	customerID = read_int("\nCustomer ID: ")
	first_name = read_string("\nFirst Name: ")
	last_name = read_string("\nLast Name: ")
	email = read_string("\nEmail: ")
	phone_number = read_string("\nPhone Number: ")
	address = read_string("\nAddress: ")
	storeID = read_int("\nStore ID: ")
	staffID = read_int("\n Staff ID: ")
	sign_up_date = date.today().strftime("%Y-%m-%d")

	sql_enter_member = """
	INSERT INTO Member (CustomerID, FirstName, LastName, Email, PhoneNumber, Address)
	VALUES (%s, %s, %s, %s, %s, %s);
	"""
	sql_enter_sign_up = """
	INSERT INTO SignUp(CustomerID, StoreID, StaffID, SignUpDate) VALUES(%s, %s, %s, %s);
	"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_enter_member, (customerID, first_name, last_name, email, phone_number, address))
	cur.execute(sql_enter_sign_up, (customerID, storeID, staffID, sign_up_date))
	conn.commit()



def update_member(conn): # Updates information on existing members
	first_name = read_string("\nFirst Name: ")
	last_name = read_string("\nLast Name: ")
	email = read_string("\nEmail: ")
	phone_number = read_string("\nPhone Number: ")
	address = read_string("\nAddress: ")
	active_status = read_string("\nTRUE OR FALSE (ALL CAPS): ")
	customerID = read_int("\nCustomer ID: ")

	sql_update_member = """
	UPDATE Member
	SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, Address = %s, ActiveStatus = %s
	WHERE CustomerID = %s;
	"""

	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_update_member, (first_name, last_name, email, phone_number, address, active_status, customerID))
	conn.commit()

def delete_member(conn): # deletes a member
	customerID = read_int("\nCustomer ID: ")

	sql_delete_member = """
	DELETE FROM Member WHERE CustomerID = %s;
	"""

	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_delete_member, (customerID,))
	conn.commit()


def search_member(conn): # Searches for a member based on ID
	customerID = read_int("\nCustomer ID: ")

	sql_search_member = """
	SELECT * FROM Member WHERE CustomerID = %s;
	"""

	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_search_member, (customerID,))
	conn.commit()
	
	results = cur.fetchall()
	for row in results:
		print(row)




def enter_staff(conn): # Enters a new staff member
	first_name = read_string("\nWhat is the staff's first name? ")
	last_name = read_string("\nWhat is the staff's last name? ")
	age = read_int("\nHow old is the staff? ")
	address = read_string("\nWhat is the staff's address? ")
	job = read_string("\nWhat is the staff's job? ")
	phone_number = read_string("\nWhat is the staff's phone number? ")
	sql_enter_staff = """
    INSERT INTO Staff (%s, %s, %s, %s, %s, %s,) VALUES
"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_enter_staff, (first_name, last_name, age, address, job, phone_number))
	conn.commit()


def update_staff(conn): # Updates staff data
	first_name = read_string("\nWhat is the staff's first name? ")
	last_name = read_string("\nWhat is the staff's last name? ")
	age = read_int("\nHow old is the staff? ")
	address = read_string("\nWhat is the staff's address? ")
	job = read_string("\nWhat is the staff's job? ")
	phone_number = read_string("\nWhat is the staff's phone number? ")
	staff_ID = read_string("\nWhat is the staff's ID? ")

	sql_enter_staff = """
    UPDATE Staff SET FirstName = %s, LastName = %s, Age = %s, Address =%s, Job =%s, PhoneNumber = %s WHERE StaffID = %s;
	"""

	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_enter_staff, (first_name, last_name, age, address, job, phone_number, staff_ID))
	conn.commit()


def delete_staff(conn): # Deletes a staff member
	staffID = read_int("\n What is the staff's ID? ")

	sql_delete_staff = """
		DELETE FROM Staff WHERE StaffID = %s;
	"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_delete_staff, (staffID,))
	conn.commit()


def search_staff(conn): # searches staff based on ID
	sql_search_staff = """
		SELECT FirstName, LastName, Age, Address, Job, PhoneNumber, StaffID FROM Staff;
	"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_search_staff)
	conn.commit()
	results = cur.fetchall()
	for row in results:
		print(row)