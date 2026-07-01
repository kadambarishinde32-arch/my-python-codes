class B:
    def abc(self):
        print("from abc A")

    def __init__(self):
        print("from B")
        super().__init__()