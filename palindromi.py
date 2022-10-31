def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


while True:
    word = input("Enter a word: ")
    if word == "":
        print("Έγινε εισαγωγή κενης συμβολοσειράς, το πρόγραμμα τερματίζει...")
        break
    elif palindrome(word):
        print("παλίνδρομη")
    else:
        print("όχι παλίνδρομη")
