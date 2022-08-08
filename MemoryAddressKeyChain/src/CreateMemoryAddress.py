import asyncio
import sqlite3
import random
import hashlib
import hmac
import os
import re 
import json
from cryptography.fernet import Fernet
import shutil


#Inheritance based memory relation 
#Grandparent class
class SimilarAddressExample:
    # Add any functionality needed here 
    pass 
     

#Parent class
class SimilarExampleTwo(SimilarAddressExample):
    # Add any functionality needed here 
    pass 
      
# Child class
class SimilarExampleThree(SimilarExampleTwo):
     # Add any functionality needed here 
     pass 

simone = SimilarAddressExample()
simetwo = SimilarExampleTwo()
simThree = SimilarExampleThree()
print(simone)
print(simetwo)
print(simThree)

# Basic Examples of a Memory Space 
#Class One
class Example:
    # Add any functionality needed here 
    pass 

#Parent class
class ExampleTwo:
    # Add any functionality needed here 
    pass 
      
# Child class
class ExampleThree:
     # Add any functionality needed here 
    pass 

ex = Example()
ex2  = ExampleTwo()
ex3 = ExampleThree()
print(ex)
print(ex2)
print(ex3)


# Memory Address Chain

class ChainObjExample:
    i = "example"
    num = 2 
class ChainObjExampleTwo:
    i2 = "exampletwo"
    num2 = 3 

class ProtectAddress():
            
    def holdClass(self, example, exampleTwo, exampleThree):

        example = example
        exampleTwo = exampleTwo
        exampleThree = exampleThree
        classData = (example, exampleTwo, exampleThree)
       
        return classData

    def inheritanceHoldClass(self,interExample, interExampleTwo, interExampleThree):

        interExample = interExample
        interExampleTwo = interExampleTwo
        interExampleThree = interExampleThree
        inheritanceClassData = (interExample, interExampleTwo, interExampleThree)

        return inheritanceClassData
    
    def chainingHoldClass(self,chainingExample):

        chainingExample = chainingExample

        chainingClassData = (chainingExample)

        return chainingClassData

# To make sure that values do not get released in memory. 
class CreateStaticValues():
    protectAddress = ProtectAddress()
    
    #Basic Classes
    example = Example()
    exampleTwo = ExampleTwo()
    exampleThree = ExampleThree()

    # Inheritance based memory relation classes 
    interExampleObj = SimilarAddressExample()
    interExampleTwoObj  = SimilarExampleTwo()
    interExampleThreeObj  = SimilarExampleThree()

    # Object Chaining 
    # First Object  
    chainExample = ChainObjExample() 
    getHexObj = hex(id(chainExample))
    chainOne = hex(id(chainExample.i))
    chainTwo =  hex(id(chainExample.num))
    # Second Object 
    chainExampleTwo = ChainObjExampleTwo() 
    getHexObj2 = hex(id(chainExampleTwo))
    chainOneObj2 = hex(id(chainExampleTwo.i2))
    chainTwoObj2 =  hex(id(chainExampleTwo.num2))
    chain =  getHexObj + chainOne +  chainTwo +  getHexObj2 + chainOneObj2  + chainTwoObj2

    protectFunctionCall = protectAddress.holdClass(example, exampleTwo, exampleThree)
    inheritanceFunctionCall = protectAddress.inheritanceHoldClass(interExampleObj, interExampleTwoObj, interExampleThreeObj)
    chainingFunctionCall = protectAddress.chainingHoldClass(chain)
    print(chainingFunctionCall)


#New Instance of CreateStaticValues for classes to reference 
createStaticValues = CreateStaticValues()
referenceAddresses = createStaticValues.protectFunctionCall
  
class CacheDatabase():

    createStaticValues = CreateStaticValues()
    referenceAddresses = createStaticValues.protectFunctionCall 
    inheritanceAddresses = createStaticValues.inheritanceFunctionCall
    chainAddresss = createStaticValues.chainingFunctionCall

    """
    If num is equal to 1 it will encrypt :memory: from sqlite 

    If num is equal to 2 it will encrypt the back up  from sqlite 
    """
    def strEncrypt(self,tempKey, num):

        if num == 1:
            # opening the key
            with open(tempKey, 'rb') as filekey:
                key = filekey.read()
            # using the generated key
            fernet = Fernet(key)
    
            # opening the original file to encrypt
            with open('/private/var/vm/tempSQLite3/:memory:', 'rb') as file:
                original = file.read()
                
            # encrypting the file
            encrypted = fernet.encrypt(original)

            # opening the file in write mode and
            # writing the encrypted data
            with open('/private/var/vm/tempSQLite3/:memory:', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

        if num == 2: 
             # opening the key
            with open(tempKey, 'rb') as filekey:
                key = filekey.read()
            # using the generated key
            fernet = Fernet(key)
    
            # opening the original file to encrypt
            with open('/private/var/vm/tempSQLite3/test.db', 'rb') as file:
                original = file.read()
                
            # encrypting the file
            encrypted = fernet.encrypt(original)

            # opening the file in write mode and
            # writing the encrypted data
            with open('/private/var/vm/tempSQLite3/test.db', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
    
        """
        If num is equal to 1 it will decrypt :memory: from sqlite 

        If num is equal to 2 it will decrypt the back up from sqlite 
        """
    def strDecryptAndRead(self,tempKey, num):

        if num == 1:
            pass
            # opening the key
            with open(tempKey, 'rb') as filekey:
                key = filekey.read()
            # using the key
            fernet = Fernet(key)

            # opening the encrypted file
            with open('/private/var/vm/tempSQLite3/:memory:', 'rb') as enc_file:
                encrypted = enc_file.read()
            
            # decrypting the file
            decrypted = fernet.decrypt(encrypted)
            
            # opening the file in write mode and
            # writing the decrypted data
            with open('/private/var/vm/tempSQLite3/:memory:', 'wb') as dec_file:
                dec_file.write(decrypted)
         

        if num == 2:
            # opening the key
            with open(tempKey, 'rb') as filekey:
                key = filekey.read()
            # using the key
            fernet = Fernet(key)

            # opening the encrypted file
            with open('/private/var/vm/tempSQLite3/test.db', 'rb') as enc_file:
                encrypted = enc_file.read()
            
            # decrypting the file
            decrypted = fernet.decrypt(encrypted)
            
            # opening the file in write mode and
            # writing the decrypted data
            with open('/private/var/vm/tempSQLite3/test.db', 'wb') as dec_file:
                dec_file.write(decrypted)

    def saltPepperStoreSqlLite(self):

        postionIterate = 0    

        con = sqlite3.connect("/private/var/vm/tempSQLite3/:memory:")
        con1 = sqlite3.connect("/private/var/vm/tempSQLite3/test.db")
        # Memory Connection
        cur = con.cursor()
        cur.execute("create table IF NOT EXISTS storeMemAddress (MemoryAddress TEXT)")
        con.commit()
        # Backup Connection
        cur1 = con1.cursor()
        cur1.execute("create table IF NOT EXISTS storeMemAddress (MemoryAddress TEXT)")
        con1.commit()

        
        for i in referenceAddresses:

    
            # Creating a list of reference addresss  and casting to string 
            cast  = str(referenceAddresses[postionIterate])
      
            alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            chars = []
            
            for t in range(16):
                chars.append(random.choice(alphabet))

            # Salt and Peppering Memory Address 
            pepperString = cast.join(chars)
            pepperedMemAddress = hmac.new(pepperString.encode("utf-8"), pepperString.encode("utf-8"), hashlib.sha256).hexdigest()
            salt = os.urandom(32)
            saltPepperMemAddress = pepperedMemAddress.encode()
            memAddressDigest = hashlib.pbkdf2_hmac('sha256', saltPepperMemAddress, salt, 10000)
            # Convert to hex for Storage 
            hexMemAddressDigest  = memAddressDigest.hex()

        # Creating variables before loop 
        inheritanceAddresses = createStaticValues.inheritanceFunctionCall
        for i in inheritanceAddresses:

            # Creating a list of inheritance ddresseses and casting to String  
            castInheritanceAddresses = str(inheritanceAddresses[postionIterate])

            alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            chars = []
            
            for t in range(16):
                chars.append(random.choice(alphabet))

            # Salt and Peppering Memory Address 
            pepperStringInherit = castInheritanceAddresses.join(chars)
            pepperedInheritanceAddresses = hmac.new(pepperStringInherit.encode("utf-8"), pepperStringInherit.encode("utf-8"), hashlib.sha256).hexdigest()
            saltInherit = os.urandom(32)
            saltPepperInheritanceAddresses = pepperedInheritanceAddresses.encode()
            inheritanceAddressesDigest = hashlib.pbkdf2_hmac('sha256', saltPepperInheritanceAddresses, saltInherit, 10000)
            # Convert to hex for Storage 
            hexInheritanceAddressesDigest  = inheritanceAddressesDigest.hex()

        # Creating variables before loop 
        chainAddresss = createStaticValues.chainingFunctionCall
        for i in chainAddresss:

            # Creating a list of inheritance ddresseses and casting to String  
            castingChainAddresss= str(chainAddresss[postionIterate])

            alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            chars = []
            
            for t in range(16):
                chars.append(random.choice(alphabet))

            # Salt and Peppering Memory Address 
            pepperStringChaining = castingChainAddresss.join(chars)
            pepperedChaining= hmac.new(pepperStringChaining.encode("utf-8"), pepperStringChaining.encode("utf-8"), hashlib.sha256).hexdigest()
            saltChaining = os.urandom(32)
            saltPepperChaining = pepperedChaining.encode()
            chainingAddressesDigest = hashlib.pbkdf2_hmac('sha256', saltPepperChaining, saltChaining, 10000)
            # Convert to hex for Storage 
            hexChainingAddressesDigest = chainingAddressesDigest.hex()

         # add to postion to move to the next value in tuple
            postionIterate += 1 
        
        #Adjust for unbound variables 
        class StatichexMemAddressDigest:
                hexMemAddress = hexMemAddressDigest
                hexInheritanceAddresses = hexInheritanceAddressesDigest                

        statichexMemAddressDigest  = StatichexMemAddressDigest()
        address = statichexMemAddressDigest.hexMemAddress
        inheritanceAddresses = statichexMemAddressDigest.hexInheritanceAddresses

        # Storing in Memory 
        cur.execute("insert into storeMemAddress values (?)", (address,))
        cur.execute("insert into storeMemAddress values (?)", (inheritanceAddresses,))

        con.commit()
        # Closing database 
        con.close()

        # Storing in backup database
        cur1.execute("insert into storeMemAddress values (?)", (address,))
        cur1.execute("insert into storeMemAddress values (?)", (inheritanceAddresses,))
        con1.commit()
        # Closing database 
        con1.close()

    def query(self):

      
        con = sqlite3.connect("/private/var/vm/tempSQLite3/:memory:")
        con1 = sqlite3.connect("/private/var/vm/tempSQLite3/test.db")

        # check space memory
        cur = con.cursor()
        cur.execute("SELECT * FROM storeMemAddress")
        print("\n")
        print(cur.fetchall())
        print("\n")
        con.close()

        # check backup memory
        cur1 = con1.cursor()
        cur1.execute("SELECT * FROM storeMemAddress")
        print("\n")
        print(cur1.fetchall())
        print("\n")
        con1.close()
        
