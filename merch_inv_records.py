import pymysql.cursors
#useful read functions :)
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

#the main stuff
def merch_inv_records(conn):
	choice = -1
	while choice < 1 or choice > 3: #main menu of this section
		choice = int(input("\nWhat merchandise and inventory records would you like to change?\n" +
						"1. Enter, Update, or Delete information about products\n" +
						"2. Enter, Update, or Delete information about discounts\n" +
						"3. Increase, Remove, or search inventory for a specific product\n" + "\n"))
	return choice


def product_info(conn):
	choice = -1
	while choice < 1 or choice > 4: #product menu
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
	while choice < 1 or choice > 4: #discount menu
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
	#takes values to put into querry
	store_id = read_int("\nStore ID: ")
	name = read_string("\nName: ")
	buy_price = read_float("\nBuy Price: ")
	sell_price = read_float("\nSell Price: ")

#querry
	sql_enter_product = """
        INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES ((%s), (%s), (%s), (%s));
		"""
	#executing querry
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_enter_product, (store_id, name, buy_price, sell_price))
	conn.commit()
#simmilar concept to the previous function for all the other functions
def update_product(conn):
	name = read_string("\nEnter the name of the product you want to update: ") #specify just so the user does not think they are updating an ID
	sell_price = read_float("\nSell Price: ")
	sql_update_product = """
        UPDATE Product SET Price = (%s) WHERE Name = (%s);
		"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_update_product, (sell_price, name))
	conn.commit()

def delete_product(conn):
	product_id = read_int("\nProduct ID: ")
	sql_delete_product = """
        DELETE FROM Product WHERE ProductID = (%s);
		"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_delete_product, (product_id))
	conn.commit()

def search_product(conn):
	product_id = read_int("\nProductID: ")
	sql_search_product = """
        SELECT Name, BuyPrice, SellPrice FROM Product WHERE ProductID = (%s);
		"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_search_product, (product_id))
	conn.commit()



def enter_discount(conn):
	amount = read_float("\nName: ")
	start_date = read_string("\nStart Date: ")
	end_date = read_string("\nEnd Date: ")

	sql_enter_discount = """
        INSERT INTO Discount (Amount, StartDate, EndDate) VALUES ((%s), '2026-8-31', '2026-10-15');
		"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_enter_discount, (amount, start_date, end_date))
	conn.commit()

def update_discount(conn):
	discount_id = read_string("\nEnter the ID of the discount you want to update: ")
	amount = read_float("\nName: ")
	start_date = read_string("\nStart Date: ")
	end_date = read_string("\nEnd Date: ")

	sql_update_discount = """
        UPDATE Discount SET Amount = (%s), StartDate = (%s), EndDate = (%s) WHERE DiscountID = (%s);
		"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_update_discount, (amount, start_date, end_date, discount_id))
	conn.commit()

def delete_discount(conn):
	discount_id = read_int("\nDiscount ID: ")
	sql_delete_discount = """
        DELETE FROM Discount WHERE DiscountID = (%s);
		"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_delete_discount, (discount_id))
	conn.commit()

def search_discount(conn):
	discount_id = read_int("\nDiscount ID: ")
	sql_search_discount = """
        SELECT * FROM Discount WHERE DiscountID = (%s);;
		"""
	conn.begin()
	cur = conn.cursor()
	cur.execute(sql_search_discount, (discount_id))
	conn.commit()