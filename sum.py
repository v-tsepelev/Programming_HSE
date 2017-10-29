# Print sum of numbers, given by user.
s = input()
if s == "":
    print(0)
else:
    inflow = [int(x) for x in s.split()]
    result = 0
    for i in inflow:
        result += i
    print(result)
