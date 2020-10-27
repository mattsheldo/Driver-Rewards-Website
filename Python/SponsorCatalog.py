from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

class CatalogItem:
    def __init__(self, itemID, name, price, shipping, points):
        self.itemID = itemID
        self.name = name
        self.price = price
        self.shipping = shipping
        self.points = points

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
    if not 'searchResult' in data.keys():
        return foundItems
    for item in data['searchResult']['item']:
        itemID = item['itemId']
        itemName = item['title']
        itemPrice = item['sellingStatus']['currentPrice']['value']
        itemShipping = item['shippingInfo']['shippingServiceCost']['value']
        foundItems.append(CatalogItem(int(itemID), itemName, float(itemPrice), float(itemShipping), 0.0))

        if len(foundItems) >= 10:
            return foundItems
    
    return foundItems