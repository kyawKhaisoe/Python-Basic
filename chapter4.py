my_name = "Kyaw Khai Soe"

print ("--- Character from my name ---")

for letter in my_name:
    print (letter)

a_count = 0

for cha in my_name:
    if cha == "a":
        a_count += 1


print(f"'{my_name}' has {a_count} 'a'.")




#Find and count the letter "a" in the setence

setence = "Python is an amazing programming language."

a_count = 0

print("\n-- Finding letter 'a' in the setence ---")

for char in setence:
    if char == "a":
        a_count += 1


print(f"'{setence}' has {a_count} 'a'.")


#Print numbers from 1 to 10
for number in range(1, 11):
    print(number)

for j in range(5, 16):
    print(j)


#Count backward from 10 to 1

for back in range(10, 0, -1):
    print(back)


#Example stopping a loop with break statement

print("\n-- Breaking the loop example ---")
for i in range(1, 11):
    if i == 5 :
        print("Reached to 5, Stopping the loop. ")
        break
    print(i)


#skipping an iteration with continue statememt
print("\n-- Skipping the iteration example ---")

for num in range(1, 6):
    if num % 2 == 0: #even number
        print(f"{num} is even number, Skipping...")
        continue    #skip this iteration and go to next iteration
    print(f"{num} is odd number ")




#A llop that stops when it finds a number greater than 5

print('\n-- break when number greater than 5 is found --- ')

for x in range(1, 11):
    if x > 5:
        print (f"Found {x}, which is greater than 5 , stopping the loop.:")
        break
    print(f"Current number is  {x}")



#a loop that skip numbers divisible by 3
print("\n-- Skipping numbers divisible by 3 ---")
for y in range(1, 11):
    if y % 3 == 0:
        print(f"skipping {y} as it is divisible by 3")
        continue
    print(f" not divided by 3:{y}")



#Eg: Creating a Multiplication Table
print("\n ---Multiplication Table (Nested Loops)")

for i in range(1,4): #Outer Loop
    for j in range(1,4): #Inner Loop
        print(f"{i} * {j}")

    print("---")





#Eg: Creating a Multiplication Table from 1 to 5

print("\n ---Multiplication Table (Nested Loops)")

for i in range(1,6): #Outer Loop
    for j in range(1,6): #Inner Loop
        print(f"{i} * {j} = {j} * {i}")


    print("-" * 15 ) # prints a line of dashes



#Creating a star pattern (Triangle)
print("\n ---Star Pattern--- ")

for row in range(1, 7): #5 rows
    for col in range(row): #Number of stars in each row
        print("*", end="") #Print star without newline  
    print() #Move to the next line after each row



print("\n--- Diamond Pattern ---")

rows = 5

# Upper part
for row in range(1, rows + 1):
    print(" " * (rows - row), end="")
    print("*" * (2 * row - 1))

# Lower part
for row in range(rows - 1, 0, -1):
    print(" " * (rows - row), end="")
    print("*" * (2 * row - 1))



secret_number = 7

while True: #keep asking until correct guess

    guess_str = int (input("Guess the secret number between 1 and 10:"))

    if guess_str == secret_number:
        print("Congratulations! You guessed it right.")
        break
    elif guess_str < secret_number:
        print("Too Low , Try again.")
    else:
        guess_str > secret_number 
        print("Too High , Try again.")



#Factional Calculator
num = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= num:
    factorial = factorial * i
    i += 1

print("Factorial of", num, "is:", factorial)












