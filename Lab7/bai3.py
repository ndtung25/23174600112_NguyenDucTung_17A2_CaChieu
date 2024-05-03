text = '''One day I was returning from the school. When I was about 1 Km away from my house, it started raining. 
I had no umbrella. I stood under a shed in front of a shop. Half an hour passed. Rain became heavier. Street was 
full of water now.  I could not stand like this forever. So I decided to go in rain. I drenched completely. Some 
children were playing with paper boats. I also joined them. I forgot everything. Suddenly I saw my mother was 
coming with an umbrella. She scolded me. But I was happy. I can’t forget that day.'''

words = text.split()
word_counts = {}

for word in words:
    word = word.strip(",.?!")

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

max_count = max(word_counts.values())
min_count = min(word_counts.values())

most_frequent_words = [word for word, count in word_counts.items() if count == max_count]
print("Từ có số lần xuất hiện nhiều nhất:")
for word in most_frequent_words:
    print(f"{word}: {max_count} lần")

least_frequent_words = [word for word, count in word_counts.items() if count == min_count]
print("\nTừ có số lần xuất hiện ít nhất:")
for word in least_frequent_words:
    print(f"{word}: {min_count} lần")
