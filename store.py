class Store:

    def __init__(self):
        self.requests = [
        {'p_user': '9378421922', 
         'p_vendor': '8004849999',
         'time': '2000-01-01T00:00:00',
         'message': 'give me the meats', 
         'accepted': 'False'},
        {'p_user': '9378421922', 
         'p_vendor': '8004849999',
         'time': '2000-01-01T00:00:00',
         'message': 'I have big grass help me', 
         'accepted': 'True'},
        {'p_user': '9378421922', 
         'p_vendor': '8004849999',
         'time': '2000-01-01T00:00:00',
         'message': 'Yeet a hampster for me', 
         'accepted': 'False'},
        {'p_user': '9378421922', 
         'p_vendor': '8004849999',
         'time': '2000-01-01T00:00:00',
         'message': 'I need grocieriez run pop tarts are out', 
         'accepted': 'true'}
        ]
        self.users = [
        {'phone': '9378421922',
         'name': 'spencer',
         'type': 'user',
         'address': '4203 Falcon Rd\n Pangolin, OH'},
        {'phone': '8004849999',
         'name': 'fake vendor',
         'type': 'vendor',
         'address': 'Ham Street'},
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

    def requestReply(self, vendor_number, accept):
        # Get vendor orders where accepted = false
            # To accept mark the order as accepted2
        # To reject remove vendor number from order
        print("Reqest to vendor %s accepted" % vendor_number)

    ## Dispatcher Utilities ##

    def getPendingRequests(self):
        # Returns request data where p_vendor is empty
        print("Returning request data")
        return [{'phone': '9378421922', 
                 'message': 'give me the meats', 
                 'address': '4203 Falcon Rd\n Pangolin, OH'}]

    def removePendingRequest(self, index):
        # Removes request data at index
        print("Purging registered request data")
        return
