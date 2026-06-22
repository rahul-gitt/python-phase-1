# check the string is palindrome or not
def palindrome (strr):
    rev = ""
    for i in range(len(strr)-1,-1,-1):
        rev = rev+strr[i]

    if strr == rev:
        print(f"{strr} is a Palindrome.")
    else:
        print(f"{strr} is not a Paindrome.")

palindrome("madam")
palindrome("rahul")