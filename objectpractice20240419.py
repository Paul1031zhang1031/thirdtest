accountName=''
accountBalance=0
accountPassword=""

def newAccount(name,balance,password):
    global accountName,accountBalance,accountPassword
    accountName=name
    accountBalance=balance
    accountPassword=password
    return accountName+" "+ str(accountBalance)  

def show():
    global accountName,accountBalance,accountPassword
    print("Name:",accountName)
    print("Balance:",accountBalance)
    print("Password:",accountPassword)

def getbalance(password):
    global accountName,accountBalance,accountPassword
    if password!= accountPassword:
        print("incorrect password")
        return  None
    else:
        return accountBalance

    
def deposit(accountToDeposit,password):
    global accountName,accountBalance,accountPassword
    if password!= accountPassword:
        print("incorrect password")
        return  None
    if accountToDeposit < 0:
        print("you can not deposit a  negative amount")
        return None
    else:
        accountBalance = accountToDeposit+accountBalance
        return accountBalance

def withdraw(amountToWithdraw,password):
    if  password!= accountPassword:
        print("incorrect password")
        return  None
    if  amountToWithdraw < 0:
        print("you can not withdraw a  negative amount")
        return None
    if  accountBalance < amountToWithdraw:
        return None

    accountBalance = accountBalance - amountToWithdraw
    return accountBalance

newAccount("Jessy",10000,'c999')

while True:
    #print()
    #print("press b to get a balance")
    #print("press d to get a deposit")
    #print("press w to get a withdraw")
    #print("press s to show the account information")
    #print("press q to quit")
    #print()

    action = input('what do you want to do?')
    action = action.lower()
    action = action[0]
    print(action)

    if action == 'b':
       print("get Balance:") 
       usePassword = input("please enter the password: ")
       balance=getbalance(usePassword)
       if balance is not None:
          print("your balance is:" ,balance)
    elif action == "d":
       print("deposit:")
       userdepositamount =input("please enter amount to deposit:")
       userdepositamount=int(userdepositamount)
       usePassword = input("please enter the password:")
       newbalance=deposit(userdepositamount,usePassword)
       if newbalance is not None:
           print("the new balance is:",newbalance)
    elif action == "s":
         userinformation=newAccount("Jessy",10000,'c999')
         print("tell me details acount",)
         print(userinformation)

       



    








