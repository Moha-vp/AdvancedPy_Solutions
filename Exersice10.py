word = input("Type in a word: ").strip()


is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]: 
        is_palindrome = False
        break  
    
if is_palindrome:
    print("it's a palindrome.")
else:
    print("it's not a palindrome.")
