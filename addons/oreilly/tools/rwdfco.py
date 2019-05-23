import sys
import requests
import json
from bs4 import BeautifulSoup
from requests.auth import AuthBase



class FirstCallOnline:
    URL = 'https://rwd.firstcallonline.com/FirstCallOnline/' 
    URLin = URL + 'login.html'
    URLorders = URL + 'recent/ordersTab' 
    URLvehicles = URL + 'recent/vehiclesTab'
    URLquotes = URL + 'recent/quotesTab'
    
    def __init__(self):
        self.client = requests.Session()
        self.trusted = False
        self._csrf = self.get_csrf()
        print(self.authenticate())

    def get_secret(self):
        with open('/home/nick/.odentials', 'r') as sFile:
            return eval(sFile.read())

    def get_csrf(self):
        self.indexPage = self.client.get(self.URL+'index.html')
        soup = BeautifulSoup(self.indexPage.content, features="lxml")
        self._csrf = soup.find('input', dict(name='_csrf'))['value']
        
        if self._csrf:
            self.client.headers.update({'X-CSRF-TOKEN':self._csrf})
            self.client.headers.update({'X-Requested-With':'XMLHttpRequest'})
            self.client.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        else:
            print("No token...Sad")

        return self.client

    def authenticate(self):
        """ get authentication token """
        secret = self.get_secret()
        payload = {'loginName':secret['loginName'], 'password':secret['password'], '_rememberMe':'on',  '_csrf':self._csrf}
        self.authenticatedRequest = self.client.post(self.URLin, data=payload, headers=dict(Referer=self.URLin), cookies=self.indexPage.cookies)
        self.trusted = True
        return self.authenticatedRequest

    def makeRequest(self, reqType, url):
        return self.client.get(url, cookies=self.authenticatedRequest.cookies)
    
    def getData(self):
        """ Starting point to retreive data from FirstCallOnline """

        self.orders = self.makeRequest('orders', self.URLorders)
        self.vehicles = self.makeRequest('vehicles', self.URLvehicles)
        self.quotes = self.makeRequest('quotes', self.URLquotes)

        dictOrders = json.loads(self.orders.text) + json.loads(self.quotes.text)
        dictVehicles = json.loads(self.vehicles.text)

        def change_id_to_ident(oDataDict):
            """ jsonData with a field name 'id' gets changed to 'ident' """
            for i in oDataDict:
                i['my_ident'] = i['id']
                del i['id']
            return oDataDict

        return {
                'vehicles':change_id_to_ident(dictVehicles),
                'orders':change_id_to_ident(dictOrders)
                }
#
#client = FirstCallOnline()
#client.authenticate()
#print(client.getData())


