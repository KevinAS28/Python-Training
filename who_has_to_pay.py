import random
import string
import sys
#pinjemnya berapa
#banyak orang juga
#semua harus terstruktur
spab = lambda x: [print(" ") for i in range(x)]
people_have_money_count = 2
people_need_money_count = 5
people = list(string.ascii_uppercase)
people_have_money = []
people_need_money = []
history = []
#people_need_money should not equal to people_have_money
for i in range(people_have_money_count):
    name = random.choice(people)
    if (not name in people_have_money):
        people_have_money.append((name, 1))
for i in range(people_need_money_count):
    name  = random.choice(people)
    if (not name in people_need_money):
        people_need_money.append((name, 0))
print("Peoples that need money: ")
for i in (people_need_money):
    print(i[0])
print("Peoples that have money: ")
for i in (people_have_money):
    print(i[0])
spab(5)
for i in range(len(people_need_money)):
    angka0 = random.randint(0, len(people_need_money)-1)
    angka1 = random.randint(0, len(people_have_money)-1)
    borrow = people_need_money[angka0]
    lend = people_have_money[angka1]
    if (lend[0] == borrow[0]):
        continue 
    print(lend[0], " Lending Money to ", borrow[0])
    history += (lend, borrow)
    people_have_money.append(people_need_money[angka0])
    #del people_need_money[angka0]
    del people_have_money[angka1]

class Node:
    def __init__(self, data=None, selanjutnya=None):
        self.data = data
        self.selanjutnya = selanjutnya
class Linked_List:
    head = None
    def __init__(self):
        pass
    def add(self, data):
        self.head = Node(data=data, selanjutnya=self.head)
    def the_last(self):
        return self.head.data
    def the_first(self):
        curr = self.head
        while (curr):
            if (curr.selanjutnya==None):
                break
            curr = curr.selanjutnya
        return curr.data

LS = Linked_List()
for i in range(len(history)):
    LS.add(history[i])
must_pay = LS.the_last()
must_recv = LS.the_first()
if must_pay[0] == must_recv[0]:
    print("No one must Pay")
    sys.exit(0)
print(must_pay[0], "Must Pay to ", must_recv[0])
