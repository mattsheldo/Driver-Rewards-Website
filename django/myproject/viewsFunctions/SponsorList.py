import mysql.connector

class SponsorListItem:
    def __init__(self, first, last, user, pVal):
        self.first = first
        self.last = last
        self.user = user
        self.pVal = pVal

def pulldownAdmins():
    adminNames = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
	    host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
	    password="adminpass",
	    database="DriverRewards"
	)

        # Look for all admins
        myCursor = mydb.cursor()
        query = "SELECT first_name, last_name, auth_user.username FROM auth_user JOIN Admins ON Admins.Username = auth_user.username;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()                                                                             
            # Put query results into a list
            for d in myResults:
                adminNames.append(SponsorListItem(d[0], d[1], d[2], 0))
        except Exception as e:
            print("pulldownAdmins(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pulldownAdmins(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return adminNames

def pulldownSponsors():
    sponsorNames = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
	)

        # Look for all sponsors
        myCursor = mydb.cursor()
        query = "SELECT first_name, last_name, auth_user.username, PointsPerDollar FROM (auth_user JOIN Sponsors ON Sponsors.Username = auth_user.username) JOIN Employers ON Employers.ID = Sponsors.Employer_ID;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into a list
            for d in myResults:
                sponsorNames.append(SponsorListItem(d[0], d[1], d[2], d[3]))
        except Exception as e:
            print("pulldownSponsors(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pulldownSponsors(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return sponsorNames



