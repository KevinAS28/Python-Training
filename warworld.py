
class Warworld:
 roboot = [None, 'Panther', 'Python', 'Thunder', 'Assault', 'Leviathan']
 handgun = [[None, 'Yellow', 'Blacker', 'Blade1', 'Blade2'], [None, 'Singlegun', 'Triplegun', 'Xenon']]
 missile = [None, 'TwoShot', 'StormExtreme']
 mortar = [None, 'Bomber', 'Armageddon']
 speeder = [None, 'SideSpeed', 'ForwardSpeed', 'JumpSpeed'] 
 shield = ['Sideshield', 'OracleShield', 'PerfectShield1', 'PerfectShield2']

 spec = []
 count = 0
 def __init__(self, robot):
  self.robot = Warworld.roboot[robot]
  Warworld.spec.append(["Robot1 spec: "])
  Warworld.spec[Warworld.count].append("Model: %s " %(self.robot))
  
 def frontgun(self, type0, type1, gun0, gun1):
  lefthand = Warworld.handgun[type0][gun0]
  righthand = Warworld.handgun[type1][gun1]
  Warworld.spec[Warworld.count].append("Right Gun model: %s" %(righthand))
  Warworld.spec[Warworld.count].append("Left Gun model: %s" %(lefthand))
  

 def backequip(self, mis, mor, spe):
  misil = missile[mis]
  mortaar = mortar[mor]
  speder = speeder[spe]



oke = Warworld(1)
oke.frontgun(0, 1, 2, 3)
print(oke.spec[len(oke.spec) - 1])

