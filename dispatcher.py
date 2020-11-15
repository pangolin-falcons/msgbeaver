from dispatchees.send_sms import SendSMS
class Dispatcher:
    
    def __init__(self):
        # store = Store()
        return

    def claimRequest(self):
        # requests = store.getPendingRequests()
        # request = requests[0]
        # store.removePendingRequest(0)
        return

    def registerRequest(self, request):
        print("Registering claimed request")

    def processRequest(self, phoneNum, messageBody, vendors):
        uniqKeywords = list(set(messageBody.split(" ")))

        firstVendor = {}
        for keyword in uniqKeywords:
            #TODO: Search database for this
            for vendor in vendors:
                if vendor['keyword'] == keyword:
                    firstVendor = vendor

        print(firstVendor)
        sms = SendSMS()
        newMessageBody = "Hi " + firstVendor['name'] + ", new order for service from " + phoneNum + ". Please contact."
        status = sms.send(firstVendor['phone'], newMessageBody)
        print(status)
