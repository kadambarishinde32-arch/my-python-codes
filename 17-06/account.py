from bank import bank
class account(bank):
    def __init__(self, bankname, ifsc_code,a_no,acc_name):
        super().__init__(bankname, ifsc_code)
        self.a_no=a_no
        self.acc_name=acc_name
        