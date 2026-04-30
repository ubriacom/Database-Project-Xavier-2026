import pymysql.cursors

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
			pass


def reports_date_choice(conn):
	choice = -1
	while choice < 1 or choice > 3:
		choice = int(input("\nDo you need the sales by day, month, or year?\n" +
				   "1. Day\n" +
				   "2. Month\n" +
				   "3. Year\n" + "\n"))
		if choice == 1:
			pass
		elif choice == 2:
			pass
		elif choice == 3:
			pass


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