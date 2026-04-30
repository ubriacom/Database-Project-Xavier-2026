import pymysql.cursors

def merch_inv_records(conn):
	choice = -1
	while choice < 1 or choice > 4:
		choice = int(input("\nWhat merchandise and inventory records would you like to change?\n" +
						"1. Enter, Update, or Delete information about products\n" +
						"2. Enter, Update, or Delete information about discounts\n" +
						"3. Increase, Remove, or search inventory for a specific product\n" + "\n"))
	return choice