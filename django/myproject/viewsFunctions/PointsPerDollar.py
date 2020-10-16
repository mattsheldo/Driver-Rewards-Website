import mysql.connector

def UpdatePVal(sponsorID, DollarValue):
    mydb = mysql.connector.connect(host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin", password="adminpass", database="DriverRewards")
    myCursor = mydb.cursor()
    query = "UPDATE Employers SET PointsPerDollar = "+DollarValue+" WHERE ID = "+str(sponsorID)+";"
    myCursor.execute(query)
    mydb.commit()

    myCursor.close()
    mydb.close()
                                                                   
def getID(userName):
    mydb = mysql.connector.connect(host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )

    myCursor = mydb.cursor()
    query = "SELECT Employer_ID FROM Sponsors WHERE Username = '"+userName+"';"
    myCursor.execute(query)
    myResults = myCursor.fetchall()

    myCursor.close()
    mydb.close()
    return myResults [0][0]
