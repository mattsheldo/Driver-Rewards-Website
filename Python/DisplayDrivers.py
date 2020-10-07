import mysql.connector

class DriverListItem:
    def __init__(self, first, last, pointTotal, user):
        self.first = first
        self.last = last
        self.pointTotal = pointTotal
        self.user = user

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

        # Look for all drivers under the current sponsor
        myCursor = mydb.cursor()
        query = "SELECT auth_user.first_name, auth_user.last_name, Drivers.Point_Total, auth_user.username FROM (Drivers JOIN Sponsors ON Drivers.Employer_ID = Sponsors.Employer_ID) JOIN auth_user ON Drivers.Username = auth_user.username WHERE Sponsors.Username = '" + sponsor + "' ORDER BY auth_user.last_name, auth_user.first_name;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into a list
            for d in myResults:
                driverNames.append(DriverListItem(d[0], d[1], d[2], d[3]))
        except Exception as e:
            print("pulldownDrivers(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pulldownDrivers(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return driverNames