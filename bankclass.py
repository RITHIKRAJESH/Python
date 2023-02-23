class bankac:
    def custdet(self,cname,acno,actype,bal):
        self.cname=cname
        self.acno=acno
        self.actype=actype
        self.bal=bal
    def deposit(self,amt):
        self.bal=self.bal+amt
    def withdraw(self,amt):
        if self.bal<amt:
            return false
        else:
            self.bal=self.bal-amt
    def display(self):
        print("customer name:",self.cname)
        print("account number:",self.acno)
        print("account type:",self.actype)
        print("balance ammount:",self.bal)
obj=bankac()
obj.deposit
obj.withdraw
ch=0
while(ch!=5):
    print("1.Store Customer Details")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Show customer details")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        cname=input("enter the name:")
        acno=int(input("enter account number:"))
        actype=input("Enter account type:")
        bal=int(input("Enter balance:"))
        obj.custdet(cname,acno,actype,bal)
    elif ch==2:
        amt=int(input("enter the deposit amount:"))
        obj.deposit(amt)
    elif ch==3:
        amt=int(input("enter the withdrawal amount:"))
        obj.withdraw(amt)
    elif ch==4:
        obj.display()
    else:
        print("Invalid choice")
