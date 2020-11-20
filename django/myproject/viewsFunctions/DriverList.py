from viewsFunctions.AddFunctions import DriverPoints
import mysql.connector

class DriverListItem:
    def __init__(self, first, last, pointTotal, user, pointsObj):
        self.first = first
        self.last = last
        self.pointTotal = pointTotal
        self.user = user
        self.pointsObj = pointsObj
    
def pulldownDrivers(sponsor):
    driverNames = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all driver under the current sponsor
        myCursor = mydb.cursor()
        query = "SELECT auth_user.first_name, auth_user.last_name, Driver_Points.Point_Total, auth_user.username FROM (Driver_Points JOIN Sponsors ON Driver_Points.Employer_ID = Sponsors.Employer_ID) JOIN auth_user ON Driver_Points.Driver_User = auth_user.username WHERE Sponsors.Username LIKE '" + sponsor + "' AND Approved = true ORDER BY auth_user.last_name, auth_user.first_name;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into a list
            for d in myResults:
                driverNames.append(DriverListItem(d[0], d[1], d[2], d[3], []))
        except Exception as e:
            print("pulldownDrivers(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pulldownDrivers(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return driverNames

def pullPendingDrivers(sponsor):
    driverNames = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all drivers under the current sponsor not approved
        myCursor = mydb.cursor()
        query = "SELECT auth_user.first_name, auth_user.last_name, Driver_Points.Point_Total, auth_user.username FROM (Driver_Points JOIN Sponsors ON Driver_Points.Employer_ID = Sponsors.Employer_ID) JOIN auth_user ON Driver_Points.Driver_User = auth_user.username WHERE Sponsors.Username LIKE '" + sponsor + "' AND Approved = false ORDER BY auth_user.last_name, auth_user.first_name;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into a list
            for d in myResults:
                driverNames.append(DriverListItem(d[0], d[1], d[2], d[3], []))
        except Exception as e:
            print("pullPendingDrivers(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pullPendingDrivers(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return driverNames

def adminPulldownDrivers():
    driverNames = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all drivers
        myCursor = mydb.cursor()
        query = "SELECT first_name, last_name, Point_Total, username, Employers.ID, Employers.Name_ FROM (Driver_Points JOIN auth_user ON Driver_User = username) JOIN Employers ON Employer_ID = Employers.ID ORDER BY auth_user.last_name, auth_user.first_name, Employers.Name_;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into a list
            employers = []
            # Stores the username of the last driver read in
            pastDriver = ""
            item = DriverListItem("", "", 0, "", [])
            first = True
            for d in myResults:
                if first:
                    first = False
                    pastDriver = d[3]
                # If there are no more employers for this driver, update driverNames
                if pastDriver != d[3]:
                    pastDriver = d[3]
                    driverNames.append(item)
                    item = DriverListItem("", "", 0, "", [])
                    employers = []

                # Get current info
                if d[4] > -1:
                    employers.append(DriverPoints(d[2], d[4], d[5]))
                item = DriverListItem(d[0], d[1], 0, d[3], employers)
        except Exception as e:
            print("pulldownDrivers(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pulldownDrivers(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return driverNames


def addTempUname(username):

    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()

    query = "UPDATE Drivers SET Temp_Uname = '"+username+"' WHERE Username = 'dummydriver';"
    myCursor.execute(query)
    myCursor.close()
    mydb.commit()
    mydb.close()


def addTempUnameSponsor(username):

    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()

    query = "UPDATE Sponsors SET Temp_Uname = '"+username+"' WHERE Username = 'dummysponsor';"
    myCursor.execute(query)
    myCursor.close()
    mydb.commit()
    mydb.close()



def removeTempName(username):

    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()

    query = "UPDATE Drivers SET Temp_Uname = '' WHERE Username = 'dummydriver';"
    myCursor.execute(query)
    myCursor.close()
    mydb.commit()
    mydb.close()



def getTempName(username):
    name = ""
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()

    query = "SELECT Temp_Uname FROM Drivers WHERE Username = '"+username+"';"
    
    myCursor.execute(query)
    myResults = myCursor.fetchall()

    name = myResults[0][0]

    myCursor.close()
    mydb.close()
    return name


def getTempNameSponsor(username):
    name = ""
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()

    query = "SELECT Temp_Uname FROM Sponsors WHERE Username = '"+username+"';"

    myCursor.execute(query)
    myResults = myCursor.fetchall()

    name = myResults[0][0]

    myCursor.close()
    mydb.close()
    return name



