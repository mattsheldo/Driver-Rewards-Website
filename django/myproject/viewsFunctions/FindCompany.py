import mysql.connector

def applyToCompany(driver, code):
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

            # If no match found, just return
            if len(myResults) == 0:
                myCursor.close()
                mydb.close()
                return

            for i in myResults:
                myID = i[0]
        except Exception as e:
            print("applyToCompany(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Check if the driver is already in this company's system
        myCursor = mydb.cursor()
        query = "SELECT Employer_ID FROM Driver_Points WHERE Driver_User = '" + driver + "' AND Employer_ID = " + str(myID) + ";"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # If they are in the system, stop the request to join
            if len(myResults) > 0:
                myCursor.close()
                mydb.close()
                return
        except Exception as e:
            print("applyToCompany(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Add the driver to that employer, but don't mark approved yet
        myCursor = mydb.cursor()
        query = "INSERT INTO Driver_Points VALUES ('" + driver + "', " + str(myID) + ", 0, false);"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("applyToCompany(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("applyToCompany(): Failed to connect: " + str(e))
    finally:
        mydb.close()
