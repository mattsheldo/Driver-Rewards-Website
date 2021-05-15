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

class Message:
    def __init__(self, message,msgid):
        self.message = message
        self.msgid = msgid


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
        query = "SELECT auth_user.first_name, auth_user.last_name, auth_user.preferred_name, auth_user.email, auth_user.phone, auth_user.address_, Driver_Points.Point_Total FROM Driver_Points JOIN auth_user ON Driver_Points.Driver_User = auth_user.username WHERE auth_user.username = '" + uname + "';"
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

def getUserAlerts(username, pc, oc, oi):
    messages = []
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()
    if pc == True:
        query1 = "SELECT Message_, ID FROM Driver_Alerts WHERE Username = '"+username+"' AND Type_ = 'pc'"
        myCursor.execute(query1)
        myResults = myCursor.fetchall()
        for i in myResults:
            messages.append(Message(i[0],i[1]))
    if oc == True:
        query2 = "SELECT Message_, ID FROM Driver_Alerts WHERE Username = '"+username+"' AND Type_ = 'op'"
        myCursor.execute(query2)
        myResults = myCursor.fetchall()
        for i in myResults:
            messages.append(Message(i[0],i[1]))
    if oi == True:
        query3 = "SELECT Message_, ID FROM Driver_Alerts WHERE Username = '"+username+"' AND Type_ = 'oi'"
        myCursor.execute(query3)
        myResults = myCursor.fetchall()
        for i in myResults:
            messages.append(Message(i[0],i[1]))

    # Always get the required alerts
    query4 = "SELECT Message_, ID FROM Driver_Alerts WHERE Username = '"+username+"' AND Type_ IN ('ac', 'rm');"
    myCursor.execute(query4)
    myResults = myCursor.fetchall()
    for i in myResults:
        messages.append(Message(i[0],i[1]))
    
    myCursor.close()
    mydb.close()

    return messages

def deleteUserMsg(msgToDel):
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
	user="admin",
	password="adminpass",
	database="DriverRewards"
    )
    myCursor = mydb.cursor()

    query = "DELETE FROM Driver_Alerts WHERE ID = "+str(msgToDel)+";"
    
    myCursor.execute(query)
    mydb.commit()
    myCursor.close()
    mydb.close()

def updateFilter(username, pc, oc, oi):
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )
    myCursor = mydb.cursor()
    query = "UPDATE Drivers set Points_Alert = "+str(pc)+", Order_Placed_Alert = "+str(oc)+", Order_Issue_Alert = "+str(oi)+" WHERE Username = '"+username+"';"

    myCursor.execute(query)
    mydb.commit()
    myCursor.close()
    mydb.close()




