class Store:

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

    def removePendingRequest(self, index):
        # Removes request data at index
        print("Purging registered request data")
        return
