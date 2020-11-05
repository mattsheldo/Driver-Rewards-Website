import mysql.connector

class CompanyProfile:
    def __init__(self, cid, name, pointRatio, code, query):
        self.cid = cid
        self.name = name
        self.pointRatio = pointRatio
        self.code = code
        self.query = query

def pullAllCompanies():
    companies = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all info for all employers
        myCursor = mydb.cursor()
        query = "SELECT ID, Name_, PointsPerDollar, Join_Code, API_Keyword FROM Employers WHERE ID > -1 ORDER BY Name_, ID;"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into the profile object and append to array
            for c in myResults:
                profileObj = CompanyProfile(c[0], c[1], c[2], c[3], c[4])
                companies.append(profileObj)
        except Exception as e:
            print("pullAllCompanies(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pullAllCompanies(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return companies

def pullCompanyProfile(sponsor):
    profileObj = CompanyProfile(0, "", 0.0, 0, "")

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all info for this employer
        myCursor = mydb.cursor()
        query = "SELECT ID, Name_, PointsPerDollar, Join_Code, API_Keyword FROM Employers JOIN Sponsors ON Employer_ID = ID WHERE Username = '" + sponsor + "';"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into the profile object
            for c in myResults:
                profileObj = CompanyProfile(c[0], c[1], c[2], c[3], c[4])
        except Exception as e:
            print("pullCompanyProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pullCompanyProfile(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return profileObj

def drPullCompanyProfile(emp):
    profileObj = CompanyProfile(0, "", 0.0, 0, "")

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all info for this employer
        myCursor = mydb.cursor()
        query = "SELECT ID, Name_, PointsPerDollar, Join_Code, API_Keyword FROM Employers WHERE ID = " + str(emp) + ";"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # Put query results into the profile object
            for c in myResults:
                profileObj = CompanyProfile(c[0], c[1], c[2], c[3], c[4])
        except Exception as e:
            print("drPullCompanyProfile(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("drPullCompanyProfile(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return profileObj

def getPoints(driver, empID):
    dPoints = 0

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Get the points the driver has with this employer
        myCursor = mydb.cursor()
        query = "SELECT Point_Total FROM Driver_Points WHERE Driver_User = '" + driver + "' AND Employer_ID = " + str(empID) + ";"
        try:
            # Execute query and get results
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for p in myResults:
                dPoints = p[0]
        except Exception as e:
            print("getPoints(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("getPoints(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return dPoints