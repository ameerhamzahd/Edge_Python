#1. Practice-1: Print the first 10 numbers using the for loop.

for i in range(1, 11):

    print(i)

#2. Practice-2: Write a program to calculate the sum of all numbers from 1 to n, where n is entered by the user

n = int(input ("Enter a number: "))

total = sum(range(1, n + 1))

print(f"sum: {total}")

#3. Practice-3: Create a program to reverse a string using a loop.

string = input("Enter a string: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print(f"Reversed string: {reversed_string}")

#Practice-4: Write a program to print all the prime numbers between 1 and 100.

for num in range(2, 101):
    is_prime = True

    for i in range(2, int (num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)

#5. Class practice:

count = ["none", "one", "one two", "one two three", "one two three four"]
word = "But only"

for number in range(5, 0, -1):
    print(number, "little ducks went out one day")
    print("Over the hill and far away")
    print('Mother duck said, "Quack, quack, quack, quack"')

    if number == 2:
        print("But only 1 little duck came back")
        print("one")

    else:
        new_numbers = number - 1
        print(word, new_numbers, "little ducks came back")

        if new_numbers <= len(count):
            print(count[new_numbers])

    print()


