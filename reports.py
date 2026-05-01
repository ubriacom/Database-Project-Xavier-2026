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



def reports(conn):
    choice = -1
    while choice < 1 or choice > 3:
        choice = int(input("\nWhat reports are needed?\n" +
                           "1. Total sales by day, month, or year\n" +
                           "2. Merchandise stock reporting\n" +
                           "3. Customer total purchase amount for a given time period\n" + "\n"))
        if choice == 1:
            reports_date_choice(conn)
        elif choice == 2:
            stock_reporting(conn)
        elif choice == 3:
            start_date = read_string("\nStart Date: ")
            end_date = read_string("\nEnd Date: ")
            customerID = read_int("Customer ID: ")

            sql_customer_purchase_records = """
                SELECT SUM(P.SellPrice) AS Amount_Spent, t.CustomerID
                FROM Transaction t
                INNER JOIN PurchasedProduct pp ON t.TransactionID = pp.TransactionID
                INNER JOIN Product p ON pp.ProductID = p.ProductID
                WHERE (t.PurchaseDate BETWEEN (%s) AND (%s)) AND t.CustomerID = (%s);
            """
            conn.begin()
            cur = conn.cursor()
            cur.execute(sql_customer_purchase_records, (start_date, end_date, customerID))
            conn.commit()


def reports_date_choice(conn):
	choice = -1
	while choice < 1 or choice > 3:
		choice = int(input("\nDo you need the sales by day, month, or year?\n" +
						   "1. Day\n" +
						   "2. Month\n" +
						   "3. Year\n\n"))

		if choice == 1:
			storeID = read_int("Store ID: ")
			date = read_string("Day (YYYY-MM-DD): ")
			sql = """
				SELECT COUNT(*) AS Sales
				FROM Transaction
				WHERE StoreID = %s
				AND DATE(PurchaseDate) = %s;
			"""
			
			cur = conn.cursor()
			cur.execute(sql, (storeID, date))
			result = cur.fetchone()
			cur.close()
			print(f"\nSales for Store {storeID} on {date}: {result[0]}")

		elif choice == 2:
			storeID = read_int("Store ID: ")
			month = read_int("Month (1-12): ")
			year = read_int("Year (YYYY): ")
			sql = """
				SELECT COUNT(*) AS Sales
				FROM Transaction
				WHERE StoreID = %s
				AND MONTH(PurchaseDate) = %s
				AND YEAR(PurchaseDate) = %s;
			"""
			cur = conn.cursor()
			cur.execute(sql, (storeID, month, year))
			result = cur.fetchone()
			cur.close()
			print(f"\nSales for Store {storeID} in {month}/{year}: {result[0]}")

		elif choice == 3:
			storeID = read_int("Store ID: ")
			year = read_int("Year (YYYY): ")
			sql = """
				SELECT COUNT(*) AS Sales
				FROM Transaction
				WHERE StoreID = %s
				AND YEAR(PurchaseDate) = %s;
			"""
			cur = conn.cursor()
			cur.execute(sql, (storeID, year))
			result = cur.fetchone()
			cur.close()
			print(f"\nSales for Store {storeID} in {year}: {result[0]}")

		else:
			print("Invalid choice, please enter 1, 2, or 3.")


def stock_reporting(conn):
	choice = -1
	while choice < 1 or choice > 2:
		choice = int(input("\nDo you want to check a product across one store or all stores\n" +
					 "1. One store\n" +
					 "2. All stores\n" + "\n"))
		if choice == 1:
			pass
		elif choice == 2:
			pass
		

def customer_records(conn):
	pass