he_so_goc_1=float(input("Nhập hệ số góc của đường thẳng thứ nhất: "))
he_so_tu_do_1=float(input("Nhập hệ số tự do của đường thẳng thứ nhất: "))
he_so_goc_2=float(input("Nhập hệ số góc của đường thẳng thứ hai: "))
he_so_tu_do_2=float(input("Nhập hệ số tự do của đường thẳng thứ hai: "))
print("Vị trí tương đối của hai đường thẳng: ")
if he_so_goc_1 == he_so_goc_2:
  if he_so_tu_do_1 == he_so_tu_do_2:
    print("Hai đường thẳng trùng nhau")
  else:
    print("Hai đường thẳng song song")
else:
  print("Hai đường thẳng cắt nhau")