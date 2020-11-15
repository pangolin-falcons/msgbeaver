from dispatchees.send_sms import SendSMS
from store import Store

class Dispatcher:
    
    def __init__(self, number, message):
        print('dispatcher init')
        store = Store()
        print('store for d made')
        v_id, vendor_name = store.isVendor(number)
        print('isvendor running')
        if v_id:
            print('issa vendor')
            vendorKeyword = self.isVendorKeyword(message) # Vendor sent the message
            if vendorKeyword:
                print('vendor keyword here')
                pendingOrderNumber = store.grabPending(v_id)
                if pendingOrderNumber:
                    if vendorKeyword == 'accept':
                        # store.acceptRequest(number) # Todo, this locks up the db
                        self.processAcceptance(number, pendingOrderNumber, v_id)
                        return
                    elif vendorKeyword == 'deny':
                        # recurse?
                        # store.rejectRequest(number, pendingOrder[0]['phoneNumber'], v_id)
                        # Todo, we need to decide what exactly to do when the vendor denies a job.
                        return
                    else:
                        print("Vendor's words made no sense")
                        return
                else:
                    print("there aren't any jobs pending for this guy")
                    return
            else:
                pass # Treat vendor like a customer if they acted dumb

        # Customer sent the message
        print('customer')
        #vendorNumber = store.grabAvailableVendor(message) # Todo, this doesn't grab correctly.
        # grabAvailableVendor should grab a vendor's phone number from Vendors that doesn't have an un-accepted order in Orders.
        # if True: #vendorNumber:
        #     print('vendor grabbed')
        #     store.generateOrder(vendorNumber[0], number) # Todo, Can't into INSERT
        #     print('order generated')
        #     self.processRequestForService(vendorNumber[0], number)
        #     return
        # else:
        #     print('No takers')
        #     return

    def isVendorKeyword(self, message):
        acceptKeywords = [ 'yes', 'Yes', 'YES' ]
        denyKeywords = [ 'no', 'No', 'NO' ]
        if message in acceptKeywords:
            return 'accept'
        elif message in denyKeywords:
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

    def processRequestForService(self, vendorNumber, number):
        # This is called when a customer asks for a service
        sms = SendSMS()
        messageBody = "New order for service from " + number + ". Please contact."
        status = sms.send(vendorNumber, messageBody)
        print(status)

    def processAcceptance(vendorNumber, number, vendorName):
        # This is called when a servicer takes a job
        sms = SendSMS()
        messageBody = "Your order has been accepted by " + vendorName + "."
        status = sms.send(number, messageBody)
        print(status)

    def processDenial(vendorNumber, number, vendorName):
        # This is called when a servicer denies a job
        return
