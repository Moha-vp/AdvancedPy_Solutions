word = input(" give a Word please: ")
spaces = (30 - len(word)) // 2

print('*' * 30)

print('*' + ' ' * spaces + word + ' ' * (30 - len(word) - spaces - 1) + '*')

print('*' * 30)
