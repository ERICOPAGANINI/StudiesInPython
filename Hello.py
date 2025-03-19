#Reading the name of the user, removing 
#the whitespaces from str and capitalize them
name = input("What's your name? ").strip().title()

# Slipting user's name into first name and last name.
first, middle, last = name.split(" ")

#Printing the name gathered and greeting him
print("Hello" , name, "nice to meet you", sep="--", end=". ")
print()
print(f"Hello {name}", "nice to meet you")
print("Your first name is " + first)
print("Your middle name is " + middle)
print("Your last name is " + last)



