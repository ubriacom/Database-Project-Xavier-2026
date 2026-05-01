import pymysql.cursors

def bill_trans_records(conn):
	choice = -1
	while choice < 1 or choice > 3:
	  # ask for the value
		choice = int(input("\nWhat records do you need from transactions and billing?\n" +
					 "1. Generate reward notices for members that are due at the end of each month\n" +
					 "2. Generate rewards checks for employees at the end of each quarter\n" +
					 "3. Transaction information including total price\n" + "\n"))
					 
	  # direct to correct function, or ask the person to retry
	  
		if choice == 1:
			member_reward_notice(conn)
		elif choice ==2:
			employee_reward_check(conn)
		elif choice == 3:
			transaction_information(conn)
		else:
		  print(f"{choice} is not a valid value, please input '1', '2', or '3' (without quotes)")
		


def member_reward_notice(conn):
  pass
def employee_reward_check(conn):
  pass

def transaction_information(conn):
    # get the transaction id
  	transaction_id = read_int("Transaction ID: ")
  	
  	# create our large SQL statement (boo! im a big block of code!)
  	sql_statement = f"""
		SELECT DISTINCT p.Name, MAX(p.SellPrice) AS Individual_Price, MAX(pp.Quantity) AS Total_Quantity, MAX(p.SellPrice * pp.Quantity) AS Raw_Amount_Spent,
    SUM(d.Amount) AS Discount, MAX(p.SellPrice * pp.Quantity) * (100-SUM(d.Amount))/100 AS Amount_Spent
    FROM Transaction t -- Using joins to chain transaction purchased prodcuct and product together.
    INNER JOIN PurchasedProduct pp ON t.TransactionID = pp.TransactionID
    INNER JOIN Product p ON pp.ProductID = p.ProductID -- the chain is over :D 
    INNER JOIN DiscountAppliesToProduct DAP ON DAP.ProductID = p.ProductID
    INNER JOIN Discount d ON DAP.DiscountID = d.DiscountID
    WHERE t.TransactionID = %s AND d.DiscountID IN (
  	SELECT DiscountID FROM Discount
  	WHERE Discount.StartDate < CURDATE() AND CURDATE() < Discount.EndDate ) 
    GROUP BY p.ProductID;
  	"""
  	
  	try:
  	  # start our transaction
  		conn.begin() 
  		cur = conn.cursor(dictionary=True) # makes it nicer to read
  
      cur.execute(sql_statement, (transaction_id))
      results = cur.fetchall() # get our results
      print(f"Information for Transaction ID: {transaction_id}")
      
      if (len(results) == 0):
        # no data! let the user known
        raise Exception(f"No data found for Transaction ID: {transaction_id}")
      
      # display results and calculate total manually
      total_spent = 0
      for row in results:
        print(row)
        total_spent += row["Amount_Spent"] or row["Raw_Amount_Spent"] or 0
        
      print(f"Total money spent in transaction: {total_spent}")
      
  	except Exception as err:
  		print("Error: ", err)
  		conn.rollback() # same as ROLLBACK in SQL
  
  	else: # this only triggers if the entire try block was successful
  		conn.commit() # same as COMMIT in SQL
  
