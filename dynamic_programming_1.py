
# coding: utf-8

# In[16]:


n = int(input())
data = []
for i in range(n):
    data.append(input().split(" "))
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

time = [data[0][0]]
if n > 1:
    time.append(min([data[0][0] + data[1][0], data[0][1]]))
if n > 2:
    time.append( min([data[0][2], data[1][1] + data[2][0], data[0][0] + data[1][0] + data[2][0]]))
if n > 3:
    for pos in range(3, n):
        time.append(min(time[pos - 3] + data[pos - 2][2], time[pos - 2] + data[pos - 1][1], time[pos - 1] + data[pos][0]))

print(data)
print(time)
print(time[n - 1])

