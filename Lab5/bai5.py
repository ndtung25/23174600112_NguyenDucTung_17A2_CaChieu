string1="Hello"
string2="World"
result=""
a,b = 0, 0
while a < len(string1) and b < len(string2):
    result += string1[a] + string2[b]
    a += 1
    b += 1
result += string1[a:] + string2[b:]
print("-".join(result))