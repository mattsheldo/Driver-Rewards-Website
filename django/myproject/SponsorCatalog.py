from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
import mysql.connector

class CatalogItem:
    def __init__(self, itemID, name, price, shipping, points, itemURL):
        self.itemID = itemID
        self.name = name
        self.price = price
        self.shipping = shipping
        self.points = points
        self.itemURL = itemURL

def searchGeneralAPI(keyword):
    data = {}
    foundItems = []

    try:
        api = Finding(config_file='/home/ubuntu/django/myproject/ebay.yaml')
        body = {
            'keywords': keyword,
            'itemFilter': [{
                'name': 'Condition',     # Only search for new items
                'value': 'New'
            }, {
                'name': 'Currency',     # Only deal with American dollars
                'value': 'USD'
            }, {
                'name': 'ListingType',     # Don't deal with any auctions
                'value': 'FixedPrice'
            }]
        }
        response = api.execute('findItemsAdvanced', body)
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
        return foundItems
    
    data = response.dict()
    if 'searchResult' not in data.keys() or not data['searchResult']:
        return foundItems
    for item in data['searchResult']['item']:
        itemID = item['itemId']
        itemName = item['title']
        itemPrice = item['sellingStatus']['currentPrice']['value']
        if 'shippingServiceCost' in item['shippingInfo'].keys() and item['shippingInfo']['shippingServiceCost']:
            itemShipping = item['shippingInfo']['shippingServiceCost']['value']
        else:
            itemShipping = 0.0
        itemURL = item['viewItemURL']
        foundItems.append(CatalogItem(int(itemID), itemName, float(itemPrice), float(itemShipping), 0.0, itemURL))

        if len(foundItems) >= 10:
            return foundItems
    
    return foundItems

def updateCatalog(sponsor, newQuery):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Get the employer to update the query for
        empID = -1
        myCursor = mydb.cursor()
        query = "SELECT Employer_ID FROM Sponsors WHERE Username = '" + sponsor + "';"
        try:
            myCursor.execute(query)
            myResults = myCursor.fetchall()

            for i in myResults:
                empID = i[0]
        except Exception as e:
            print("updateCatalog(): Failed to query database: " + str(e))
        finally:
            myCursor.close()

        # Update the query string for that employer
        myCursor = mydb.cursor()
        query = "UPDATE Employers SET API_Keyword = '" + newQuery + "' WHERE ID = " + str(empID) + ";"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("updateCatalog(): Failed to update database: " + str(e))
    except Exception as e:
        print("updateCatalog(): Failed to connect: " + str(e))
    finally:
        mydb.close()

def adminUpdateCatalog(empID, newQuery):
    # Open connection
    try:
        mydb = mysql.connector.connect(
            host="cpsc4910group1rds.cwlgcbjw7kmo.us-east-1.rds.amazonaws.com",
            user="admin",
            password="adminpass",
            database="DriverRewards"
        )

        # Update the query string for that employer
        myCursor = mydb.cursor()
        query = "UPDATE Employers SET API_Keyword = '" + newQuery + "' WHERE ID = " + str(empID) + ";"
        try:
            myCursor.execute(query)
            mydb.commit()
        except Exception as e:
            print("adminUpdateCatalog(): Failed to update database: " + str(e))
    except Exception as e:
        print("adminUpdateCatalog(): Failed to connect: " + str(e))
    finally:
        mydb.close()
