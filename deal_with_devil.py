
# coding: utf-8

# In[55]:


s = input()
unique = ''.join(set(s))
nominals = []
for j in unique:
    nominals.append(j)
multiplicities = []
for c in nominals:
    multiplicities.append(s.count(c))
for j in range(len(nominals)):
    nominals[j] = int(nominals[j])

pizdets = []
k = 0
for j in range(10):
    if j in nominals:
        pizdets.append([int(j),int(multiplicities[nominals.index(j)])])
        k += 1
    else:
        pizdets.append([int(j),int(0)])
pizdets.sort(key=lambda x: x[0])

j = len(pizdets)-1
while j != 0:
    pizdets[j-1][1] += pizdets[j][0]*pizdets[j][1]
    j -= 1
    
days_to_death = 0
for x in pizdets:
    days_to_death += x[1]
    
print(days_to_death)


# In[17]:


L = [(1,"juca"),(22,"james"),(53,"xuxa"),(44,"delicia")]
[i for i, v in enumerate(L) if v[0] == 22][0]
res_list = [x[0] for x in L]
print(res_list)


# In[28]:


s = input()
unique = ''.join(set(s))
nominals = []
for j in unique:
    nominals.append(j)
multiplicities = []
for c in nominals:
    multiplicities.append(s.count(c))
for j in range(len(nominals)):
    nominals[j] = int(nominals[j])

print(multiplicities)
print(nominals)

for y in nominals:
    print(type(y))
    
pizdets = []
for j in range(10):
    if j in nominals:
        print("success")


# In[37]:


nominals = [6,5]
nominals.index(5)

