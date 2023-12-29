numbers = []
i = 1
while (len(numbers) < 5):
    numbers.append(i)
    i += 1
for n in numbers:
    if n % 2 == 0:
        print(n)
