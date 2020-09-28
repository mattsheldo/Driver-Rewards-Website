import mysql.connector

# Open connection
try:
  mydb = mysql.connector.connect(
    host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
    user="admin",
    password="adminpass"
  )

  username = getstuff()
  acctype = getstuff()

  # Look for a username and password match
  myCursor = mydb.cursor()
  query = ""
  if acctype=='Driver':
    query = "INSERT INTO Drivers VALUES ('" + username + "', -1, 0)"
  elif acctype=='Sponsor':
    query = "INSERT INTO Sponsors VALUES ('" + username + "', -1)"
  elif acctype=='Admin':
    query = "INSERT INTO Admins VALUES ('" + username + "')"

  try:
    # Execute query and get results
    myCursor.execute(query)
    mydb.commit()

  except Exception:
    print("verifyAccount(): Failed to query")
  finally:
    myCursor.close()
    mydb.close()
    return
except Exception:
  print("verifyAccount(): Failed to connect")
finally:
  mydb.close()
  return