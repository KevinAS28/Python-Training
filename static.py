class oke:
 def __init__(self, oke, eko):
  self.oke = oke
  self.eko = eko
 def kali(self):
  return self.oke + self.eko
 @classmethod
 def baru(cls, satu, dua):
  return cls(satu, dua)
 @staticmethod
 def lama(masa, sih):
  print(masa * sih)

ooo = oke.baru(5, 6)
print(ooo.kali())
oke.lama(10, 6)
