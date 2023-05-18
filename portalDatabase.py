import mysql.connector
from mysql.connector import Error
from config import HOST, PORT, DATABASE, USER, PASSWORD


class Database():
    def __init__(self,
                 host=HOST,
                 port=PORT,
                 database=DATABASE,
                 user=USER,
                 password=PASSWORD):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)


    def getAllAccounts(self):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            query = "select * from accounts"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def getAllTransactions(self):
        ''' Complete the method to execute
                query to get all transactions'''
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            query = "select * from Transactions"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
        pass
       
    def deposit(self, accountID, amount):
        ''' Complete the method that calls store procedure
                    and return the results'''
        if self.connection.is_connected():
            self.cursor= self.connection.cursor()
            query = ("call deposit(accountID, amount) VALUES (%d, %f)")
            val = (accountID, amount)
            self.cursor.execute(query, val)
            self.connection.commit()
        pass
   

    def withdraw(self, accountID, amount):
        ''' Complete the method that calls store procedure
                    and return the results'''
        if self.connection.is_connected():
            self.cursor= self.connection.cursor()
            query = ("call withdraw(accountID, amount) VALUES (%d, %f)")
            val = (accountID, amount)
            self.cursor.execute(query, val)
            self.connection.commit()
        pass
        
    def addAccount(self, ownerName, owner_ssn, balance, status):
        ''' Complete the method to insert an
                    account to the accounts table'''
        if self.connection.is_connected():
            self.cursor= self.connection.cursor()
            query = ("insert into accounts (ownerName, owner_ssn, balance, account_status) VALUES (%s, %s, %s, %s)")
            val = (ownerName, owner_ssn, balance, status)
            self.cursor.execute(query, val)
            self.connection.commit()
        pass
  
    def accountTransactions(self, accountID):
        ''' Complete the method to call
                    procedure accountTransaction return results'''
        pass
  
    def deleteAccount(self, AccountID):
        ''' Complete the method to delete account
                and all transactions related to account'''
        if self.connection.is_connected():
            self.cursor= self.connection.cursor()
            query = ("delete * from accounts where AccountID=accounts.accountID VALUES (%d)")
            val = (AccountID)
            self.cursor.execute(query, val)
            self.connection.commit()
        pass
        
        
        
    
    
