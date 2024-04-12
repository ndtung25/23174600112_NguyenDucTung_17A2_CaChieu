text=input("Nhập một chuỗi văn bản:").lower()
word_to_find=input("Nhập từ cần tìm kiếm:").lower()
word_index=text.find(word_to_find)
if word_index != -1:
    print(f"Từ '{word_to_find}' được tìm thấy ở vị trí: {word_index}")
else:
    print(f"Từ '{word_index}' không được tìm thấy.")

word_in_text=text.split()
word_count={}
most_common_word=None
max_count=0
for word in (word_in_text):
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
    if word_count[word]>max_count:
        most_common_word=word
        max_count=word_count[word]
if most_common_word:
    print(f"Từ '{most_common_word}' xuất hiện nhiều nhất trong chuỗi với số lần là: {max_count}")
else:
    print("Không có từ nào xuất hiện trong chuỗi.")