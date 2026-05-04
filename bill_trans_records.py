import pymysql.cursors

# UTILITY FUNCTIONS
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



# MAIN SELECTOR FUNCTION
def bill_trans_records(conn):
	choice = -1
	while choice < 1 or choice > 4:
	  # ask for the value
		choice = int(input("\nWhat records do you need from transactions and billing?\n" +
					 "1. Generate reward notices for members that are due at the end of each month\n" +
					 "2. Generate rewards checks for employees at the end of each quarter\n" +
					 "3. Transaction information including total price\n" + "4. [Cancel]" + "\n"))
					 
	  # direct to correct function, or ask the person to retry
	  
		if choice == 1:
			member_reward_notice(conn)
		elif choice ==2:
			employee_reward_check(conn)
		elif choice == 3:
			transaction_information(conn)
		else:
		  print(f"{choice} is not a valid value, please input '1', '2', or '3' (without quotes)")
		  print("'4' to close")


# ----- CALCULATE A MEMBERS REWARD -----
# EXAMPLE: CustomerId = 3, Year = 2026, Month = 3
# Should Return: an actual value
def member_reward_notice(conn):
  # we should use USER(), however this lets us test without having to have multiple users
  customer_id = -1 
  transaction_year = -1
  transaction_month = -1
  
  # make sure its a valid id
  while customer_id < 0:
    customer_id = read_int("Input Customer ID: ")
    if customer_id < 0:
      print("Customer IDs cannot be negative, please try again")
    
  # make sure it's a valid year
  # for this dataset, the earliest it will go is 2000, and the latest it will go is 2026
  while transaction_year < 2000 or transaction_year > 2026:
    transaction_year = read_int("Input Year (4 digits): ")
    if transaction_year < 2000 or transaction_year > 2026:
      print("Please input a valid year (years 2000-2026)")
  
      
  # make sure it's a valid month
  while transaction_month < 1 or transaction_month > 12:
    transaction_month = read_int("Input Month (input number from 1-12: ")
    if transaction_month < 1 or transaction_month > 12:
      print("Please input a value between 1 and 12, according to the month.")
      
  # do the same thing we did in Transaction Information, except we'll just grab
  # the total money spent :
  sql_statement = """
  	SELECT DISTINCT p.Name, MAX(p.SellPrice) AS Individual_Price, MAX(pp.Quantity) AS Total_Quantity, MAX(p.SellPrice * pp.Quantity) AS Raw_Amount_Spent,
  	SUM(d.Amount) AS Discount, MAX(p.SellPrice * pp.Quantity) * (100-SUM(d.Amount))/100 AS Amount_Spent
  	FROM Transaction t 
  	INNER JOIN PurchasedProduct pp ON t.TransactionID = pp.TransactionID
  	INNER JOIN Product p ON pp.ProductID = p.ProductID
  	INNER JOIN DiscountAppliesToProduct DAP ON DAP.ProductID = p.ProductID
  	INNER JOIN Discount d ON DAP.DiscountID = d.DiscountID
  	WHERE (YEAR(t.PurchaseDate) = %s AND MONTH(t.PurchaseDate) = %s) AND t.CustomerID = %s  AND d.DiscountID IN (
  	SELECT DiscountID FROM Discount
  	WHERE Discount.StartDate < CURDATE() AND CURDATE() < Discount.EndDate ) 
  	GROUP BY p.ProductID;
  """
  try:
  	  # start our transaction
  	  conn.begin() 
  	  cur = conn.cursor(dictionary=True) # makes it nicer to read
  	  
  	  cur.execute(sql_statement, (transaction_year,transaction_month,customer_id))
  	  
  	  results = cur.fetchall() # get our results

      if (len(results) == 0):
        # no data! let the user known
        raise Exception(f"No data found for customer on given date!")
      
      # calculate total
      total_spent = 0
      for row in results:
        total_spent += row["Amount_Spent"] or row["Raw_Amount_Spent"] or 0
        
      # round and calculate rewards
      total_spent = round(total_spent,2)
      total_rewards = total_spent * 0.02 # 2% in rewards :D
      
      print(f"Total Customer Rewards for Customer Id {customer_id} on year {transaction_year} and month {transaction_month}: { total_rewards }")
      
    except Exception as err:
      print("Error: ", err)
      conn.rollback() # same as ROLLBACK in SQL
  
  	else: # this only triggers if the entire try block was successful
  		conn.commit() # same as COMMIT in SQL
  
  
  
# ----- CALCULATE AN EMPLOYEES REWARD -----
# EXAMPLE: EmployeeId = 1, Year = 2018, Quarter = 3
# Should Return: 50 (2 sign ups -> 50 dollar bonus)
def employee_reward_check(conn):
  employee_id = -1 
  transaction_year = -1
  transaction_quarter = -1
  
  # make sure its a valid id
  while employee_id < 0:
    employee_id = read_int("Input Employee ID: ")
    if employee_id < 0:
      print("Employee IDs cannot be negative, please try again")
    
  # make sure it's a valid year
  # for this dataset, the earliest it will go is 2000, and the latest it will go is 2026
  while transaction_year < 2000 or transaction_year > 2026:
    transaction_year = read_int("Input Year (4 digits): ")
    if transaction_year < 2000 or transaction_year > 2026:
      print("Please input a valid year (years 2000-2026)")
      
  # make sure it's a valid quarter
  while transaction_quarter < 1 or transaction_quarter > 12:
    transaction_quarter = read_int("Quarter 1: Spring\nQuarter 2: Summer\nQuarter 3: Fall\nQuarter 4: Winter\nInput Quarter (input number from 1-4): ")
    if transaction_quarter < 1 or transaction_quarter > 12:
      print("Please input a value between 1 and 4, according to the quarter.")
      
  # to make it easier, let's just convert our "quarter" to 3 month values
  qMonth1 = 0
  qMonth2 = 0
  qMonth3 = 0
  
  if transaction_quarter = 1: # spring months
    qMonth1 = 3
    qMonth2 = 4
    qMonth3 = 5
  elif transaction_quarter = 2: # summer months
    qMonth1 = 6
    qMonth2 = 7
    qMonth3 = 8
  elif transaction_quarter = 3: # fall months
    qMonth1 = 9
    qMonth2 = 10
    qMonth3 = 11
  else # fall months
    qMonth1 = 12
    qMonth2 = 1
    qMonth3 = 2
    
  # a small query?! impossible
  sql_statement = """
      SELECT COUNT(StaffID) AS SignUps, COUNT(StaffID)*25 AS Bonus
      FROM Signup s
      WHERE s.StaffID = %s AND YEAR(s.SignUpDate) = %s AND
      (MONTH(s.SignUpDate) IN (%s,%s,%s));
     """
     
  try:
  	  # start our transaction
  	  conn.begin() 
  	  cur = conn.cursor(dictionary=True) # makes it nicer to read
  	  
  	  cur.execute(sql_statement, (employee_id,transaction_year,qMonth1,qMonth2,qMonth3))
  	  
  	  results = cur.fetchall() # get our results

      if (len(results) == 0):
        # no data! let the user known
        raise Exception(f"No data found for employee on given date!")
      
      # calculate total (reusing the code from others to make it simpler)
      total_bonus = 0
      total_signups = 0
      for row in results:
        total_bonus += row["Bonus"] or 0
        total_signups += row["SignUps"] or 0
        
      # print the bonus!
      print(f"Employee signed up {total_signups} in quarter {transaction_quarter}, {transaction_year} and earned ${total_bonus} !")
      
    except Exception as err:
      print("Error: ", err)
      conn.rollback() # same as ROLLBACK in SQL
  
  	else: # this only triggers if the entire try block was successful
  		conn.commit() # same as COMMIT in SQL
     


# ----- GET ALL INFORMATION FOR A TRANSACTION -----
# EXAMPLE: TransactionID = 1
# Should Return: a purchase of 5 items
def transaction_information(conn):
    # get the transaction id
    transaction_id = -1 
    
  	# make sure the transaction id is valid
  	while transaction_id < 0:
  	  transaction_id = read_int("Transaction ID: ")
  	  if transaction_id < 0:
  	    print("Transaction ID must be positive!")
  	
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
        
      print(f"Total money spent in transaction: { round(total_spent,2) }")
      
    except Exception as err:
      print("Error: ", err)
      conn.rollback() # same as ROLLBACK in SQL
  
  	else: # this only triggers if the entire try block was successful
  		conn.commit() # same as COMMIT in SQL
  
