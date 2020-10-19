import mysql.connector
from random import choice

def createCompany(sponsor, name):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Get last used ID in Employers
        myID = -1
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Employers ORDER BY ID DESC LIMIT 1;"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
                myID = i[0] + 1
        except Exception as e:
            print("createCompany(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Get the code of every company in the database already
        codeList = []
        myCursor = mydb.cursor()
        query = "SELECT Join_Code FROM Employers;"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for c in myResults:
                codeList.append(c[0])
        except Exception as e:
            print("createCompany(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
        # Get a random join code
        code = choice([i for i in range(100000, 999999) if i not in codeList])

        # Create the Employer
        myCursor = mydb.cursor()
        query = "INSERT INTO Employers VALUES (" + str(myID) + ", '" + name + "', 100, " + str(code) + ");"
        try:
            # Execute query and get results
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("createCompany(): Failed to update database: " + str(e))
        finally:
            myCursor.close()

        # Update the sponsor's employer
        myCursor = mydb.cursor()
        query = "UPDATE Sponsors SET Employer_ID = " + str(myID) + " WHERE Username = '" + sponsor + "';"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("createCompany(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("createCompany(): Failed to connect: " + str(e))
    finally:
        mydb.close()

def joinCompany(sponsor, code):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Find the Employer's ID from the join code
        myID = -1
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Employers WHERE Join_Code = " + str(code) + ";"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
                myID = i[0]
        except Exception as e:
            print("joinCompany(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Update the sponsor's employer
        myCursor = mydb.cursor()
        query = "UPDATE Sponsors SET Employer_ID = " + str(myID) + " WHERE Username = '" + sponsor + "';"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("joinCompany(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("joinCompany(): Failed to connect: " + str(e))
    finally:
        mydb.close()