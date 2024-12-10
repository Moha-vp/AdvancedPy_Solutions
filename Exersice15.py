
input_s = input("Please type in a string: ")

# Check for each vowel and print the appropriate message
for vowel in ['a', 'e', 'o']:
    if vowel in input_s:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
