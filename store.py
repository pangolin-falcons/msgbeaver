import sqlite3 as sql

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
            UPDATE Orders o
                SET o.is_accepted = 1
                WHERE o.is_accepted = 0 AND
                    o.v_id = (select v_id from Vendors WHERE phoneNumber = ?);
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

    def getVendor(self, number):
        # returns the primary key of a vendor if given number is a vendor number
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT v_id, name FROM Vendors
            WHERE phoneNumber = ?;
            ''', (number,))
        return cursor.fetchone()

    def grabPending(self, v_id):
        # returns the order that's pending for a given vendor phone number
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT o_id FROM Orders
            WHERE v_id = ? AND
                is_accepted = 0;
            ''', (v_id,))
        return cursor.fetchone()

    def getOrderInfo(self, o_id):
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Vendors.name, Vendors.phoneNumber, Customers.name, Customers.phoneNumber FROM Orders, Vendors, Customers
            WHERE o_id = ? AND
            Orders.v_id=Vendors.v_id AND
            Orders.c_id=Customers.c_id;
            ''', (o_id,))
        return cursor.fetchone()

    def getVendorsFromKeywords(self, keywords):
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        vendorKeywords = ['carpenter','handyman','plumber']

        for key in keywords:
            if key is vendorKeywords:
                cursor.execute('''
                    SELECT v_id FROM Vendors
                        WHERE keyword = ?
                    );
            ''', (key,))
        return cursor.fetchall()

    def generateOrder(self, vendorNumber, clientNumber):
        # Appends to the Order table
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Orders (phoneNumber, request)
            VALUES (?, ?);
        ''', ((vendorNumber,), clientNumber))
