import mysql.connector

def updateBillInfo(sponsorID,endDate,total,paid):
    mydb = mysql.connector.connect(
        host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",                                                      user="admin",                                                                                                           password="adminpass",
        database="DriverRewards"
    )
    
    myCursor = mydb.cursor()
    
    query = "UPDATE Invoices SET Month_End_Date = '"+endDate+"', Total = '"+str(total)+"', Paid = '"+paid+"' WHERE Employer_ID = '"+sponsorID+"';"

    myCursor.execute(query)
    mydb.commit()

    myCursor.close()
    mydb.close() 
