import mysql.connector
from datetime import datetime

def addPoints(sponsor, driver, currentPoints, newPoints):
    newTotal = currentPoints + newPoints

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Update driver's points
        myCursor = mydb.cursor()
        query = "UPDATE Drivers SET Point_Total = " + newTotal + " WHERE Username = '" + driver + "';"
        try:
            # Execute query and commit
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("addPoints(): Failed to update database: " + str(e))
        finally:
            myCursor.close()

        # Get the last used ID from Point_History
        myid = -1
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Point_History WHERE Username = '" + driver + "';"
        try:
            # Execute query
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
              myid = i[0] + 1
        except Exception as e:
            print("addPoints(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Get current date
        today = datetime.today().strftime("%Y-%m-%d")
        # Update Point_History
        myCursor = mydb.cursor()
        query = "INSERT INTO Point_History (ID, Username, Date_, Point_Cost, Type_Of_Change, Sponsor_ID) VALUES (" + myid + ", '" + driver + "', '" + today + "', " + newPoints + ", 'add', '" + sponsor + "');"
        try:
            # Execute query and commit
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("addPoints(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("addPoints(): Failed to connect: " + str(e))
    finally:
        mydb.close()