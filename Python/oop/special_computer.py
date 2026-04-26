
class computer:
    def __init__(self, cpu, ram, ssd):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    def config(self):
        print("CPU:", self.cpu, "RAM:", self.ram, "SSD:", self.ssd)

com1 = computer("i5", "16gb", "512gb")
com2 = computer("i7", "32gb", "1tb")

com1.config()
com2.config()
