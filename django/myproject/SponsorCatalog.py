from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

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
