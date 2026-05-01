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
		choice = int(input("\nWould you like to enter, update or delete information?\n" +
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
    cur.execute(sql_search_store, (storeID,))
    conn.commit()


def enter_customer(conn):
	pass


def update_customer(conn):
	pass


def delete_customer(conn):
	pass


def search_customer(conn):
	pass




def enter_staff(conn):
	pass


def update_staff(conn):
	pass


def delete_staff(conn):
	pass


def search_staff(conn):
	pass