import mysql.connector

def addUserInfo(userUser,prefName,phoneNum,address):
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )

    myCursor = mydb.cursor()
    query = "UPDATE auth_user SET phone = '"+phoneNum+"', address_ = '"+address+"', preferred_name = '"+prefName+"' WHERE username = '"+userUser+"';"

    myCursor.execute(query)
    mydb.commit()

    myCursor.close()
    mydb.close()


def addUserTypeInfo(userUser,userType):
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
        user="admin",
        password="adminpass",
        database="DriverRewards"
    )

    myCursor = mydb.cursor()

    if userType is 'Driver':
        query = "INSERT INTO Drivers (Username) VALUES ('"+userUser+"');"
        query2 = "INSERT INTO Driver_Points (Driver_User, Employer_ID, Point_Total) VALUES ('"+userUser+"',-1,0);"
        myCursor.execute(query)
        myCursor.execute(query2)
    elif userType is 'Sponsor':
        query = "INSERT INTO Sponsors (Username, Employer_ID) VALUES ('"+userUser+"',-1);"
        myCursor.execute(query)
    else:
        query = "INSERT INTO Admins (Username) VALUES ('"+userUser+"');"
        myCursor.execute(query)
    mydb.commit()
    myCursor.close()
    mydb.close()


