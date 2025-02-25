#Using the "input" method in Python, ask a user to input a sentence. Then develop a function that accepts a the user input and will tell you how many words are in that string. 

""" sentence = input("input a sentence:")
words = sentence.split()
print(words)
count = len(words)
print(count) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """
""" 
x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

#Let's create a function that determines if a number is odd or even

""" number = input("enter a number:")
if number / 2 == 0:
    print("even")
else:
    print("odd") """

#Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ". 

""" def calculate_tip(bill, service_rating):
    tip_percentages = {
        "bad": 0,
        "okay": 0.15,
        "good": 0.20,
        "great": 0.25
    }

    tip = bill * tip_percentages[service_rating.lower()]
    
    total_amount = bill + tip
    
    return f"Bill: ${bill:.2f}, Tip: ${tip:.2f}, Total: ${total_amount:.2f}"

print(calculate_tip(50, "good")) """

#Create a function that accepts an input and determines all factors of the number. 

def find_factors(number):
    factors = []
    
    for i in range(1, number + 1):
        if number % i == 0:  
            factors.append(i)
    
    return factors

number = int(input("Enter a number: "))
print(f"Factors of {number} are: {find_factors(number)}")
