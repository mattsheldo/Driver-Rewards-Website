import mysql.connector

def verifyAccount(userUser):
    returnType = ""

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass"
        )

        # Look for a match in Drivers
        myCursor = mydb.cursor()
        query = "SELECT * FROM DriverRewards.Drivers WHERE Username = '" + userUser + "';"
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
        except Exception:
            print("verifyAccount(): Failed to query Drivers")
        finally:
            myCursor.close()

        # Look for a match in Sponsors
        myCursor = mydb.cursor()
        query = "SELECT * FROM DriverRewards.Sponsors WHERE Username = '" + userUser + "';"
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
        except Exception:
            print("verifyAccount(): Failed to query Sponsors")
        finally:
            myCursor.close()

        # Look for a match in Admins
        myCursor = mydb.cursor()
        query = "SELECT * FROM DriverRewards.Admins WHERE Username = '" + userUser + "';"
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
        except Exception:
            print("verifyAccount(): Failed to query Admins")
        finally:
            myCursor.close()
    except Exception:
        print("verifyAccount(): Failed to connect")
    finally:
        mydb.close()
        return returnType
  
def findUsername():
    # Goal: find username of the most recent login to pass to verifyAccount()
    returnVal = ""
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass"
        )

        # Look for the most recent login
        myCursor = mydb.cursor()
        query = "SELECT username FROM DriverRewards.auth_user ORDER BY last_login DESC;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Get first result
            for x in myResults:
                returnVal = x
                myCursor.close()
                mydb.close()
                return returnVal
        except Exception:
            print("verifyAccount(): Failed to query auth_user")
        finally:
            myCursor.close()
    except Exception:
        print("verifyAccount(): Failed to connect")
    finally:
        mydb.close()
        return returnVal