import requests, urllib, base64



def getAuthToken():
     AppSettings = {
          'client_id':'DevonGil-CPSC4910-SBX-05007f986-bf3d55ed',
          'client_secret':'SBX-5007f9869d09-62ab-46f3-a149-e2d2',
          'ruName': 'Devon_Gilliard-DevonGil-CPSC49-dhfvu'
          }

     authHeaderData = AppSettings['client_id'] + ':' + AppSettings['client_secret']
     encodedAuthHeader = base64.b64encode(str.encode(authHeaderData))
     strHeader = str(encodedAuthHeader)
     headers= {
          'Content-Type' : 'application/x-www-form-urlencoded',
          'Authorization' : 'Basic ' + strHeader
          }
     print(headers)
    #app_scopes = ["https://api.ebay.com/oauth/api_scope", "https://api.ebay.com/oauth/api_scope/buy.item.feed"]

     body= {
          "grant_type" : "client_credentials",
          "redirect_uri" : AppSettings['ruName'],
          "scope" : "https://api.ebay.com/oauth/api_scope"
      }

     data = urllib.parse.urlencode(body)
     print(data)

     tokenURL = "https://api.sandbox.ebay.com/identity/v1/oauth2/token"

     response = requests.post(tokenURL, headers=headers, data=data)


     return response.json()

# def getCode():
#
# GET https://auth.sandbox.ebay.com/oauth2/authorize?
#     client_id=DevonGil-CPSC4910-SBX-05007f986-bf3d55ed&
#     redirect_uri=Devon_Gilliard-DevonGil-CPSC49-dhfvu&
#     response_type=code&
#     scope=https%3A%2F%2Fapi.ebay.com%2&   # a URL-encoded string of space-separated scopes
#     prompt=login

response = getAuthToken()
print(response)
response['access_token'] #access keys as required
response['error_description'] #if errors



# r = requests.get("https://api.ebay.com/sell/fulfillment/v1/order?limit=10",
#                          headers={"Authorization": "{}".format(response['access_token']),
#                                   "Content-Type": "application/json",
#                                   "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
#                                   "Accept": "application/json"
#                                   })
