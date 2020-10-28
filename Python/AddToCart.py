import mysql.connector

def addToCart(driver, empID, points, itemID, itemName):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Find the next open ID in the cart table
        myID = -1
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Shopping_Cart_Items ORDER BY ID DESC LIMIT 1;"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            # If the table is empty, make id 0
            if len(myResults) == 0:
                myID = 0
            else:
                for i in myResults:
                    myID = i[0] + 1
        except Exception as e:
            print("addToCart(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Insert item into the appropriate cart
        myCursor = mydb.cursor()
        query = "INSERT INTO Shopping_Cart_Items (ID, Username, Employer_ID, Point_Cost, Product_ID, Product_Name) VALUES (" + str(myID) + ", '" + driver + "', " + str(empID) + ", " + str(points) + ", " + str(itemID) + ", '" + itemName + "');"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("addToCart(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("addToCart(): Failed to connect: " + str(e))
    finally:
        mydb.close()