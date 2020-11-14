class Store:

    def __init__(self):
        self.requests = [
        {'p_user': '9378421922', 
         'p_vendor': '8004849999',
         'message': 'give me the meats', 
         'accepted': 'False'},
        {'p_user': '9378421922', 
         'p_vendor': '8004849999',
         'message': 'I have big grass help me', 
         'accepted': 'True'},
        {'p_user': '9378421922', 
         'p_vendor': '8004849999',
         'message': 'Yeet a hampster for me', 
         'accepted': 'False'},
        {'p_user': '9378421922', 
         'p_vendor': '8004849999',
         'message': 'I need grocieriez run pop tarts are out', 
         'accepted': 'true'}
        ]

    ## Reviever Utilities ##

    def storeRequest(self, req):
        # Puts data into store
        print("Request %s stored" % req)

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

