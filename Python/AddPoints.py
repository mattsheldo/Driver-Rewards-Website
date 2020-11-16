import mysql.connector
import time
from datetime import datetime, timedelta

def setPointsAlert(driver):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Get the next available id
        myid = 0
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Driver_Alerts ORDER BY ID DESC LIMIT 1;"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
                myid = i[0] + 1
        except Exception as e:
            print("setPointsAlert(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Tell the driver that their points were updated
        myCursor = mydb.cursor()
        query = "INSERT INTO Driver_Alerts VALUES (" + str(myid) + ", '" + driver + "', 'pc', 'Your points have been updated');"
        try:
            # Execute query and get result
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("setPointsAlert(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("setPointsAlert(): Failed to connect: " + str(e))
    finally:
        mydb.close()

def addPoints(sponsor, driver, currentPoints, newPoints, addB):
    newTotal = 0
    changeType = ""
    if addB:
        newTotal = currentPoints + newPoints
        changeType = "add"
    else:
        newTotal = currentPoints - newPoints
        changeType = "sub"

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Get the sponsor's employer
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Employers JOIN Sponsors ON Employer_ID = ID WHERE Username = '" + sponsor + "';"
        employerID = -2
        try:
            # Execute query and get result
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for id in myResults:
                employerID = id[0]
        except Exception as e:
            print("addPoints(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Update driver's points
        myCursor = mydb.cursor()
        query = "UPDATE Driver_Points SET Point_Total = " + str(newTotal) + " WHERE Driver_User = '" + driver + "' AND Employer_ID = " + str(employerID) + ";"
        try:
            # Execute query and commit
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("addPoints(): Failed to update database: " + str(e))
        finally:
            myCursor.close()

        # Alert the driver
        setPointsAlert(driver)

        # Get the last used ID from Point_History
        myid = 0
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Point_History ORDER BY ID DESC LIMIT 1;"
        try:
            # Execute query
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
              myid = int(i[0]) + 1
        except Exception as e:
            print("addPoints(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Get current date
        today = time.strftime('%Y-%m-%d %H:%M:%S')
        # Update Point_History
        myCursor = mydb.cursor()
        query = "INSERT INTO Point_History (ID, Username, Employer_ID, Date_, Point_Cost, Type_Of_Change, Sponsor_ID) VALUES (" + str(myid) + ", '" + driver + "', " + str(employerID) + ", '" + today + "', " + str(newPoints) + ", '" + changeType + "', '" + sponsor + "');"
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

def addPointsAdmin(admin, driver, currentPoints, newPoints, addB, employerID):
    newTotal = 0
    changeType = ""
    if addB:
        newTotal = currentPoints + newPoints
        changeType = "add"
    else:
        newTotal = currentPoints - newPoints
        changeType = "sub"

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
        query = "UPDATE Driver_Points SET Point_Total = " + str(newTotal) + " WHERE Driver_User = '" + driver + "' AND Employer_ID = " + str(employerID) + ";"
        try:
            # Execute query and commit
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("addPointsAdmin(): Failed to update database: " + str(e))
        finally:
            myCursor.close()

        # Alert the driver
        setPointsAlert(driver)

        # Get the last used ID from Point_History
        myid = 0
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Point_History ORDER BY ID DESC LIMIT 1;"
        try:
            # Execute query
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
              myid = int(i[0]) + 1
        except Exception as e:
            print("addPointsAdmin(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Get current date
        today = time.strftime('%Y-%m-%d %H:%M:%S')
        # Update Point_History
        myCursor = mydb.cursor()
        query = "INSERT INTO Point_History (ID, Username, Employer_ID, Date_, Point_Cost, Type_Of_Change, Admin_ID) VALUES (" + str(myid) + ", '" + driver + "', " + str(employerID) + ", '" + today + "', " + str(newPoints) + ", '" + changeType + "', '" + admin + "');"
        try:
            # Execute query and commit
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("addPointsAdmin(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("addPointsAdmin(): Failed to connect: " + str(e))
    finally:
        mydb.close()