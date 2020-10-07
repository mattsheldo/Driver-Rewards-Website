import mysql.connector

class Info:
    def __init__(self, fname, lname, pname, email, phone, address):
        self.fname = fname
        self.lname = lname
        self.pname = pname
        self.email = email
        self.phone = phone
        self.address = address

def getUserInfo(uname):

    driverNames = []
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
        )

    # Look for all driver under the current sponsor
    myCursor = mydb.cursor()
    
    query = "SELECT auth_user.first_name, auth_user.last_name, auth_user.preferred_name, auth_user.email, auth_user.phone, auth_user.address_ FROM auth_user WHERE auth_user.username = '" + uname + "';"
    
    # Execute query and get results
    myCursor.execute(query)
    myResults = myCursor.fetchall()

    infoList = []

    # Put query results into a list
    for i in myResults:
        infoList.append(Info(i[0], i[1], i[2], i[3], i[4], i[5]))
    
    myCursor.close()
    mydb.close()
    return infoList
                                                                                                                    
