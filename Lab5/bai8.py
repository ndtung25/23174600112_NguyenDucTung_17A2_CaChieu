string=input("Nhập chuỗi:")
if len(string)<=10:
    print("Nhập lại chuỗi có độ dài >10")
else:
    string_a=string[1:8]
    print(string_a)
    string_b=string[4:9]
    print(string_b)
    string_c=string[-3:]
    print(string_c)
    string_d=string.lower()
    print(string_d)
    string_e=string.upper()
    print(string_e)
    string_f=string[::-1]
    print(string_f)