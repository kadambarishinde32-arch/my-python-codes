from B import B
from C1 import C
class D(B,C):
    def mno(self):
        print("from mno D")

    def __init__(self):
        print("from D")
        super().__init__()

obje=D()