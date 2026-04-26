
class computer:
    def __new__(cls):
        print("in constructor")
        return super(computer, cls).__new__(cls)

    def __init__(self):
        print("in init")

    def show(self):
        print("in show")


com1 = computer()
com1.show()