import os 
from cryptography.fernet import Fernet
#os.system("rm /private/var/vm/tempSQLite3/backup.db")
os.system("rm /private/var/vm/tempSQLite3/temp.txt")

"""
os.system("rm /private/var/vm/tempSQLite3/test.db")
os.system("rm /private/var/vm/tempSQLite3/test.db:memory:")
os.system("rm /private/var/vm/tempSQLite3/:memory:")
#os.system("touch /private/var/vm/tempSQLite3/temp.txt")
os.system("touch /private/var/vm/tempSQLite3/test.db")

#os.system('rm /private/var/vm/tempSQLite3/filekey.key')
"""
"""
# key generation
key = Fernet.generate_key()
# string the key in a file
with open('/private/var/vm/tempSQLite3/filekey.key', 'wb') as filekey:
   filekey.write(key)
"""