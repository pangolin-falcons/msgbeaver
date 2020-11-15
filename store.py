import sqlite3 as sql
from dispatcher import Dispatcher

class Store:

    def __init__(self):
        self.db_name = "data.sqlite"

    ## Reviever Utilities ##

    def storeRequest(self, phoneNum, messageBody):
        conn = sql.connect(self.db_name)
        conn.execute('''
            INSERT INTO Orders (c_id, request)
                VALUES (
                    (SELECT c.c_id FROM Customers c WHERE c.phoneNumber = ?), 
                    ?
                );''', (phoneNum, messageBody))
        conn.commit()
        conn.close()

    def acceptRequest(self, vendor_phone):
        # Get vendor orders where accepted = false
            # To accept mark the order as accepted2
        conn = sql.connect(self.db_name)
        conn.execute('''
            UPDATE order o
                SET o.is_accepted = 1
                WHERE o.is_accepted = 0 AND
                    o.v_id = (select v_id from Vendors WHERE phoneNumber = ?)
        ''', (vendor_phone))

    def rejectRequest(self, vendor_number):
        # Remove vendor number from order
        for r in self.requests:
            if(r['accepted'] == False and r['p_vendor'] == vendor_phone):
                r['p_vendor'] = None
        print("Reqest to vendor %s accepted" % vendor_number)

    def markCompletedRequest(self, vendor_phone): 
        return

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

