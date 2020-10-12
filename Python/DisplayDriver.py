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
        query = "SELECT auth_user.username, first_name, last_name, Point_Total, Employer_ID, preferred_name, email, phone, address_, Name_ FROM (auth_user JOIN Driver_Points ON Driver_Points.Driver_User = auth_user.username) JOIN Employers ON Employer_ID = Employers.ID WHERE auth_user.username = '" + username + "';"
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
            print("pullDriverProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pullDriverProfile(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return profileObj