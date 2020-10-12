import mysql.connector

class Info:
    def __init__(self, fname, lname, pname, email, phone, address, points):
        self.fname = fname
        self.lname = lname
        self.pname = pname
        self.email = email
        self.phone = phone
        self.address = address
        self.points = points

class InfoButLess:
    def __init__(self, fname2, lname2, pname2, email2, phone2, address2):
        self.fname2 = fname2
        self.lname2 = lname2
        self.pname2 = pname2
        self.email2 = email2
        self.phone2 = phone2
        self.address2 = address2    

def getUserInfo(uname, uType):

    driverNames = []
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
        )

    # Look for all driver under the current sponsor
    myCursor = mydb.cursor()
    
    if uType == "d":
        query = "SELECT auth_user.first_name, auth_user.last_name, auth_user.preferred_name, auth_user.email, auth_user.phone, auth_user.address_, Drivers.Point_Total FROM Drivers JOIN auth_user ON Drivers.Username = auth_user.username WHERE auth_user.username = '" + uname + "';"
    elif uType == "s":
         query = "SELECT auth_user.first_name, auth_user.last_name, auth_user.preferred_name, auth_user.email, auth_user.phone, auth_user.address_ FROM Sponsors JOIN auth_user ON Sponsors.Username = auth_user.username WHERE auth_user.username = '" + uname + "';"
    else:
         query = "SELECT auth_user.first_name, auth_user.last_name, auth_user.preferred_name, auth_user.email, auth_user.phone, auth_user.address_ FROM Admins JOIN auth_user ON Admins.Username = auth_user.username WHERE auth_user.username = '" + uname + "';"

    # Execute query and get results
    myCursor.execute(query)
    myResults = myCursor.fetchall()

    infoList = []

    # Put query results into a list
    if uType == "d":
        for i in myResults:
            infoList.append(Info(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
    else:
        for i in myResults:
            infoList.append(InfoButLess(i[0], i[1], i[2], i[3], i[4], i[5]))

    myCursor.close()
    mydb.close()
    return infoList

                                                                                                                    
