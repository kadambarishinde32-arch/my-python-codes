from A import A
class C(A):
    def pqr(self):
        print("from pqr c")

    def __init__(self):
        print("from c")
        super().__init__()