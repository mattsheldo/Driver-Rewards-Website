import mysql.connector

class CompanyProfile:
    def __init__(self, name, pointRatio, code):
        self.name = name
        self.pointRatio = pointRatio
        self.code = code

def pullCompanyProfile(sponsor):
    profileObj = CompanyProfile("", 0.0, 0)

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
        query = "SELECT Name_, PointsPerDollar, Join_Code FROM Employers JOIN Sponsors ON Employer_ID = ID WHERE Username = '" + sponsor + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into the profile object
            for c in myResults:
                profileObj = CompanyProfile(c[0], c[1], c[2])
        except Exception as e:
            print("pullCompanyProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pullCompanyProfile(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return profileObj