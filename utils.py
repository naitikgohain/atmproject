from sqlconn import *

UID=None
def changepin(cpin,npin):
    
    if(checkuser(UID,cpin)):
       pinchange(UID,npin)
       return 1
    else:
       return 0

def setuid(u):
    global UID
    UID = u

def checkuser(u,p):
    if(check_user(u,p)!=0):
        return True
    else:
        return False


def getuser():
    return get_user(UID)


def authuser(u,p):
    if(checkuser(u,p)):
       setuid(u)
       return True
    else:
       return False
def getbalance():
    return show_balance(UID)[0]

def addbalance(amount):
    try:
        add_balance(UID,amount)
        return True
    except sqlite3.Error as er:
        return False

def removebalance(amount):
    b=getbalance()
    if(b>=amount):
        try:
            remove_balance(UID,amount)
            return True
        except sqlite3.Error as er:
            return False
    else:
        return False
    
        
    
    
#setpin(0)
"""print(UID)

setuid(0)
addbalance(2000)

if(removebalance(10000)):
    print("god")
else:
    print("not good")
print(show_balance(0)[0])
remove_balance(0,1000)"""

