def listEmployers():
    employers = []

    mydb = mysql.connector.connect(                                                                                             host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",                                                                                                           password="adminpass",                                                                                                   database="DriverRewards"
    )
    myCursor = mydb.cursor()
    query = "SELECT ID FROM Employers;"

    myCursor.execute(query)
    myResults = myCursor.fetchall()
    
    i = 0
    for ids in myResults:
        employerName.append(myResults[0][i])
        i += 1
    myCursor.close()
    mydb.close()
    return employers



def getAllDriversForEmployer(employerID):

    drivers = []

    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()
    query = "SELECT Driver_User FROM Driver_Points WHERE Employer_ID = "+employerID+";"

    myCursor.execute(query)
    myResults = myCursor.fetchalli()
    i = 0
    for names in myResults:
        drivers.append(myResults[0][i])
        i += 1
    myCursor.close()
    mydb.close()
    return drivers



def getEmployerName(employerID):

    employerName = ""

    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()
    query = "SELECT Name_ FROM Employers WHERE ID = "+employerID+";"

    myCursor.execute(query)
    myResults = myCursor.fetchall()
    employerName = myResults[0][0]
    myCursor.close()
    mydb.close()
    return employerName



def getDriverPurchaseHistory(employerID):

    driverHistory = []

    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()
    query = "SELECT * FROM Purchase_History WHERE Employer_ID = "+employerID+";"

    myCursor.execute(query)
    myResults = myCursor.fetchall()
    for info in myResults:
        driverHistory.append(info[0])
        driverHistory.append(info[1])
        driverHistory.append(info[2])
        driverHistory.append(info[3])
        driverHistory.append(info[4])
        driverHistory.append(info[5])
        driverHistory.append(info[6])
        driverHistory.append(info[7])
        driverHistory.append(info[8])
    myCursor.close()
    mydb.close()
    return driverHistory






