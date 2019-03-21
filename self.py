class Yay:
    sen = 10
    def __init__(self):
        print("INIT")
        self.x = 10
        self.sen = self
    def bomb(self):
        return "Bomb"
    
    @bomb
    def bomb1(self):
        print("Bomb1")
    
    def wow(self, wo):
        print(wo.bomb())
    def ooo(oke):
        print(oke)
    #ooo(10)
    def diri(self):
        return self
    
    @diri
    def dut(x):
        return x.bomb()
    x = 10
    y = sen
    dut(y)
y = Yay()
print(y.dut())