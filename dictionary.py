s = input().split(", ")
s_lower_case = [x.lower() for x in s]
min_word = sorted(s_lower_case)[0]
origin = s[s_lower_case.index(min_word)]
print(origin)
