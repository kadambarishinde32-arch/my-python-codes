from account import account
class savingacc(account):
    def __init__(self, bankname, ifsc_code, a_no,acc_name,bal,fd):
        super().__init__(bankname, ifsc_code,acc_name, a_no)
        self.bal=bal
        self.fd=fd
        print(bal)

    def __init__(self, name, bases, dict, /, **kwds):
        super().__init__(name, bases, dict, **kwds)