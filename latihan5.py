class coba:
    def __init__(self, x):
        print("from init")
    def __new__(self, x):
        print("from new")
def coba1(massa, kecepatan) -> "Joules":
    return massa+kecepatan

def main():
    print(coba1.__annotations__)
    print(coba1(100, 200))
    print(coba1.__name__)
    oke = coba(10)

main()
    
    