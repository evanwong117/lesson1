word=input("Please enter the word: ")
character=input("Please enter the character: ")
count=0
for i in word:
    if character==i:
        count=count+1
print(count)
    