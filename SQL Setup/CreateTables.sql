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
  Preferred_Name VARCHAR(50),
  Phone_Number CHAR(10) NOT NULL,
  Email VARCHAR(100) NOT NULL,
  Address_ VARCHAR(200) NOT NULL,
  CONSTRAINT AccPK PRIMARY KEY(Username)
);

CREATE TABLE Drivers(
  Username VARCHAR(150) NOT NULL,
  Employer_ID INT NOT NULL,
  CONSTRAINT DrPK PRIMARY KEY(Username),
  CONSTRAINT DrAccFK FOREIGN KEY(Username) REFERENCES auth_user(username),
  CONSTRAINT DrEmpFK FOREIGN KEY(Employer_ID) REFERENCES Employers(ID)
);

CREATE TABLE Sponsors(
  Username VARCHAR(150) NOT NULL,
  Employer_ID INT NOT NULL,
  CONSTRAINT SpPK PRIMARY KEY(Username),
  CONSTRAINT SpAccFK FOREIGN KEY(Username) REFERENCES auth_user(username),
  CONSTRAINT SpEmpFK FOREIGN KEY(Employer_ID) REFERENCES Employers(ID)
);

CREATE TABLE Admins(
  Username VARCHAR(150) NOT NULL,
  CONSTRAINT AdPK PRIMARY KEY(Username),
  CONSTRAINT AdAccFK FOREIGN KEY(Username) REFERENCES auth_user(username)
);

-- Create an entry for each point change
CREATE TABLE Point_History(
  ID INT NOT NULL,
  Username VARCHAR(150) NOT NULL,
  Employer_ID INT NOT NULL,
  Date_ DATE NOT NULL,
  Point_Cost INT NOT NULL,
  Type_Of_Change CHAR(3) NOT NULL,     -- add or sub
  Sponsor_ID VARCHAR(150),     -- Either Sponsor_ID or Admin_ID can be NULL, but NOT BOTH
  Admin_Id VARCHAR(150),
  CONSTRAINT PntPK PRIMARY KEY(ID),
  CONSTRAINT PntAccFK FOREIGN KEY(Username) REFERENCES Drivers(Username),
  CONSTRAINT PntSpFK FOREIGN KEY(Sponsor_ID) REFERENCES Sponsors(Username),
  CONSTRAINT PntAdmFK FOREIGN KEY(Admin_Id) REFERENCES Admins(Username),
  CONSTRAINT PntEmpFK FOREIGN KEY(Employer_ID) REFERENCES Employers(ID)
);

-- Create an entry for each item in a cart
CREATE TABLE Shopping_Cart_Items(
  ID INT NOT NULL,
  Username VARCHAR(150) NOT NULL,
  Employer_ID INT NOT NULL,
  Point_Cost INT NOT NULL,
  Product_Name VARCHAR(150) NOT NULL,
  Sponsor_ID VARCHAR(150),
  Admin_Id VARCHAR(150),
  CONSTRAINT CrtPK PRIMARY KEY(ID),
  CONSTRAINT CrtAccFK FOREIGN KEY(Username) REFERENCES Drivers(Username),
  CONSTRAINT CrtSpFK FOREIGN KEY(Sponsor_ID) REFERENCES Sponsors(Username),
  CONSTRAINT CrtAdmFK FOREIGN KEY(Admin_Id) REFERENCES Admins(Username),
  CONSTRAINT CrtEmpFK FOREIGN KEY(Employer_ID) REFERENCES Employers(ID)
);

-- Create an entry for each item purchased
CREATE TABLE Purchase_History(
  ID INT NOT NULL,
  Username VARCHAR(150) NOT NULL,
  Employer_ID INT NOT NULL,
  Date_ DATE NOT NULL,
  Point_Total INT NOT NULL,
  Product_Name VARCHAR(150) NOT NULL,
  Completed BOOLEAN NOT NULL,     -- False until 24 hours has passed from time of purchase
  Sponsor_ID VARCHAR(150),
  Admin_Id VARCHAR(150),
  CONSTRAINT PchPK PRIMARY KEY(ID),
  CONSTRAINT PchAccFK FOREIGN KEY(Username) REFERENCES Drivers(Username),
  CONSTRAINT PchSpFK FOREIGN KEY(Sponsor_ID) REFERENCES Sponsors(Username),
  CONSTRAINT PchAdmFK FOREIGN KEY(Admin_Id) REFERENCES Admins(Username),
  CONSTRAINT PchEmpFK FOREIGN KEY(Employer_ID) REFERENCES Employers(ID)
);

CREATE TABLE Driver_Points(
  Driver_User VARCHAR(150) NOT NULL,
  Employer_ID INT NOT NULL,
  Point_Total INT NOT NULL,
  CONSTRAINT DPPk PRIMARY KEY(Driver_User, Employer_ID),
  CONSTRAINT DPDrFK FOREIGN KEY(Driver_User) REFERENCES Drivers(Username),
  CONSTRAINT DPEmpFK FOREIGN KEY(Employer_ID) REFERENCES Employers(ID)
);