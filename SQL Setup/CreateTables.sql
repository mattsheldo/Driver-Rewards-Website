-- Create tables for CPSC 4910 project
CREATE TABLE Employers(
  ID INT NOT NULL,
  Name_ VARCHAR(50) NOT NULL,
  PointsPerDollar DECIMAL(6, 2) NOT NULL,     -- 1 by default -- I don't expect more than 1,000 points/dollar
  CONSTRAINT EmpPK PRIMARY KEY(ID)
);

CREATE TABLE Invoices(
  ID INT NOT NULL,
  Month_End_Date DATE NOT NULL,
  Total DECIMAL(8, 2) NOT NULL,     -- I don't expect totals to hit $1 million
  Employer_ID INT NOT NULL,
  Paid BOOLEAN NOT NULL,     -- False upon invoice creation until paid off
  CONSTRAINT InvPK PRIMARY KEY(ID),
  CONSTRAINT InvEmpFK FOREIGN KEY(Employer_ID) REFERENCES Employers(ID)
);

CREATE TABLE Accounts(
  Username VARCHAR(20) NOT NULL,
  Encrypted_Password VARCHAR(80) NOT NULL,     -- Store the hashed password assuming SHA-256 method
  First_Name VARCHAR(20) NOT NULL,
  Last_Name VARCHAR(20) NOT NULL,
  Preferred_Name VARCHAR(20),
  Phone_Number CHAR(10) NOT NULL,
  Email VARCHAR(50) NOT NULL,
  Address_ VARCHAR(100) NOT NULL,
  CONSTRAINT AccPK PRIMARY KEY(Username)
);

CREATE TABLE Drivers(
  Username VARCHAR(20) NOT NULL,
  Employer_ID INT NOT NULL,
  Point_Total INT NOT NULL,
  CONSTRAINT DrPK PRIMARY KEY(Username),
  CONSTRAINT DrAccFK FOREIGN KEY(Username) REFERENCES Accounts(Username),
  CONSTRAINT DrEmpFK FOREIGN KEY(Employer_ID) REFERENCES Employers(ID)
);

CREATE TABLE Sponsors(
  Username VARCHAR(20) NOT NULL,
  Employer_ID INT NOT NULL,
  CONSTRAINT SpPK PRIMARY KEY(Username),
  CONSTRAINT SpAccFK FOREIGN KEY(Username) REFERENCES Accounts(Username),
  CONSTRAINT SpEmpFK FOREIGN KEY(Employer_ID) REFERENCES Employers(ID)
);

CREATE TABLE Admins(
  Username VARCHAR(20) NOT NULL,
  CONSTRAINT AdPK PRIMARY KEY(Username),
  CONSTRAINT AdAccFK FOREIGN KEY(Username) REFERENCES Accounts(Username)
);

-- Create an entry for each point change
CREATE TABLE Point_History(
  ID INT NOT NULL,
  Username VARCHAR(20) NOT NULL,
  Date_ DATE NOT NULL,
  Point_Cost INT NOT NULL,
  Type_Of_Change CHAR(3) NOT NULL,     -- add or sub
  Sponsor_ID VARCHAR(25),     -- Either Sponsor_ID or Admin_ID can be NULL, but NOT BOTH
  Admin_Id VARCHAR(25),
  CONSTRAINT PntPK PRIMARY KEY(ID),
  CONSTRAINT PntAccFK FOREIGN KEY(Username) REFERENCES Drivers(Username),
  CONSTRAINT PntSpFK FOREIGN KEY(Sponsor_ID) REFERENCES Sponsors(Username),
  CONSTRAINT PntAdmFK FOREIGN KEY(Admin_Id) REFERENCES Admins(Username)
);

-- Create an entry for each item in a cart
CREATE TABLE Shopping_Cart_Items(
  ID INT NOT NULL,
  Username VARCHAR(20) NOT NULL,
  Point_Cost INT NOT NULL,
  Product_Name VARCHAR(20) NOT NULL,
  Sponsor_ID VARCHAR(25),
  Admin_Id VARCHAR(25),
  CONSTRAINT CrtPK PRIMARY KEY(ID),
  CONSTRAINT CrtAccFK FOREIGN KEY(Username) REFERENCES Drivers(Username),
  CONSTRAINT CrtSpFK FOREIGN KEY(Sponsor_ID) REFERENCES Sponsors(Username),
  CONSTRAINT CrtAdmFK FOREIGN KEY(Admin_Id) REFERENCES Admins(Username)
);

-- Create an entry for each item purchased
CREATE TABLE Purchase_History(
  ID INT NOT NULL,
  Username VARCHAR(20) NOT NULL,
  Date_ DATE NOT NULL,
  Point_Total INT NOT NULL,
  Product_Name VARCHAR(20) NOT NULL,
  Completed BOOLEAN NOT NULL,     -- False until 24 hours has passed from time of purchase
  Sponsor_ID VARCHAR(25),
  Admin_Id VARCHAR(25),
  CONSTRAINT PchPK PRIMARY KEY(ID),
  CONSTRAINT PchAccFK FOREIGN KEY(Username) REFERENCES Drivers(Username),
  CONSTRAINT PchSpFK FOREIGN KEY(Sponsor_ID) REFERENCES Sponsors(Username),
  CONSTRAINT PchAdmFK FOREIGN KEY(Admin_Id) REFERENCES Admins(Username)
);