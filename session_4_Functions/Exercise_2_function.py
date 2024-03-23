# def add_numbers(a, b):
#    return a + b

# # Scenario 1: Function call
# result = add_numbers(3, 4)
# print(result)

# _______________________________


def multiply_numbers(x, y):
   return x * y

# Scenario 2: Function not called
print(multiply_numbers)


# # ________________________________

def greet(name, time):
   
   message = "Good "+ time + name + "!"
   return message

# Scenario 3: Function call with print

print(greet(name = " Abdelrahman", time = "morning"))
