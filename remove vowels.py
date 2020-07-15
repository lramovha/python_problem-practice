def filterVowel():
    newstr = input("Enter string: \n")
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in newstr.lower():
        if i in vowels:
            newstr = newstr.replace(i, "")
    print("New string is :",newstr);

def filterConsonent():
    newstr = input("Enter a string: \n")
    vowels = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
              'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    for j in newstr.lower():
        if j in vowels:
            newstr = newstr.replace(j, "")
    print("New string is :",newstr);    

filterVowel()
filterConsonent()