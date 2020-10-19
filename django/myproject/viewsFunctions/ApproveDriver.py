import mysql.connector

def approveDriver(driver, sponsor, acc):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Find the common employer between the driver and sponsor
        empID = -1
        myCursor = mydb.cursor()
        query = "SELECT DP.Employer_ID FROM Driver_Points as DP JOIN Sponsors ON DP.Employer_ID = Sponsors.Employer_ID WHERE Driver_User = '" + driver + "' AND Username = '" + sponsor + "';"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
                empID = i[0]
        except Exception as e:
            print("approveDriver(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        myCursor = mydb.cursor()
        # If approved, change the driver's status to approved
        if acc:
            query = "UPDATE Driver_Points SET Approved = true WHERE Driver_User = '" + driver + "' AND Employer_ID = " + str(empID) + ";"
        else:
            query = "DELETE FROM Driver_Points WHERE Driver_User = '" + driver + "' AND Employer_ID = " + str(empID) + ";"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("approveDriver(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("approveDriver(): Failed to connect: " + str(e))
    finally:
        mydb.close()
