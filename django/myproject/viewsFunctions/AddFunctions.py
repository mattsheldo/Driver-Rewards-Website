from datetime import datetime
import mysql.connector

class DriverPoints:
    def __init__(self, pointTotal, employer, employerName):
        self.pointTotal = pointTotal
        self.employer = employer
        self.employerName = employerName

class DriverProfile:
    def __init__(self, user, first, last, pointObjs, prefName, email, phone, address):
        self.user = user
        self.first = first
        self.last = last
        self.pointObjs = pointObjs
        self.prefName = prefName
        self.email = email
        self.phone = phone
        self.address = address

def pullDriverProfile(username):
    profileObj = DriverProfile("", "", "", [], "", "", "", "")

    # Open connection
    try:
        mydb = mysql.connector.connect(
	    host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )
        # Look for all info for this driver
        myCursor = mydb.cursor()
        query = "SELECT auth_user.username, first_name, last_name, Point_Total, Employer_ID, preferred_name, email, phone, address_, Name_, Approved FROM (auth_user JOIN Driver_Points ON Driver_Points.Driver_User = auth_user.username) JOIN Employers ON Employer_ID = Employers.ID WHERE auth_user.username = '" + username + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into the profile object
            pointList = []
            pref = ""
            for d in myResults:
                if d[10] == True:
                    pointList.append(DriverPoints(d[3], d[4], d[9]))
                if d[5]:
                    pref = d[5]
                profileObj = DriverProfile(d[0], d[1], d[2], pointList, pref, d[6], d[7], d[8])
        except Exception as e:
            print("pullDriverProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pullDriverProfile(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return profileObj

def spPullDriverProfile(username, sponsor):
    profileObj = DriverProfile("", "", "", [], "", "", "", "")

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for the employer that this sponsor works for
        myID = -1
        myCursor = mydb.cursor()
        query = "SELECT Employer_ID FROM Sponsors WHERE Username = '" + sponsor + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Store the employer id
            for i in myResults:
                myID = i[0]
        except Exception as e:
            print("spPullDriverProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Look for all info for this driver
        myCursor = mydb.cursor()
        query = "SELECT auth_user.username, first_name, last_name, Point_Total, Employer_ID, preferred_name, email, phone, address_, Name_ FROM (auth_user JOIN Driver_Points ON Driver_Points.Driver_User = auth_user.username) JOIN Employers ON Employer_ID = Employers.ID WHERE auth_user.username = '" + username + "' AND Employer_ID = " + str(myID) + ";"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into the profile object
            pointList = []
            pref = ""
            for d in myResults:
                pointList.append(DriverPoints(d[3], d[4], d[9]))
                if d[5]:
                    pref = d[5]
            profileObj = DriverProfile(d[0], d[1], d[2], pointList, pref, d[6], d[7], d[8])
        except Exception as e:
            print("spPullDriverProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("spPullDriverProfile(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return profileObj

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
        today = datetime.today().strftime("%Y-%m-%d")
        # Update Point_History
        myCursor = mydb.cursor()
        query = "INSERT INTO Point_History (ID, Username, Employer_ID, Date_, Point_Cost, Type_Of_Change, Sponsor_ID) VALUES (" + str(myid) + ", '" + driver + "', " + str(employerID) + ", '" + today + "', " + str(newPoints) + ", '" + changeType + "', '" + sponsor + "');"
        try:
            # Execute query and commit
            myCursor.execute(query)
            myResults = myCursor.fetchall()
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
        today = datetime.today().strftime("%Y-%m-%d")
        # Update Point_History
        myCursor = mydb.cursor()
        query = "INSERT INTO Point_History (ID, Username, Employer_ID, Date_, Point_Cost, Type_Of_Change, Admin_ID) VALUES (" + str(myid) + ", '" + driver + "', " + str(employerID) + ", '" + today + "', " + str(newPoints) + ", '" + changeType + "', '" + admin + "');"
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
