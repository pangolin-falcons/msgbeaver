class Dispatcher:
    
    def __init__(self):
        store = Store()

    def claimRequest(self):
        requests = store.getPendingRequests()
        request = requests[0]
        store.removePendingRequest(0)

    def registerRequest(self, request):
        print("Registering claimed request")
