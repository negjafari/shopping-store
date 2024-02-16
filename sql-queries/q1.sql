-- CREATE DATABASE shop;

-- USE shop;

-- CREATE TABLE IF NOT EXISTS Address(
--   ID INT NOT NULL auto_increment, 
--   Country VARCHAR(45) NOT NULL, 
--   City VARCHAR(45) NOT NULL, 
--   Street VARCHAR(45) NOT NULL, 
--   BlockNumber INT NOT NULL, 
--   Location VARCHAR(45) NULL, 
--   Phone VARCHAR(20) NULL, 
--   PostalCode VARCHAR(20) NULL, 
--   PRIMARY KEY (ID)
-- ) ENGINE = InnoDB;



-- CREATE TABLE IF NOT EXISTS Shop(
--   ID INT NOT NULL AUTO_INCREMENT, 
--   ManagerName VARCHAR(20) NOT NULL, 
--   AddressID INT NOT NULL, 
--   Email VARCHAR(45) NULL, 
--   PRIMARY KEY(ID), 
--   FOREIGN KEY(AddressID) REFERENCES Address(ID) ON DELETE CASCADE ON UPDATE CASCADE
-- ) ENGINE = InnoDB;



-- CREATE TABLE IF NOT EXISTS CustomerProfile(
--   ID INT NOT NULL auto_increment, 
--   Username VARCHAR(45) NOT NULL, 
--   UserPassword INT NOT NULL, 
--   Email VARCHAR(45) NOT NULL, 
--   PRIMARY KEY (ID)
-- ) engine = InnoDB;


-- CREATE TABLE IF NOT EXISTS Customer(
--   ID INT NOT NULL auto_increment, 
--   FullName VARCHAR(45) NOT NULL, 
--   LastTimeVisited DATE NULL, 
--   BirthDate DATE NULL, 
--   AddressID INT NOT NULL, 
--   ProfileID INT NOT NULL, 
--   ShopID INT NOT NULL, 
--   PRIMARY KEY (`ID`), 
--   FOREIGN KEY (AddressID) REFERENCES Address(ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (ProfileID) REFERENCES CustomerProfile (ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (ShopID) REFERENCES Shop (ID) ON DELETE CASCADE ON UPDATE CASCADE
-- ) engine = InnoDB;


-- CREATE TABLE IF NOT EXISTS Provider(
--   ID INT NOT NULL auto_increment, 
--   PName VARCHAR(45) NOT NULL, 
--   Email VARCHAR(45) NULL, 
--   ShopID INT NOT NULL, 
--   AddressID INT NOT NULL, 
--   PRIMARY KEY (ID), 
--   FOREIGN KEY (ShopID) REFERENCES Shop (ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (AddressID) REFERENCES Address(ID) ON DELETE CASCADE ON UPDATE CASCADE
-- ) engine = InnoDB;


-- CREATE TABLE IF NOT EXISTS Staff(
--   ID INT NOT NULL auto_increment, 
--   SName VARCHAR(45) NOT NULL, 
--   Salary INT NOT NULL, 
--   BirthDate DATE NULL, 
--   Email VARCHAR(45) NULL, 
--   AddressID INT NOT NULL, 
--   ManagerID INT NOT NULL, 
--   ShopID INT NOT NULL, 
--   PRIMARY KEY (ID), 
--   FOREIGN KEY (AddressID) REFERENCES Address(ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (ManagerID) REFERENCES Staff(ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (ShopID) REFERENCES Shop(ID) ON DELETE CASCADE ON UPDATE CASCADE
-- ) ENGINE = InnoDB;



-- CREATE TABLE IF NOT EXISTS Category(
--   ID INT NOT NULL auto_increment, 
--   CategoryName VARCHAR(45) NOT NULL, 
--   PRIMARY KEY (ID)
-- ) ENGINE = InnoDB;


-- CREATE TABLE IF NOT EXISTS Product (
--   ID INT NOT NULL auto_increment, 
--   Price INT NOT NULL, 
--   Brand VARCHAR(45) NULL, 
--   ProductName VARCHAR(45) NOT NULL, 
--   CategoryID INT NOT NULL, 
--   ShopID INT NOT NULL, 
--   Discount INT NOT NULL,
--   PRIMARY KEY (ID), 
--   FOREIGN KEY (CategoryID) REFERENCES Category(ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (ShopID) REFERENCES Shop(ID) ON DELETE CASCADE ON UPDATE CASCADE
-- ) ENGINE = InnoDB;


-- CREATE TABLE product_provider (
--   ID int NOT NULL AUTO_INCREMENT, 
--   ProviderID int NOT NULL, 
--   ProductID int NOT NULL, 
--   Price int NOT NULL, 
--   PRIMARY KEY (ID), 
--   FOREIGN KEY (ProductID) REFERENCES product (ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (ProviderID) REFERENCES provider (ID) ON DELETE CASCADE ON UPDATE CASCADE
-- ) ENGINE = InnoDB;


-- CREATE TABLE product_review (
-- ID int NOT NULL AUTO_INCREMENT,
-- Title varchar(100) NOT NULL,
-- Rating smallint DEFAULT NULL,
-- Published tinyint(1) NOT NULL,
-- CreatedAt datetime DEFAULT NULL,
-- PublishedAt datetime DEFAULT NULL,
-- Content text,
-- productID int not null,
-- PRIMARY KEY (ID),
-- FOREIGN KEY (productID) REFERENCES product (ID)
-- ) ENGINE = InnoDB;


-- CREATE TABLE IF NOT EXISTS Factor(
--   ID INT NOT NULL auto_increment, 
--   TotalPrice INT NOT NULL, 
--   TotalDiscount FLOAT NOT NULL, 
--   Date datetime NOT NULL, 
--   PRIMARY KEY (ID)
-- ) ENGINE = InnoDB;


-- CREATE TABLE IF NOT EXISTS Report(
--   ID INT NOT NULL auto_increment, 
--   TotalDiscount FLOAT NOT NULL, 
--   SalesNumber INT NOT NULL, 
--   FactorID INT NOT NULL, 
--   ShopID INT NOT NULL, 
--   PRIMARY KEY (ID), 
--   FOREIGN KEY (FactorID) REFERENCES Factor(ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (ShopID) REFERENCES Shop(ID) ON DELETE CASCADE ON UPDATE CASCADE
-- ) engine = InnoDB;


-- CREATE TABLE IF NOT EXISTS ShoppingCart(
--   ID INT NOT NULL auto_increment, 
--   ProfileID INT NOT NULL, 
--   FactorID INT NOT NULL, 
--   PRIMARY KEY (ID), 
--   FOREIGN KEY (ProfileID) REFERENCES CustomerProfile(ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (FactorID) REFERENCES Factor(ID) ON DELETE CASCADE ON UPDATE CASCADE
-- ) ENGINE = InnoDB;


-- CREATE TABLE IF NOT EXISTS CartItem(
--   ID INT NOT NULL auto_increment, 
--   Discount FLOAT NOT NULL, 
--   Count INT NOT NULL, 
--   TotalPrice INT NOT NULL, 
--   ShoppingCartID INT NOT NULL, 
--   ProductID INT NOT NULL, 
--   PRIMARY KEY (ID), 
--   FOREIGN KEY (ShoppingCartID) REFERENCES ShoppingCart(ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (ProductID) REFERENCES Product(ID) ON DELETE CASCADE ON UPDATE CASCADE
-- ) ENGINE = InnoDB;


-- CREATE TABLE IF NOT EXISTS Transaction(
--   ID INT NOT NULL auto_increment, 
--   TransactionType VARCHAR(45) NOT NULL, 
--   TracingNumber INT NOT NULL, 
--   TransactionDate DATE NOT NULL, 
--   FactorID INT NOT NULL, 
--   customerID INT NOT NULL, 
--   PRIMARY KEY (ID), 
--   FOREIGN KEY (FactorID) REFERENCES Factor(ID) ON DELETE CASCADE ON UPDATE CASCADE, 
--   FOREIGN KEY (customerID) REFERENCES customer (ID) ON DELETE CASCADE ON UPDATE CASCADE
-- ) ENGINE = InnoDB;









