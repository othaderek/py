magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n") #\n creates a new line.

print("Thank you everyone! \nThat was a great magic show!")


message = ("Those are the first 9 numbers!")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
	print(number)

print(message)

#using a list function to generate a set of numbers

numbers = list(range(1,11))
print(numbers)

# for loop that saves each number in number variable and prints
for number in numbers:
	print(number)

even_numbers = list(range(2,11,2))
print(even_numbers)

odd_numbers = list(range(1,101,2))
print(odd_numbers)

for odd_number in odd_numbers:
	print(odd_number*odd_number)







