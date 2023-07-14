word = input("Put your word")
revword = word[::-1]
if word == revword:
    print('This word is palindrom')
else:
    print("This word is not polindrom")
print(revword)