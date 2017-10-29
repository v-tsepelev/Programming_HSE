# Recursive solution of unbounded (integer) knapsack problem.

data = list(map(int, input().split(" ")))
vol = data[0]
            
def knapsack_recursive(n):
    if n == 1:
        return data[1]
    else:
        list=[]
        for i in range(1, n):
            list.append(knapsack_recursive(n-i)+data[i])
        list.append(data[n])
        return max(list)
    
print(knapsack_recursive(vol))
