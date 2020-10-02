import mysql.connector  

def findUsername():
    # Goal: find username of the most recent login to pass to verifyAccount()
    returnVal = ""
    # Open connection
    try:
        mydb = mysql.connector.connect(    
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for the most recent login
        myCursor = mydb.cursor()
        query = "SELECT username FROM auth_user ORDER BY last_login DESC;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Get first result
            for x in myResults:
                returnVal = x[0]
                myCursor.close()
                mydb.close()
                return returnVal
                
        except Exception as e:
            print("verifyAccount(): Failed to query auth_user: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("verifyAccount(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return returnVal
