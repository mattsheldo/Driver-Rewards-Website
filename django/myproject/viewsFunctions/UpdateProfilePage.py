import mysql.connector

def updateUserInfo(userUser,fname,lname,prefName,email,phoneNum,address):
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",                                                      user="admin",                                                                                                           password="adminpass",
        database="DriverRewards"
    )
    
    myCursor = mydb.cursor()
    
    query = "UPDATE auth_user SET first_name = '"+fname+"', last_name = '"+lname+"', email = '"+email+"', phone = '"+phoneNum+"', address_ = '"+address+"', preferred_name = '"+prefName+"' WHERE username = '"+userUser+"';"

    myCursor.execute(query)
    mydb.commit()

    myCursor.close()
    mydb.close() 
