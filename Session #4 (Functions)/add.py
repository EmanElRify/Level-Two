def add(*b):
    sum = 0
    for number in b:
        sum += number
    return sum

print(add(1,2,3,4,5,6,6))

def pi():
    return 22/7

x = pi()
print(x)