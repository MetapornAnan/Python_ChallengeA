def count_words(sentence):
    words = sentence.split()
 
    word_count = {}
    duplicate_words = []
   
    for word in words:
        if word in word_count:
            word_count[word] += 1
            if word not in duplicate_words:
                duplicate_words.append(word)  
        else:
            word_count[word] = 1
 
    print(f"มีคำทั้งหมด {len(words)} คำ")
    for word in duplicate_words:
        print(f"คำว่า '{word}' ปรากฏ {word_count[word]} ครั้ง")
 
    return len(duplicate_words), duplicate_words
 
print("--------------------------------------")
user_sentence = input("ป้อนข้อความ: ")
print("--------------------------------------")
duplicate_count, duplicate_words = count_words(user_sentence)
print(f"มีคำซ้ำกันทั้งหมด {duplicate_count} คำ คำคือ {', '.join(duplicate_words)}")
print("--------------------------------------")