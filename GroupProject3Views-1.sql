USE MuskieCo;

# If we're a manager, let us see any employee that works at a location we manage
CREATE VIEW ManagerEmployeeInfo AS
SELECT DISTINCT S.StaffID, S.FirstName, S.LastName, S.Age, S.Address, S.Job, S.PhoneNumber FROM Staff S
LEFT JOIN StaffWorksAt SwA ON S.StaffID = SwA.StaffID
LEFT JOIN Store St ON St.StoreID = SwA.StoreID
WHERE St.ManagerID = USER();

# If we're a normal staff, let us see our own information
CREATE VIEW EmployeeInfo AS
SELECT * FROM Staff S
WHERE S.StaffID = USER();

# If we're any employee, let us see all the product information in stores that we work at
CREATE VIEW StoreProductInfo AS
SELECT P.ProductID, P.StoreID, P.Name, P.BuyPrice, P.SellPrice FROM Staff S
LEFT JOIN StaffWorksAt SwA ON S.StaffID = SwA.StaffID
LEFT JOIN Store St ON St.StoreID = SwA.StoreID
LEFT JOIN Product P ON P.StoreID = St.StoreID
WHERE S.StaffID = USER();

# if this is a member, we'll see the info, if not, we wont see anything
CREATE VIEW CustomerSignUpInfo AS
SELECT C.CustomerID, S.StoreID, S.StaffID, S.SignUpDate FROM Customer C
INNER JOIN SignUp S ON C.CustomerID = S.CustomerID
WHERE C.CustomerID = USER();

# any customer should be able to view their transactions
CREATE VIEW CustomerTransactionInfo AS
SELECT C.CustomerID, T.TransactionID, T.StoreID, T.StaffID, P.Name, PP.Quantity FROM Customer C
LEFT JOIN Transaction T ON C.CustomerID = T.CustomerID
LEFT JOIN PurchasedProduct PP ON PP.TransactionID = T.TransactionID
LEFT JOIN Product P ON PP.ProductID = P.ProductID
WHERE C.CustomerID = USER();
