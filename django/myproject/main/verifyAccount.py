import mysql.connector

def verifyAccount(userUser):
    returnType = ""

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for a match in Drivers
        myCursor = mydb.cursor()
        query = "SELECT * FROM Drivers WHERE Username = '" + userUser + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # If a result is found, then there's a match
            if len(myResults) > 0:
                # Driver found
                returnType = "d"
                myCursor.close()
                mydb.close()
                return returnType
        except Exception as e:
            print("verifyAccount(): Failed to query Drivers: " + str(e))
        finally:
            myCursor.close()
 
        # Look for a match in Sponsors
        myCursor = mydb.cursor()
        query = "SELECT * FROM Sponsors WHERE Username = '" + userUser + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # If a result is found, then there's a match
            if len(myResults) > 0:
                # Sponsor found
                returnType = "s"
                myCursor.close()
                mydb.close()
                return returnType
                    
        except Exception as e:
            print("verifyAccount(): Failed to query Sponsors: " + str(e))
        finally:
            myCursor.close()

        # Look for a match in Admins
        myCursor = mydb.cursor()
        query = "SELECT * FROM Admins WHERE Username = '" + userUser + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # If a result is found, then there's a match
            if len(myResults) > 0:
                # Admin found
                returnType = "a"
                myCursor.close()
                mydb.close()
                return returnType
        except Exception as e:
            print("verifyAccount(): Failed to query Admins: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("verifyAccount(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return returnType
