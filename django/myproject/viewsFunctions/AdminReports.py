import mysql.connector

class DriverHistory:
    def __init__(self, ID, username, employerID, datePurchased, PointTotal, ProductName, SponsorID, AdminID, ProductID, companyName):
        self.ID = ID
        self.username = username
        self.employerID = employerID
        self.datePurchased = datePurchased
        self.PointTotal = PointTotal
        self.ProductName = ProductName
        self.SponsorID = SponsorID
        self.AdminID = AdminID
        self.ProductID = ProductID
        self.companyName = companyName

class employerInfo:
    def __init__(self,ID,name):
        self.ID = ID
        self.name = name

def listEmployers():
    employers = []

    mydb = mysql.connector.connect(                                                                                             host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",                                                                                                           password="adminpass",                                                                                                   database="DriverRewards"
    )
    myCursor = mydb.cursor()
    query = "SELECT ID, Name_ FROM Employers;"

    myCursor.execute(query)
    myResults = myCursor.fetchall()
    
    for ids in myResults:
        employers.append(employerInfo(ids[0],ids[1]))
    myCursor.close()
    mydb.close()
    return employers



def getDriverPurchaseHistory(employerID):

    driverHistory = []

    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()
    query = "SELECT * FROM Purchase_History WHERE Employer_ID = "+str(employerID)+";"

    myCursor.execute(query)
    myResults = myCursor.fetchall()
    employers = []
    employers = listEmployers()
    for info in myResults:
        for emps in employers:
            if info[2] == emps.ID:
                if info[6]:
                    driverHistory.append(DriverHistory(info[0],info[1],info[2],info[3],info[4],info[5],info[6],"",info[8], emps.name))
                elif info[7]:
                    driverHistory.append(DriverHistory(info[0],info[1],info[2],info[3],info[4],info[5],"",info[7],info[8], emps.name))
                else:
                    driverHistory.append(DriverHistory(info[0],info[1],info[2],info[3],info[4],info[5],"","",info[8], emps.name))
    myCursor.close()
    mydb.close()
    return driverHistory






