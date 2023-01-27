# finf The ArmStrong Number
def Find_Armstrong(n):
    a = map(int,str(n))
    b = map(lambda x:x**3,a)
    if sum(b) == n:
        return n,'ArmStrong Number'
    else:
        return n, 'Not Armstrong Number'
print(Find_Armstrong(371))


