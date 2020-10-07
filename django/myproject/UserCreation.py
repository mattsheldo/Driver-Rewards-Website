import mysql.connector

def addUserInfo(userUser,prefName,phoneNum,address):
  # Open connection
  try:
    mydb = mysql.connector.connect(
      host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
      user="admin",
      password="adminpass",
      database="DriverRewards"
    )

    # Look for a username and password match
    myCursor = mydb.cursor()
    query = "UPDATE auth_user SET phone = '3213214321', address_ = 'stert', preferred_name = 'nsme' WHERE username = 'newtest2';"
#    val = (phoneNum,address,prefName,username)

    try:
      # Execute query and get results
      myCursor.execute(query)
      mydb.commit()
    except Exception:
        print("verifyAccount(): Failed to query")
    finally:
      myCursor.close()
      mydb.close()
  except Exception:
    print("verifyAccount(): Failed to connect")
  finally:
    mydb.close()  
