import mysql.connector

def addUserTypeInfo(userUser,userType):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        myCursor = mydb.cursor()
        query = "INSERT INTO Drivers (Username, Employer_ID, Point_Total) VALUES ('iamuser', -1, 0);"
#        if userType is 'Driver':
#            query = "INSERT INTO Drivers (Username, Employer_ID, Point_Total) VALUES ('iamuser', -1, 0);"
            #val = (userUser,-1,0)
#        elif userType is 'Sponsor':
#            query = "INSERT INTO Sponsors (Username, Employer_ID) VALUES (%s,%d);"
#            val = (userUser,-1)
#        else:
#            query = "INSERT INTO Admins (Username) VALUES (%s);"
#            val = (userUser)
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception:
            print("verifyAccount(): Failed to query")
        finally:
            myCursor.close()
            mydb.close()
    except Exception:
        print("verifyAccount(): Failed to connect")
    finally:
        mydb.close()
