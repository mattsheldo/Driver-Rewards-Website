import mysql.connector

# Open connection
try:
  mydb = mysql.connector.connect(
    host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
    user="admin",
    password="adminpass",
    database="DriverRewards"
  )
  
  myCursor = mydb.cursor()
  query = "INSERT INTO Drivers (Username, Employer_ID, Point_Total) VALUES ('admin', -1, 0);"
  # query = 'SELECT * FROM Employers;'
  # val = ('zachtest', -1, 0)
  
  try:
    # Execute query and get results
    myCursor.execute(query)
    # results = myCursor.fetchall()
    mydb.commit()

    # for i in results:
    #   print(i)

  except Exception as e:
    print("verifyAccount(): Failed to query: " + str(e))
  finally:
    myCursor.close()
    mydb.close()
except Exception as e:
  print("verifyAccount(): Failed to connect: " + str(e))
finally:
  mydb.close()