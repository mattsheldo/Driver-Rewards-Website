import mysql.connector

def verifyAccount(userUser, userPass):
  # Open connection
  try:
    mydb = mysql.connector.connect(
      host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
      user="admin",
      password="adminpass"
    )

    # Look for a username and password match
    myCursor = mydb.cursor()
    query = "SELECT * FROM Accounts WHERE Username = '" + userUser + "' AND Encrypted_Password = '" + userPass + "' AND Approved = True;"

    try:
      # Execute query and get results
      myCursor.execute(query)
      myResults = myCursor.fetchall()

      # If a result is found, then there's a match and the account is verified
      if len(myResults) > 0:
        return True
      else:
        return False
    except Exception:
      print("verifyAccount(): Failed to query")
    finally:
      myCursor.close()
      mydb.close()
      return False
  except Exception:
    print("verifyAccount(): Failed to connect")
  finally:
    mydb.close()
    return False
  