import mysql.connector

class DriverProfile:
    def __init__(self, user, first, last, pointTotal, prefName, email, phone, address):
        self.user = user
        self.first = first
        self.last = last
        self.pointTotal = pointTotal
        self.prefName = prefName
        self.email = email
        self.phone = phone
        self.address = address

def pullDriverProfile(username):
    profileObj = DriverProfile("", "", "", 0, "", "", "", "")

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
        query = "SELECT auth_user.username, first_name, last_name, Point_Total, preferred_name, email, phone, address_ FROM auth_user JOIN Drivers ON Drivers.Username = auth_user.username WHERE auth_user.username = '" + username + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into the profile object
            for d in myResults:
                pref = ""
                if d[4]:
                    pref = d[4]
                profileObj = DriverProfile(d[0], d[1], d[2], d[3], pref, d[5], d[6], d[7])
        except Exception as e:
            print("pullDriverProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pullDriverProfile(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return profileObj