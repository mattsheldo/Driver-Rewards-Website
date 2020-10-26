from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

class CatalogItem:
    def __init__(self, itemID, name, price):
        self.itemID = itemID
        self.name = name
        self.price = price

def searchGeneralAPI(keyword):
    data = {}
    foundItems = []

    try:
        api = Finding(config_file='ebay.yaml')
        body = {
            'keywords': keyword,
            'itemFilter': [{
                'name': 'Condition',     # Only search for new items
                'value': 'New'
            }, {
                'name': 'Currency',     # Only deal with American dollars
                'value': 'USD'
            }]
        }
        response = api.execute('findItemsAdvanced', body)
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
        return foundItems
    
    data = response.dict()
    for item in data['searchResult']['item']:
        itemID = item['itemId']
        itemName = item['title']
        itemPrice = item['sellingStatus']['currentPrice']['value']
        foundItems.append(CatalogItem(itemID, itemName, itemPrice))

        if len(foundItems) >= 10:
            return foundItems
    
    return foundItems