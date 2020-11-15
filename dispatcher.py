from dispatchees.send_sms import SendSMS
from store import Store

class Dispatcher:
    
    def __init__(self, number, message):
        print('dispatcher init')
        store = Store()
        print('store for d made')
        vid = store.isVendor(number)
        print('isvendor running')
        if vid:
            print('issa vendor')
            vendorKeyword = self.isVendorKeyword(message) # Vendor sent the message
            if vendorKeyword:
                if store.grabPending(vid):
                    if vendorKeyword == 'accept':
                        store.acceptRequest(number)
                        return
                    elif vendorKeyword == 'deny':
                        store.rejectRequest(number)
                        return
                    else:
                        return
                else:
                    return
            else:
                pass # Treat vendor like a customer if they acted dumb

        # Customer sent the message
        print('customer')
        vendorNumber = store.grabAvailableVendor(message)
        if vendorNumber:
            print('vendor grabbed')
            # flag vendor laziness to 1 and send message to vendor
            return
        else:
            print('No takers')
            return

    def isVendorKeyword(message):
        acceptKeywords = [ 'yes', 'Yes', 'YES' ]
        denyKeywords = [ 'no', 'No', 'NO' ]
        if message == acceptKeywords:
            return 'accept'
        elif message == denyKeywords:
            return 'deny'
        else:
            return None

    def claimRequest(self):
        # requests = store.getPendingRequests()
        # request = requests[0]
        # store.removePendingRequest(0)
        return

    def registerRequest(self, request):
        print("Registering claimed request")

    def processRequest(self, phoneNum, messageBody, vendors):
 
        sms = SendSMS()
        newMessageBody = "Hi " + firstVendor['name'] + ", new order for service from " + phoneNum + ". Please contact."
        status = sms.send(firstVendor['phone'], newMessageBody)
        print(status)

    def queryPending(self):
        while True:
            time.sleep(1)
            store.acceptRequest(self)
