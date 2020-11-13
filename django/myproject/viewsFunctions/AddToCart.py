import mysql.connector
import time
from datetime import datetime, timedelta

class CartItem:
    def __init__(self, pid, name, pointCost, dbid):
        self.pid = pid
        self.name = name
        self.pointCost = pointCost
        self.dbid = dbid

def setOrderPlacedAlert(driver):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Get the next available id
        myid = 0
        myCursor = mydb.cursor()
        query = "SELECT ID FROM Driver_Alerts ORDER BY ID DESC LIMIT 1;"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
                myid = i[0] + 1
        except Exception as e:
            print("setOrderPlacedAlert(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Tell the driver that their order was placed
        myCursor = mydb.cursor()
        query = "INSERT INTO Driver_Alerts VALUES (" + str(myid) + ", '" + driver + "', 'op', 'Your order has been placed');"
        try:
            # Execute query and get result
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("setOrderPlacedAlert(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("setOrderPlacedAlert(): Failed to connect: " + str(e))
    finally:
        mydb.close()

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

        # Make sure to protect against any apostraphes in the item name
        sqlItemName = itemName.replace("'", "''")

        # Insert item into the appropriate cart
        myCursor = mydb.cursor()
        query = "INSERT INTO Shopping_Cart_Items (ID, Username, Employer_ID, Point_Cost, Product_ID, Product_Name) VALUES (" + str(myID) + ", '" + driver + "', " + str(empID) + ", " + str(points) + ", " + str(itemID) + ", '" + sqlItemName + "');"
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

def pulldownCart(driver, empID):
    cartItems = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Find all items linked to this driver and employer
        myCursor = mydb.cursor()
        query = "SELECT Product_ID, Product_Name, Point_Cost, ID FROM Shopping_Cart_Items WHERE Username = '" + driver + "' AND Employer_ID = " + str(empID) + " ORDER BY Product_Name;"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for item in myResults:
                cartItems.append(CartItem(item[0], item[1], item[2], item[3]))
        except Exception as e:
            print("pulldownCart(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("pulldownCart(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return cartItems

def removeFromCart(itemID):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Delete the item with the appropriate ID
        myCursor = mydb.cursor()
        query = "DELETE FROM Shopping_Cart_Items WHERE ID = " + str(itemID) + ";"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("removeFromCart(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("removeFromCart(): Failed to connect: " + str(e))
    finally:
        mydb.close()

def driverCheckout(driver, empID, cartItems):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Get current driver's points
        drivPoints = 0
        myCursor = mydb.cursor()
        query = "SELECT Point_Total FROM Driver_Points WHERE Driver_User = '" + driver + "' AND Employer_ID = " + str(empID) + ";"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for r in myResults:
                drivPoints = r[0]
        except Exception as e:
            print("driverCheckout(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        myID = 0
        for i in cartItems:
            # Subtract the points
            drivPoints -= i.pointCost

            # Remove item from the cart
            myCursor = mydb.cursor()
            query = "DELETE FROM Shopping_Cart_Items WHERE Username = '" + driver + "' AND Employer_ID = " + str(empID) + " AND Product_ID = " + str(i.pid) + ";"
            try:
                myCursor.execute(query)
                mydb.commit()
            except Exception as e:
                print("driverCheckout(): Failed to update database: " + str(e))
            finally:
                myCursor.close()

            # Get next available id
            if myID == 0:
                myCursor = mydb.cursor()
                query = "SELECT ID FROM Purchase_History ORDER BY ID DESC LIMIT 1;"
                try:
                    myCursor.execute(query)
                    myResults = myCursor.fetchall()

                    for r in myResults:
                        myID = r[0] + 1
                except Exception as e:
                    print("driverCheckout(): Failed to query database: " + str(e))
                finally:
                    myCursor.close()
            # If it's not the first iteration, just increase the ID by 1
            else:
                myID += 1

            # Add item to purchase history with the current timestamp
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            # Make sure to protect against any apostraphes in the item name
            sqlItemName = i.name.replace("'", "''")

            myCursor = mydb.cursor()
            query = "INSERT INTO Purchase_History (ID, Username, Employer_ID, Date_, Point_Total, Product_Name, Product_ID) VALUES (" + str(myID) + ", '" + driver + "', " + str(empID) + ", '" + timestamp + "', " + str(i.pointCost) + ", '" + sqlItemName + "', " + str(i.pid) + ");"
            try:
                myCursor.execute(query)
                mydb.commit()
            except Exception as e:
                print("driverCheckout(): Failed to update database: " + str(e))
            finally:
                myCursor.close()

        # Update the driver's points
        myCursor = mydb.cursor()
        query = "UPDATE Driver_Points SET Point_Total = " + str(drivPoints) + " WHERE Driver_User = '" + driver + "' AND Employer_ID = " + str(empID) + ";"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("driverCheckout(): Failed to update database: " + str(e))
        finally:
            myCursor.close()

        # Alert the driver that the order was placed
        setOrderPlacedAlert(driver)
    except Exception as e:
        print("driverCheckout(): Failed to connect: " + str(e))
    finally:
        mydb.close()

def getOutstandingPurchases(driver):
    items = []

    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Look for all purchased items within the last 24 hours by the current driver
        cutoffTime = datetime.now() - timedelta(hours=24)
        timeStr = cutoffTime.strftime('%Y-%m-%d %H:%M:%S')

        myCursor = mydb.cursor()
        query = "SELECT Product_ID, Product_Name, Point_Total, ID FROM Purchase_History WHERE Username = '" + driver + "' AND Date_ > '" + timeStr + "';"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for item in myResults:
                items.append(CartItem(item[0], item[1], item[2], item[3]))
        except Exception as e:
            print("getOutstandingPurchases(): Failed to query database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("getOutstandingPurchases(): Failed to connect: " + str(e))
    finally:
        mydb.close()
        return items

def cancelPurchase(driver, itemID, itemCost):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Get the employer ID from purchase history
        empID = -1
        myCursor = mydb.cursor()
        query = "SELECT Employer_ID FROM Purchase_History WHERE ID = " + str(itemID) + ";"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for p in myResults:
                empID = p[0]
        except Exception as e:
            print("cancelPurchase(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Get the current driver's points first
        dPoints = 0
        myCursor = mydb.cursor()
        query = "SELECT Point_Total FROM Driver_Points WHERE Driver_User = '" + driver + "' AND Employer_ID = " + str(empID) + ";"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for p in myResults:
                dPoints = p[0]
        except Exception as e:
            print("cancelPurchase(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        dPoints += itemCost

        # Then give them their points back
        myCursor = mydb.cursor()
        query = "UPDATE Driver_Points SET Point_Total = " + str(dPoints) + " WHERE Driver_User = '" + driver + "' AND Employer_ID = " + str(empID) + ";"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("cancelPurchase(): Failed to update database: " + str(e))
        finally:
            myCursor.close()

        # Delete the item with the appropriate ID
        myCursor = mydb.cursor()
        query = "DELETE FROM Purchase_History WHERE ID = " + str(itemID) + ";"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("cancelPurchase(): Failed to update database: " + str(e))
        finally:
            myCursor.close()
    except Exception as e:
        print("cancelPurchase(): Failed to connect: " + str(e))
    finally:
        mydb.close()
