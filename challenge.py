#Using the "input" method in Python, ask a user to input a sentence. Then develop a function that accepts a the user input and will tell you how many words are in that string. 

sentence = input("input a sentence:")
words = sentence.split()
print(words)
count = len(words)
print(count)
