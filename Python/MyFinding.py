'''
Clone the repo from https://github.com/timotheus/ebaysdk-python
Edit ebay.yaml to add the App ID
Create a script like this one to make a call to the production servers
'''

from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

try:
    api = Finding(config_file='ebay.yaml')
    response = api.execute('findItemsAdvanced', {'keywords': 'NY Giants'})
    data = response.dict()
    print(data)
    '''
    data {
        'ack': 'Success',
        'version': '1.13.0',
        'timestamp': '2020-10-21-T19:53:59.357Z,
        'searchResult': {
            'item': [{
                'itemId': '283574788723',
                'title': 'New York NY Giants LED Light Lamp Collectible Eli Manning Home Decor Gift',
                'gloablId': 'EBAY-US',
                'primaryCategory': {
                    'categoryId': '206',
                    'categoryName': 'Football-NFL'
                },
                'galleryURL': 'https://thumbs4.ebaystatic.com/m/mb1wCBseaZ1QIuk8tfug9Og/140.jpg',
                'viewItemURL': 'https://www.ebay.com/itm/New-York-NY-Giants-LED-Light-Lamp-Collectible-Eli-Manning-Home-Decor-Gift-/283574788723',
                'autoPay': 'true',
                'postalCode': '891**',
                'location': 'Las Vegas,NV,USA',
                'country': 'US',
                'shippingInfo': {
                    'shippingServiceCost': {
                        '_currencyId': 'USD',
                        'value': '0.0'
                    },
                    'shippingType': 'Free',
                    'shipToLocations': 'Worldwide',
                    'expeditedShipping': 'true',
                    'oneDayShippingAvailable': 'false',
                    'handlingTime': '1',
                },
                'sellingStatus': {
                    'currentPrice': {
                        '_currencyId': 'USD',
                        'value': '23.89'
                    },
                    'convertedCurrentPrice': {
                        '_currencyId': 'USD',
                        'value': '23.89'
                    },
                    'sellingState': 'Active',
                    'timeLeft': 'P18DT3H24M31S'
                },
                'listingInfo': {
                    'bestOfferEnabled': 'false',
                    'buyItNowAvailable': 'false',
                    'startTime': '2019-08-08T23:18:30.000Z',
                    'endTime': '2020-11-08T23:18:30.000Z',
                    'listingType': 'StoreInventory',
                    'gift': 'false',
                    'watchCount': '67'
                },
                'returnsAccepted': 'true',
                'condition': {
                    'conditionId': '1000',
                    'conditionDisplayName': 'New'
                },
                'isMultiVariationListing': 'false',
                'topRatedListing': 'true'
            }, {
            ...
            },
            ...
            ]
        }
    }
    '''
except ConnectionError as e:
    print(e)
    print(e.response.dict())