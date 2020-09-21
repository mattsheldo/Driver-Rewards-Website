-- Create tables for CPSC 4910 project
CREATE TABLE Employers(
  ID INT NOT NULL,
  Name_ VARCHAR(50) NOT NULL,
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
  Encrypted_Password VARCHAR(25) NOT NULL,     -- Max password length = 20 (leave 5 characters for salting)
  First_Name VARCHAR(20) NOT NULL,
  Last_Name VARCHAR(20) NOT NULL,
  Preferred_Name VARCHAR(20),
  Phone_Number CHAR(10) NOT NULL,
  Email VARCHAR(50) NOT NULL,
  Address_ VARCHAR(100) NOT NULL,
  Approved BOOLEAN NOT NULL,     -- False upon account creation until approved
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

CREATE TABLE Point_History(
  Username VARCHAR(20) NOT NULL,
  Date_ DATE NOT NULL,
  Point_Cost INT NOT NULL,
  Type_Of_Change VARCHAR(11),     -- addition or subtraction
  Sponsor_Admin_ID VARCHAR(25) NOT NULL,     -- Merely here for the driver's benefit, no required relationship
  CONSTRAINT PntPK PRIMARY KEY(Username),
  CONSTRAINT PntAccFK FOREIGN KEY(Username) REFERENCES Drivers(Username)
);

CREATE TABLE Shopping_Carts(
  Username VARCHAR(20) NOT NULL,
  Current_Total INT NOT NULL,
  Product_Name VARCHAR(20),     -- TODO: Figure this out
  Sponsor_Admin_ID VARCHAR(20),     -- Merely here for the driver's benefit, no required relationship
  CONSTRAINT SCPK PRIMARY KEY(Username),
  CONSTRAINT SCAccFK FOREIGN KEY(Username) REFERENCES Drivers(Username)
);

CREATE TABLE Purchase_History(
  Username VARCHAR(20) NOT NULL,
  Date_ DATE NOT NULL,
  Point_Total INT NOT NULL,
  Product_Name VARCHAR(20),     -- TODO: Figure this out
  Completed BOOLEAN NOT NULL,     -- False until 24 hours has passed from time of purchase
  Sponsor_Admin_ID VARCHAR(20),     -- Merely here for the driver's benefit, no required relationship
  CONSTRAINT PchPK PRIMARY KEY(Username),
  CONSTRAINT PchAccFK FOREIGN KEY(Username) REFERENCES Drivers(Username)
);