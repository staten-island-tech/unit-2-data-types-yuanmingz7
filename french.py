""" def french(t, T):
    if T or t < 10:
 """

""" x = "t" or "T"
values = input("enter a sentence: ")
print(values)
for x in values:
    print(x)
count = len(values)
print(count)
y= values.split( )
z = y[0]
print(y)
print(z) """

""" sentence = input("input a sentence: ")
words = sentence.split()
letters= words.split( )
z = letters[0]
print(letters)
count = len(words)
letter_count = len(letters)
print(count)
print(letter_count) """


some_text = "the quick brown fox jumped over the lazy dog"
more_text = ["T", "h", "e"]

def lang(text):
    french = 0
    english = 0
    for letter in text:
        if letter == "s" or letter == "S":
            french = french +1
        #elif letter in ["t", "T"]
        elif letter.lower() == "t":
            english = english +1
            if french >= english: 
                print("French")