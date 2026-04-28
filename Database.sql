DROP DATABASE MuskieCo;
CREATE DATABASE MuskieCo;
USE MuskieCo;

-- ----- ------- [ DATASET CREATION (TASK 1) ] ------- ----- --

-- ----- [ OBJECTS ] ----- --

-- STAFF TABLE
CREATE TABLE Staff(
	StaffID INT UNSIGNED AUTO_INCREMENT,
    FirstName VARCHAR(40) NOT NULL,
    LastName VARCHAR(40) NOT NULL,
    Age INT UNSIGNED NOT NULL,
    Address VARCHAR(40) NOT NULL,
    Job VARCHAR(40),
    PhoneNumber VARCHAR(18),
    
    PRIMARY KEY(StaffID)
);
-- STORE TABLE
CREATE TABLE Store(
	StoreID INT UNSIGNED AUTO_INCREMENT,
    ManagerID INT UNSIGNED,
    Address VARCHAR(40) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(18) DEFAULT "+1(513)-284-1952", -- this'll be our general number to some sort of call center, becuase i think thats how it works 
    
    PRIMARY KEY(StoreID),
    FOREIGN KEY (ManagerID) REFERENCES Staff (StaffID) ON DELETE SET NULL ON UPDATE CASCADE
);
-- CUSTOMER TABLE
CREATE TABLE Customer(
	CustomerID INT UNSIGNED AUTO_INCREMENT,
    PRIMARY KEY(CustomerID)
);
-- MEMBER (CUSTOMER) TABLE
CREATE TABLE Member(
	CustomerID INT UNSIGNED,
    FirstName VARCHAR(40) NOT NULL,
    LastName VARCHAR(40) NOT NULL,
    Email VARCHAR(60) UNIQUE,
	PhoneNumber VARCHAR(18),
	Address VARCHAR(40) NOT NULL,
	ActiveStatus BOOLEAN DEFAULT TRUE,
    RewardsPoints INT UNSIGNED DEFAULT 0, -- (NEW VALUE) because we didnt incorperate it beforehand
	
    PRIMARY KEY(CustomerID),
    FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID) ON DELETE CASCADE ON UPDATE CASCADE,
	CHECK ( (Email IS NOT NULL) OR (PhoneNumber IS NOT NULL) ) -- give either a phone number or email, or both :), not neither
);
-- SIGN UPS TABLE
CREATE TABLE SignUp(
	CustomerID INT UNSIGNED,
    StoreID INT UNSIGNED,
    StaffID INT UNSIGNED,
    SignUpDate DATE NOT NULL,
    
    PRIMARY KEY(CustomerID),
    FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID)  ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (StoreID) REFERENCES Store (StoreID)  ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)  ON DELETE SET NULL ON UPDATE CASCADE
);
-- PRODUCT TABLE
CREATE TABLE Product(
	ProductID INT UNSIGNED AUTO_INCREMENT,
	StoreID INT UNSIGNED,
    Name VARCHAR(80) NOT NULL,
	BuyPrice DOUBLE NOT NULL,
    SellPrice DOUBLE NOT NULL,
    
    PRIMARY KEY(ProductID),
	FOREIGN KEY (StoreID) REFERENCES Store (StoreID)  ON DELETE SET NULL ON UPDATE CASCADE

);
-- DISCOUNT TABLE
CREATE TABLE Discount(
	DiscountID INT UNSIGNED AUTO_INCREMENT,
    Amount DOUBLE NOT NULL, -- we'll measure this in %, (100 = free, 0 = no discount)
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    
    PRIMARY KEY(DiscountID),
    CHECK (EndDate > StartDate)
);
-- TRANSACTION TABLE
CREATE TABLE Transaction(
	TransactionID INT UNSIGNED AUTO_INCREMENT,
	StoreID INT UNSIGNED,
    CustomerID INT UNSIGNED,
    StaffID INT UNSIGNED,
    PurchaseDate DATE NOT NULL,
    
    PRIMARY KEY (TransactionID),
	FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID)  ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (StoreID) REFERENCES Store (StoreID)  ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (StaffID) REFERENCES Staff (StaffID)  ON DELETE SET NULL ON UPDATE CASCADE
);
-- (NEW) PURCHASED PRODUCT: A way to handle the quantity of products bought
CREATE TABLE PurchasedProduct(
	PurchasedProductID INT UNSIGNED AUTO_INCREMENT,
	ProductID INT UNSIGNED,
    TransactionID INT UNSIGNED,
    Quantity DOUBLE NOT NULL, -- incase, somehow, portions of a product are bought

    PRIMARY KEY(PurchasedProductID, ProductID),
   	FOREIGN KEY (ProductID) REFERENCES Product (ProductID),
   	FOREIGN KEY (TransactionID) REFERENCES Transaction (TransactionID)
);


-- ----- [ MANY-TO-MANY RELATIONSHIPS ] ----- --

-- Staff to StoreID
CREATE TABLE StaffWorksAt(
	StaffID INT UNSIGNED,
    StoreID INT UNSIGNED,
    
    PRIMARY KEY (StaffID, StoreID),
	FOREIGN KEY (StaffID) REFERENCES Staff (StaffID),
	FOREIGN KEY (StoreID) REFERENCES Store (StoreID)
);
-- Discounts to Products
CREATE TABLE DiscountAppliesToProduct(
	DiscountID INT UNSIGNED,
    ProductID INT UNSIGNED,
    
    PRIMARY KEY (DiscountID, ProductID),
	FOREIGN KEY (DiscountID) REFERENCES Discount (DiscountID),
	FOREIGN KEY (ProductID) REFERENCES Product (ProductID)
);


-- ----- ------- [ DATASET POPULATION (TASK 2) ] ------- ----- --

-- STAFF
INSERT INTO Staff (FirstName, LastName, Age, Address, Job, PhoneNumber) VALUES ( "John", "Doe", 23, "123 Location Lane", "Cashier", "+1(202)-321-9876");
INSERT INTO Staff (FirstName, LastName, Age, Address, Job, PhoneNumber) VALUES ( "Brent", "Peterson", 42, "204 Location Lane", "General Manager", "+1(869)-555-5556");
INSERT INTO Staff (FirstName, LastName, Age, Address, Job, PhoneNumber) VALUES ( "Jonah", "Wilke-Shapiro", 19, "860 Somwhere Iowa", "Cashier", "+1(515)-770-9255");
INSERT INTO Staff (FirstName, LastName, Age, Address, Job, PhoneNumber) VALUES ( "Swagg", "Mc'Cool", 26, "9721 That Place", "General Staff", "+1(090)-892-1924");
INSERT INTO Staff (FirstName, LastName, Age, Address, Job, PhoneNumber) VALUES ( "Connor", "O'Connor", 52, "582 Over There", "General Manager", "+1(987)-654-3210");

-- STORES
INSERT INTO Store (ManagerID, Address) VALUES (3,"5900 Norwood Dr.");
INSERT INTO Store (ManagerID, Address, PhoneNumber) VALUES (3,"4510 Cincinatto Rd.","+1(513)-712-8135");
INSERT INTO Store (ManagerID, Address, PhoneNumber) VALUES (5,"001 Sesame Street","+1(808)-690-4196");
INSERT INTO Store (ManagerID, Address) VALUES (5,"6800 Centerville Rd.");
INSERT INTO Store (ManagerID, Address) VALUES (5,"2830 Washongton Lane");

-- CUSTOMERS
-- we dont store any info for general customers, only members, so lets just populate a bunch of ids
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 
INSERT INTO Customer () VALUES (); 

-- MEMBERS 
-- these are the customers we do have data on!
INSERT INTO Member (CustomerID, FirstName, LastName, Email, PhoneNumber, Address, ActiveStatus)
VALUES (3, "Jared", "Fletcher", "jfletcher123@gmail.com","+1(407)-717-8162","408 Lake Cove Point Cir.",TRUE);
INSERT INTO Member (CustomerID, FirstName, LastName, Email, PhoneNumber, Address, ActiveStatus)
VALUES (4, "Jane", "Fletcher", "jfletcher124@gmail.com","+1(407)-827-6124","408 Lake Cove Point Cir.",TRUE);
INSERT INTO Member (CustomerID, FirstName, LastName, Email, Address)
VALUES (6, "Chuck", "Bills", "c.money.alltheway@gmail.com","280 Orion Ct.");
INSERT INTO Member (CustomerID, FirstName, LastName, PhoneNumber, Address)
VALUES (8, "Wade", "Vecchi", "+1(817)-612-9185","780 Orion Ct.");
INSERT INTO Member (CustomerID, FirstName, LastName, Email, PhoneNumber, Address)
VALUES (11, "Todd", "Carlo","crazytodd@xavier.edu", "+1(511)-661-9130","0510 Holy Rd.");

-- MEMBER SIGN-UPS

INSERT INTO SignUp (CustomerID, StoreID, StaffID, SignUpDate) VALUES (3, 2, 1, '2018-08-21');    
INSERT INTO SignUp (CustomerID, StoreID, StaffID, SignUpDate) VALUES (4, 2, 1, '2018-08-21');    
INSERT INTO SignUp (CustomerID, StoreID, StaffID, SignUpDate) VALUES (6, 4, 5, '2019-02-03');    
INSERT INTO SignUp (CustomerID, StoreID, StaffID, SignUpDate) VALUES (8, 3, 3, '2020-11-18');    
INSERT INTO SignUp (CustomerID, StoreID, StaffID, SignUpDate) VALUES (11, 5, 3, '2020-06-28');    

-- PRODUCTS
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (1,'Xavier "X" T-Shirt', 5.00, 8.99);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (2,'Xavier "X" T-Shirt', 5.00, 8.99);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (3,'Xavier "X" T-Shirt', 5.00, 8.99);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (4,'Xavier "X" T-Shirt', 5.00, 8.99);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (5,'Xavier "X" T-Shirt', 5.00, 8.99);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (1, 'Xavier "X" hat', 2.00, 9.99);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (2, 'Xavier "X" hat', 2.00, 9.99);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (3, 'Xavier "X" hat', 2.00, 9.99);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (4, 'Xavier "X" hat', 2.00, 9.99);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (5, 'Xavier "X" hat', 2.00, 9.99);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (1, 'Xavier Basketball', 6.00, 15.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (2, 'Xavier Basketball', 6.00, 15.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (3, 'Xavier Basketball', 6.00, 15.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (4, 'Xavier Basketball', 6.00, 15.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (5, 'Xavier Basketball', 6.00, 15.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (1, 'Xavier Keychain', 0.50, 5.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (2, 'Xavier Keychain', 0.50, 5.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (3, 'Xavier Keychain', 0.50, 5.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (4, 'Xavier Keychain', 0.50, 5.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (5, 'Xavier Keychain', 0.50, 5.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (1,'Xavier Sweatshirt', 12.00, 80.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (2,'Xavier Sweatshirt', 12.00, 80.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (3,'Xavier Sweatshirt', 12.00, 80.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (4,'Xavier Sweatshirt', 12.00, 80.00);
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (5,'Xavier Sweatshirt', 12.00, 80.00);

-- DISCOUNTS
INSERT INTO Discount (Amount, StartDate, EndDate) VALUES (10, '2026-10-31', '2026-11-14');
INSERT INTO Discount (Amount, StartDate, EndDate) VALUES (15, '2026-05-03', '2026-05-06');
INSERT INTO Discount (Amount, StartDate, EndDate) VALUES (15, '2026-09-04', '2026-09-07');
INSERT INTO Discount (Amount, StartDate, EndDate) VALUES (5, '2026-03-01', '2026-05-31');
INSERT INTO Discount (Amount, StartDate, EndDate) VALUES (10, '2026-12-06', '2026-12-19');

-- TRANSACTIONS
INSERT INTO Transaction (StoreId, CustomerID, StaffID, PurchaseDate) VALUES (1, 1, 3, '2026-03-14');
INSERT INTO Transaction (StoreId, CustomerID, StaffID, PurchaseDate) VALUES (1, 2, 2, '2026-02-28');
INSERT INTO Transaction (StoreId, CustomerID, StaffID, PurchaseDate) VALUES (2, 3, 1, '2026-03-14');
INSERT INTO Transaction (StoreId, CustomerID, StaffID, PurchaseDate) VALUES (2, 4, 1, '2026-02-14');
INSERT INTO Transaction (StoreId, CustomerID, StaffID, PurchaseDate) VALUES (3, 5, 4, '2026-03-05');
INSERT INTO Transaction (StoreId, CustomerID, StaffID, PurchaseDate) VALUES (3, 6, 2, '2026-03-05');
INSERT INTO Transaction (StoreId, CustomerID, StaffID, PurchaseDate) VALUES (4, 7, 5, '2026-03-05');
INSERT INTO Transaction (StoreId, CustomerID, StaffID, PurchaseDate) VALUES (4, 8, 1, '2026-01-24');
INSERT INTO Transaction (StoreId, CustomerID, StaffID, PurchaseDate) VALUES (5, 9, 3, '2026-01-24');
INSERT INTO Transaction (StoreId, CustomerID, StaffID, PurchaseDate) VALUES (5, 10, 2, '2026-03-13');

-- PURCHASED PRODUCT
INSERT INTO PurchasedProduct (ProductID, TransactionID, Quantity) VALUES (1, 2, 1.00);
INSERT INTO PurchasedProduct (ProductID, TransactionID, Quantity) VALUES (2, 4, 2.00);
INSERT INTO PurchasedProduct (ProductID, TransactionID, Quantity) VALUES (3, 3, 3.00);
INSERT INTO PurchasedProduct (ProductID, TransactionID, Quantity) VALUES (4, 1, 5.00);
INSERT INTO PurchasedProduct (ProductID, TransactionID, Quantity) VALUES (5, 5, 2.00);

-- STAFF WORKS AT
INSERT INTO StaffWorksAt (StaffID, StoreID) VALUES (1, 1);
INSERT INTO StaffWorksAt (StaffID, StoreID) VALUES (2, 2);
INSERT INTO StaffWorksAt (StaffID, StoreID) VALUES (3, 3);
INSERT INTO StaffWorksAt (StaffID, StoreID) VALUES (3, 1);
INSERT INTO StaffWorksAt (StaffID, StoreID) VALUES (3, 2);
INSERT INTO StaffWorksAt (StaffID, StoreID) VALUES (4, 4);
INSERT INTO StaffWorksAt (StaffID, StoreID) VALUES (5, 5);
INSERT INTO StaffWorksAt (StaffID, StoreID) VALUES (5, 4);
INSERT INTO StaffWorksAt (StaffID, StoreID) VALUES (1, 2);
INSERT INTO StaffWorksAt (StaffID, StoreID) VALUES (3, 5);

-- DISCOUNT APPLIES TO PRODUCT
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (1, 1);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (1, 2);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (1, 3);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (1, 4);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (1, 5);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (2, 1);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (2, 2);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (2, 3);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (2, 4);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (2, 5);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (3, 1);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (3, 2);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (3, 3);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (3, 4);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (3, 5);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (4, 1);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (4, 2);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (4, 3);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (4, 4);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (4, 5);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (5, 1);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (5, 2);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (5, 3);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (5, 4);
INSERT INTO DiscountAppliesToProduct (DiscountID, ProductID) VALUES (5, 5);

-- ----- ------- [ DATASET QUERYING/MANIPULATION (TASK 4) ] ------- ----- --

-- ----- [ INFORMATION PROCESSING ] ----- --

-- ENTER INFO FOR A STORE ( DATA MANIPULATION )
INSERT INTO Store (ManagerID, Address, PhoneNumber) VALUES (2,"600 Sesame Street","+1(808)-690-4855");

-- UPDATE INFO FOR A STORE ( DATA MANIPULATION )
UPDATE Store SET ManagerID = 5, Address = "5450 Norwood Dr.", PhoneNumber = "+1(513)-819-6949" WHERE StoreID =1;

-- DELETE A STORE ( DATA MANIPULATION )
DELETE FROM Store WHERE StoreID = 3;

-- SEARCH INFO FOR A STORE ( DATA QUERYING )
SELECT * FROM Store WHERE StoreID = 1;


-- ENTER INFO FOR A MEMBER ( DATA MANIPULATION )
INSERT INTO Member (CustomerID, FirstName, LastName, Email, PhoneNumber, Address)
VALUES (2, "Jason", "Fletcher", "jason.fletcher89@gmail.com","+1(407)-899-8113","408 Lake Cove Point Cir.");
INSERT INTO SignUp (CustomerID, StoreID, StaffID, SignUpDate) VALUES (2, 2, 1, '2026-03-15');    


-- UPDATE INFO FOR A MEMBER ( DATA MANIPULATION )
UPDATE Member 
SET FirstName = "Jane", LastName = "Ford", Email="jford123#gmail.com", PhoneNumber = "+1(407)-827-6124", Address="613 Riverpoint Ln.", ActiveStatus = TRUE
WHERE CustomerID = 4;

-- DELETE A MEMBER ( DATA MANIPULATION )
DELETE FROM Member WHERE CustomerID = 3;
-- we can keep their sign-up for record keeping

-- SEARCH INFO FOR A MEMBER ( DATA QUERYING )
SELECT * FROM Member WHERE CustomerID = 6;

-- ----- [ MAINTAINING MERCHANDISE AND INVENTORY RECORDS ] ----- --

-- 9. Enter basic information about staff
INSERT INTO Staff (FirstName, LastName, Age, Address, Job, PhoneNumber) VALUES ('John', 'Smith', 26, '3800 Victory Pwky', 'Cashier', '7043217539');

-- 10. Update basic information about staff
UPDATE Staff SET Age = 22 WHERE StaffID = 1 ; 

-- 11. Delete basic information about staff
DELETE FROM Staff WHERE StaffID = 4;

-- 12. Search basic information about staff
SELECT FirstName, LastName, Age, Address, Job, PhoneNumber FROM Staff;

-- 13. Enter basic information about products
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (3, 'Xavier Stickers', .50, 1.00);

-- 14. Update basic information about products
UPDATE Product SET Price = 2.00 WHERE Name = 'Xavier Stickers';

-- 15. Delete basic information about products
DELETE FROM Product WHERE ProductID = 6; 

-- 16. Search basic information about products
SELECT Name, BuyPrice, SellPrice FROM Product;

-- ----- [ MAINTAINING BILLING AND TRANSACTION RECORDS ] ----- --

-- 17. Enter Basic Information about Discounts
INSERT INTO Discount (Amount, StartDate, EndDate) VALUES (10, '2026-8-31', '2026-10-15');

-- 18. Update basic information about discounts
UPDATE Discount 
SET Amount = 12, StartDate = '2026-8-31', EndDate = '2026-10-25'
WHERE DiscountID = 3;

-- 19. Delete basic information about discounts
DELETE FROM Discount WHERE DiscountID = 3;

-- 20. Search basic information about discounts
SELECT * FROM Discount WHERE DiscountID = 1;

-- 21. Increase Inventory for newly arrived Products
INSERT INTO Product (StoreID, Name, BuyPrice, SellPrice) VALUES (2, 'Xavier Jacket', 20, 100);

-- 22. Remove Inventory for Purchaces
DELETE FROM Product WHERE ProductID = 10;

-- 23. Search for inventory of a specific product;
SELECT COUNT(ProductID), StoreID FROM Product WHERE Name = 'Xavier Keychain' GROUP BY StoreID;
-- ----- [ REPORTS ] ----- --
-- 24
SELECT CustomerID 
FROM Member
WHERE ActiveStatus = 1;

-- 25
SELECT StaffID
FROM Staff;

-- 26
CREATE VIEW ProductPaymentSum AS -- Created View so we could get the Sum of what was returned in this select statemt
SELECT T.TransactionID, P.ProductID, P.SellPrice* (SUM(D.Amount)/100) * MAX(PP.Quantity) AS AmntPayed -- T.TransactionID, ((P.SellPrice * PP.Quantity) * (SUM(D.Amount)/100)) AS TotalPrice -- long formula to get total price
FROM Transaction T
RIGHT JOIN PurchasedProduct PP ON T.TransactionID = PP.TransactionID -- Our end goal is to grab stuff form the products discounts and transaction tables.
LEFT JOIN Product P ON PP.ProductID = P.ProductID 
RIGHT JOIN DiscountAppliesToProduct DtP ON P.ProductID = DtP.ProductID -- use right join becasue we only have one product ID and many discounts
LEFT JOIN Discount D ON DtP.DiscountID = D.DiscountID -- Linked Everything together Like a Chain
WHERE PP.TransactionID = 1
GROUP BY (P.ProductID);
SELECT SUM(ProductPaymentSum.AmntPayed) AS PaymentTotal FROM ProductPaymentSum ;
-- You could do the math by hand and the code matches the math by hand if you do it. So we know this is correct

-- 27
SELECT Count(*) AS Sales
FROM Transaction
WHERE StoreID = 1 AND PurchaseDate = '2026-03-05'; -- there are no products purchased on march 5th at store 1 hence it outputs 0

-- 28
SELECT Count(*) AS Sales
FROM Transaction
WHERE StoreID = 1 AND MONTH(PurchaseDate) = '3'; 

-- 29
SELECT Count(*) AS Sales
FROM Transaction
WHERE StoreID = 1 AND YEAR(PurchaseDate) = '2026'; 
-- 30
-- Our hypothetical input is going to be 1 for the store ID
SELECT ProductID, Name, BuyPrice, SellPrice
FROM Product
WHERE StoreID = 1;
-- 31
SELECT COUNT(*) AS Stock
FROM Product
WHERE Name = 'Xavier "X" hat'
GROUP BY Name;

-- 32
SELECT SUM(P.SellPrice) AS Amount_Spent, t.CustomerID -- The total amount spend for customers 
FROM Transaction t -- Using joins to chain transaction purchased prodcuct and product together.
INNER JOIN PurchasedProduct pp ON t.TransactionID = pp.TransactionID
INNER JOIN Product p ON pp.ProductID = p.ProductID -- the chain is over :D 
WHERE (t.PurchaseDate BETWEEN '2026-01-24' AND '2026-03-14') AND t.CustomerID = 1; -- get the purchases between the dates for the customer we want to look at. 
-- This will give us the total amount spent and the where is used to find the dates the joins are there because we need info from two tabels. 