
<h1 align="center"> Object Memory Address Token Generation  </h1>



## Executive Summary  
<br> 
The point of this software is to provide a flexible way of creating authentication while storing information. Any information that a user wants to be stored or recorded can be stored in an object. As an object is created, it is given a unique place in memory that is never the same (at least as long as the computer is turned on) (Linux and Unix, 2014  & Microsoft, 202).  An object can hold any data type: basic, or custom data types (WC, 2022). This means an object can store any information that you give it, and have an unique memory address associated with it in order to identify it. This creates a capability for a key pair value that can work well for any type of storage (SQL or NoSQL databases). 
<br>
<br>
Object-oriented programming (OOP) is extremely flexible, and the range of values that Random Access Memory (RAM) can provide is nearly endless, up to a 128-terabyte range depending on the OS (Codecademy, 2022  & Microsoft, 2021). Since there are a large amount of possibilities with these tools, the token generation is highly scalable. Thus, the objective is to harness the power of both high computational and modeable frameworks to provide token generators, key value pairs, and store data inside of objects that pairs well with any type of current database infrastructure.
<br> 
<br>
This is important when talking about finding ways of strengthening the security posture against attackers.
<br> 
<br>

## Overview

The program is a token generator which generates random memory addresses to associate to an object. Because the object can hold anything, objects, their data types, and the information they hold can be harnessed for authentication of any of the above. Because the key generator uses RAM for the addresses, it can be utilized a near-infinite number of times without the same key being generated twice.


## Program 
<br> 

### Create Memory Address Object Class 
<br> 

* Creates memory addresses 
* Classes hold values relevant to classes 
* Creates inheritance based memory address relation for objects authentication that requires 

### Memory Address Reader Class 

* Stores and reads memory address of classes 
* Encrypts and decrypts storage using In real time stateless multi-threading using coroutines. 
* Data will be salt, peppered, encrypted, and decrypted as necessary with stateless multi-threading using coroutines. 

### Authenticates Memory Address Read  

* Authenticates Memory Address Read 
<br>
<br>

### Possible Use Cases

* Identity Access Management of devices or applications within a large ecosystem. Each object memory address could serve as an application, or device within that ecosystem. 
* Passwordless sign on
* If needed for OS security, architecture verification that an object in memory (run process) has not been tampered with in memory.   
* Storing user groups identifying information in memory via objects and memory addresses.  


### Inheritance Based Memory Relation 

* From building this program, I have noticed that objects that have been inherited from the same grandparent class share a similar memory address and the ID in memory. 

* This has a couple of practical applications, but one primarily for security. Authentication for user groups, or anything that shares the similar data (subprocess of applications, object-based authentication to identify devices, etc).  


## Possible Expandition of Application 


### Memory Address Chaining  

* Since objects hold information, the implementation of object based authentication can expand.

* Objects can have literally any type of information: basic data types, custom data types, objects, structs, functions, etc. It creates a lot of functionality/creativity/flexibility. 

* For example, let's say I wanted to have an additional step of verification. Since an object can hold multiple values that make it you can leverage that to create a more unique memory address.  

* Every object has its own memory address and so do the values held within that object. If I wanted to create a unique memory address, I would simply cast the memory address until I get a string and string concatenation to form a unique value. The amount of possible value is only limited by the amount of memory address that the x32 and x64 architecture will hold (Microsoft, 2021). Thus, a complex, flexible, and scalable way of creating new tokens can be created by leveraging the functionality of RAM.  


### Key Chain of Objects  

* Virtual memory address space is greater the size of the internet (Fitzpatrick , 2013). That leads to a huge amount of scalability with a huge amount of possibilities for unique values that will not have the same address space as another object.  

* It does run RAM every time the service runs. A SQLite3 database that runs in memory will serve as a keychain. This will be a similar concept to how a keychain store works in macOS (Apple, 2022). 


### Improving Stability and Ensuring Stability of the Services 


* To ensure availability, the SQLite3 database will have a backup that runs in an encrypted swap. If the SQLite3 database gets corrupted, or the host computer randomly fails, the swap will still hold all of the data recorded.  

* Encrypted swap is common in some flavors of Linux, such as Arch Linux (Arch Linux , 2022).  

* On the run on startup, the program will decrypt and read associated objects, and then reassign new tokens (memory address) to each object (Linux and Unix StackExchange, 2014). 


### To Salt and Pepper or not Salt and Pepper, “To Season or not Season”

* Depending upon the use case, salt and peppering may not always be the best idea. If you salt and pepper, you lose the object's memory address. This removes any intended functionality for creating memory address chaining or using inheritance-based memory relation for authentication.  


## Attack Surface 

* Insecure coding practices 
* Buffer overflow/memory corruption 
* Database attacks against SQLite databases. 

## Improving Stability and Ensuring Stability of the Services 

### Protecting Attack Surface  

* Having the program sit within swap outside of the user space. This will provide the ability for it to be protected by “sudo”, or any other evaluated permissions. 

* When the program is running swap, memory space will be decrypted, but will be encrypted when the program is not. 
* Limiting access from other programs. (private, final, protected, static, let, tuples, proper inheritance, and no direct object reference, etc). 
* In real time the data will be salted, peppered, encrypted, and decrypted as necessary with stateless multi-threading using coroutines. 
* Input validation and query limiting 
* Language has a garbage collector, good type checking, etc. 
* The program will run “on demand”, but will need to be called with sudo permissions.  
* Secure Coding Practices  

## Example for practical application  

* Every object has a memory address and any object with reference to that parent object will share a very similar memory address. 
* The security token (object's memory address) will have a specific memory address. 
* For confidentiality, you can leverage the functionality of RAM to be one random and two unique per object.  
* For enhanced security, the volatility of RAM will make sure that it would be hard for an attacker to get a hold of a memory address (that serves as a security token). 
* For added security you can have the classes be private so that nothing can reference them. 
* Code can be obfuscated so that other programs cannot see what is happening inside the program.  
* Downsides of this are integrity and availability. If the computer goes down, so too does the RAM and therefore the authentication. 
* Challenges include making RAM more stable, or creating redundancy so that in case a service does go down, a new instance of the authenticator goes back up to ensure integrity and availability. 


## References  

Arch Linux (2022). dm-crypt/Swap encryption - ArchWiki. Wiki.      https://wiki.archlinux.org/title/Dm-crypt/Swap_encryption 

Linux and Unix, (2014). partition - Linux-swap on reboot - Unix & Linux Stack Exchange. Unix. https://unix.stackexchange.com/questions/104146/linux-swap-on-reboot 

Fitzpatrick , J. (2013). How Many Memory Addresses Can the RAM in My Computer Hold?. Howtogeek. https://www.howtogeek.com/163755/how-many-memory-addresses-can-the-ram-in-my-computer-hold/ 

Apple, (2022). What is Keychain Access on Mac? - Apple Support. Support. https://support.apple.com/guide/keychain-access/what-is-keychain-access-kyca1083/mac 

Microsoft,  (2021). Virtual address spaces. Microsoft, Docs. https://docs.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/virtual-address-spaces 


Codecademy, (2022 ). Why Object-Oriented Programming? | Codecademy. Codecademy. https://www.codecademy.com/article/cpp-object-oriented-programming 


West Chester University (WCU) , (2022). Objects, Classes, Instance Fields, and Methods – CSC142 - Computer Science II. Cs. https://www.cs.wcupa.edu/lngo/csc142/01-intro-to-classes-1/index.html
