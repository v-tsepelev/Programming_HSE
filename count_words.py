text = []
s = input()
answer = []
string = ''
while s != "END":
    text.append(s)
    s = input()
for x in text:
    k = 0
    for i in x:
        if i == 't':
            k = k + 1
    if k == 3:
        answer.append(x[0])
for j in range(len(answer)):
    string += answer[j]
print(string)
