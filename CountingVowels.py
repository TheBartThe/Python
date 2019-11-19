vowels = 0
word = input("Enter a word: ")
word = word.lower()
for i in word:
    if(i in "aeiou"):
        vowels += 1
print(vowels, " vowels in word")
