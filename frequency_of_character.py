#Count the frequency of the each character
word = input("Enter your word : ")
printed = ""
for ch in word:
    if ch not in printed:
        print(ch,"=", word.count(ch))
        printed+= ch
