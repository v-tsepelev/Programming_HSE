# This program checks whether given natural number is prime or not.

x = int(input("Enter NATURAL number: "))
if x >= 4:
    d = 2
    ans = 1
    while d <= x/2:
        r = x%d
        if r == 0:
            print("Given number isn't prime and divisible at least by {0}".format(d))
            ans = 0
            break
        d += 1
    if ans!=0: print("Given number is prime. Congrats!")
elif x==1 or x==2 or x==3: print("The answer is obvious, you know")
else: print("Your input isn't a natural number!")

