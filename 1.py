sentence = input("sheikvane winadadeba:")
sentence = sentence.split(" ")
print(sentence)
word_count = {}

for word in sentence:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
print(word_count.keys())