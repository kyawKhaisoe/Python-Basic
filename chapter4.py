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


