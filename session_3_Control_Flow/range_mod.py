# What is the expected output for the following piece of code
#ما هو الخرج المتوقع من الكود الاتي 
for i in range(2, 10, 2):
   print(i)
   
# Write a piece of code that stars from a certain point to the
# end of it, and identify in a print statement if a number is even or odd
# اكتب كود يبدأ من نقطة وينتهي عند نقطة ويطبع اذا كان الاعداد بين النقطتين زوجية ام فرديا 
start = 2
end = 10
for i in range (start,end,2):
    if i % 2 == 0:
        print(f"{i} is even number")
    else :
        print(f"{i} is odd number")
