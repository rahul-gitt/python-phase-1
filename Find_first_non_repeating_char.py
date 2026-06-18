word = input("Enter your word : ")
for ch in word :
    if(word.count(ch)==1):
        print("The first non repeating char is : ",ch)
        break
    else:
        print("Every letter are repeated.")
        break