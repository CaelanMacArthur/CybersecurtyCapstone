#from cProfile import run
import os 
import asyncio
import time
from CreateMemoryAddress import CacheDatabase

try: 
    def main():

        database = CacheDatabase()

        #Encase of a decryption error. 
        try: 
            #Try to decryption. 
            database.strDecryptAndRead('/private/var/vm/tempSQLite3/filekey.key',1)
            database.strDecryptAndRead('/private/var/vm/tempSQLite3/filekey.key',2)

        # Failed 
        except:
            #Try to Encrypt and then decrypt. Will secure when everything is done running
            database.strEncrypt('/private/var/vm/tempSQLite3/filekey.key',1)
            database.strDecryptAndRead('/private/var/vm/tempSQLite3/filekey.key',1)
            database.strEncrypt('/private/var/vm/tempSQLite3/filekey.key',2)
            database.strDecryptAndRead('/private/var/vm/tempSQLite3/filekey.key',2)

        database.saltPepperStoreSqlLite()
        database.query()
        # Securing :Memory:
        database.strEncrypt('/private/var/vm/tempSQLite3/filekey.key',1)
        # Securing Backup Database
        database.strEncrypt('/private/var/vm/tempSQLite3/filekey.key',2)

    if __name__ == "__main__":
        main()

except: 
    print("You do not have the right permission.")


