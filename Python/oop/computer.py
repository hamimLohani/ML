
class computer:

    def __init__(self):
        print("in init")
        self.cpu = "i5"

    def configure(self):
        print("i7, 16GB, 1TB")


com1 = computer()
com2 = computer()

com1.configure()
  
print(com1.cpu)
print(com2.cpu)