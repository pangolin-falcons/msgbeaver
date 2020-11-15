from dispatcher import Dispatcher
class Store:

    def __init__(self):
        self.requests = [
        {'p_user': '9378421922', 
         'p_vendor': None,
         'time': '2000-01-01T00:00:00',
         'message': 'give me the meats', 
         'accepted': False},
        {'p_user': '9378421922', 
         'p_vendor': '8004849999',
         'time': '2000-01-01T00:00:00',
         'message': 'I have big grass help me', 
         'accepted': 'True'},
        {'p_user': '9378421922', 
         'p_vendor': '8004849999',
         'time': '2000-01-01T00:00:00',
         'message': 'Yeet a hampster for me', 
         'accepted': False},
        {'p_user': '9378421922', 
         'p_vendor': None,
         'time': '2000-01-01T00:00:00',
         'message': 'I need grocieriez run pop tarts are out', 
         'accepted': False}
        ]
        self.users = [
        {'phone': '+19378421922',
         'name': 'spencer',
         'type': 'vendor',
         'address': '4203 Falcon Rd\n Pangolin, OH',
         'keyword': 'carpenter'
         },
        {'phone': '+17176494887',
         'name': 'fake vendor',
         'type': 'vendor',
         'address': 'Ham Street',
         'keyword': 'locksmith'
         },
        ]

    ## Reviever Utilities ##

    def storeRequest(self, phoneNum, messageBody, timestamp):
        new_request = dict([
            ('p_user', phoneNum),
            ('p_vendor', -1),
            ('time', timestamp),
            ('message', messageBody),
            ('accepted', False)])
        # Puts data into store
        self.requests.append(new_request)
        print("Request %s stored" % messageBody)
        dispatch = Dispatcher()
        print("passed to dispatch")
        dispatch.processRequest(phoneNum, messageBody, self.users)



    def acceptRequest(self, vendor_phone):
        # Get vendor orders where accepted = false
            # To accept mark the order as accepted2
        for r in self.requests:
            if(r['accepted'] == False and r['p_vendor'] == vendor_phone):
                r['accepted'] = True
        print("Reqest to vendor %s accepted" % vendor_phone)

    def rejectRequest(self, vendor_number):
        # Remove vendor number from order
        for r in self.requests:
            if(r['accepted'] == False and r['p_vendor'] == vendor_phone):
                r['p_vendor'] = None
        print("Reqest to vendor %s accepted" % vendor_number)

    ## Dispatcher Utilities ##

    def getPendingRequests(self):
        # Returns request data where p_vendor is empty
        pendingRequests = []
        for r in self.requests:
            if(r['p_vendor'] is None and not r['accepted']):
                pendingRequests.append(r)
        print("Returning request data")
        return pendingRequests

    def removePendingRequest(self, index):
        # TODO Consider removing this, I don't think we need it
        # Removes request data at index
        print("Purging registered request data")
        return
