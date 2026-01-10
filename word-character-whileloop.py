word=input("Please enter the word: ")
character=input("Please enter the character: ")
index=0
count=0

while index<len(word): 
    print ("the letter now is ", word[index])
    if word[index]==character:
        count=count+1
    index +=1

print("Number of character ", character, " is ", count)
     