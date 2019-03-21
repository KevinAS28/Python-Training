import re
def bilbul(x):
    if float != type(x):
        return False
    y = str(x).replace(".", ",")
    y = int(y[0:((re.search(",", y).start()))])
    if x <= (y + 0.5):
        return y
    else:
        return y + 1
    
spab = lambda x: [print(' ') for i in range(x)]

