import pymysql.cursors


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
		

def store_info(conn):
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


def customer_info(conn):
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
		

def member_info(conn):
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


		

def staff_info(conn):
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




def record_new_store(conn):
    managerID = read_int("Manager ID: ")
    address = read_string("Address: ")
    phone_number = read_string("Phone Number in (123)-456-7890 format: ")
		
    sql_insert_store = """ 
		INSERT INTO Store VALUES 
		(%s, %s, %s);
	"""
	
    try:
        conn.begin() # same as START TRANSACTION;
        cur = conn.cursor()

        lines_affected = cur.execute(sql_insert_store, 
			(managerID, address, phone_number))
		
        if lines_affected != 1:
            raise Exception("insert into store did not affect one line")
	
    except Exception as error:
        print("Invlaid Value: " + str(error))
		
    else:
        conn.commit()
		



def update_store(conn):
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
    cur.execute(sql_update_store(managerID, address, phone_number, storeID))
    conn.commit()

def delete_store(conn):
    storeID = read_int("Store ID: ")

    sql_delete_store = """ 
        DELETE FROM Store WHERE StoreID = (%s);
    """
    conn.begin()
    cur = conn.cursor()
    cur.execute(sql_delete_store, (storeID,))
    conn.commit()

def search_store(conn):
    storeID = read_int("Store ID: ")
	
    sql_search_store = """
        SELECT * FROM Store WHERE StoreID = (%s);
    """
    conn.begin()
    cur = conn.cursor()
    cur.execute(sql_search_store, (storeID))
    conn.commit()


def enter_customer(conn):
	pass


def update_customer(conn):
	pass


def delete_customer(conn):
	pass


def search_customer(conn):
	pass


def enter_member(conn):
	pass


def update_member(conn):
	pass


def delete_member(conn):
	pass


def search_member(conn):
	pass




def enter_staff(conn):
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
	cur.execute(sql_enter_staff (first_name, last_name, age, address, job, phone_number))
	conn.commit()


def update_staff(conn):
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
	cur.execute(sql_enter_staff (first_name, last_name, age, address, job, phone_number, staff_ID))
	conn.commit()


def delete_staff(conn):
	staffID = read_int("\n What is the staff's ID? ")

	sql_delete_staff = """
		DELETE FROM Staff WHERE StaffID = %s;
	"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_delete_staff(staffID))
	conn.commit()


def search_staff(conn):
	sql_search_staff = """
		SELECT FirstName, LastName, Age, Address, Job, PhoneNumber, StaffID FROM Staff;
	"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_search_staff)
	conn.commit()