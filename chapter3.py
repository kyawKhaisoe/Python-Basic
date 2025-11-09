user_age_str = input ('Enter your age:' )
user_age = int (user_age_str)

if user_age >= 18:
    print("You can apply for driving license")
else:
    print("You are not eligible for driving license")

print("----Congratulation!---")


#next project

num1 = 10
num2 = 10

if num1 == num2 :
    print(f"Numbers are equal: {num1} and {num2}")
else:
    print(f"Numbers are not equal: {num1} and {num2}")

    
print("----End----")


#case_sensitive

password = "MySecretPassword"
entered_password = input("Enter secrect password: ")

if entered_password == password:
    print("Password Correct!")
else:
    print("Try Again! ")



print("----Finished----")


number_str = input ("Enter a number: ")
number = int (number_str)

if number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is Odd number" )


#Temperature Checker
temperature_str = input("Enter temperature in celsius: ")
temperature = float (temperature_str)

if temperature > 30:
    print ("It's a hot today, Eat Ice Cream.")
else:
    print ("It's a cool today, Drink coffee.")

print("----Done----")





print("\n-- if-else Example---")
#Traffic Light Simulation

light_color = input ("Enter traffic light color (red, yellow, green): ").lower()

#change to lower case to avoid case sensitivity issue

if light_color == "red":
    print("Stop!)")
elif light_color == "yellow":
    print("Get Ready!")
elif light_color == "green":
    print("Go!")
else:
    print("Invalid color entered!") 



month_name = input("Enter month name: ").capitalize()


if month_name == "Febrauary":
    print(f"{month_name} has 28 days or 29 days in leap year.  ")
elif month_name in ("April,June,September,November"):
    print(f"{month_name} has 30 days.")
if month_name in ("January,March,May,July,August,October,December"):
    print(f"{month_name} has 31 days.")
else:
    print("Invalid month name entered!")

print("----Month Days Checker Finished----")



person_age_str = input ('Enter your age: ')
person_age = int(person_age_str )

is_student_input = input("Are you a student or not (True/False): ")
is_student = is_student_input.lower() == 'true'


if person_age < 18 or is_student:
    print("He is student and not an adult.")
elif person_age >= 18 and not is_student:
    print("He is adult and not a student.")
elif person_age >= 18 and is_student:
    print("He is adult and a student.")
else:
    print("He is not clear.")
print("----Age and Student Checker Finished----")   


#user and password checker

correct_username = "admin"
correct_password = "admin123"

user_input_username = input("Enter your username: ")    
user_input_password = input("Enter your password: ")    

if user_input_username == correct_username and user_input_password == correct_password:
    print("Login Successful!")  
else:
    print("Login Failed! Incorrect username or password.")

print("----Login Checker Finished----") 




weather = input("How is the weather today? (sunny, cloudy, rainy): ").strip().lower()
temperature_val = float(input("What is the temperature?: "))

if weather == "sunny":
    if temperature_val > 30:
        print("It's very hot today. Drink plenty of water!")
    else:
        print("Nice sunny day, you can go outside and enjoy!")

elif weather == "cloudy":
    print("It's cloudy today, a calm walk might be nice.")

elif weather == "rainy":
    print("It's rainy today, don't forget to take an umbrella.")
    if temperature_val < 10:
        print("It's cold and rainy, make sure to wear warm clothes.")
    else:
        print("Might be a good day to stay inside and read a book.")

else:
    print("I don't understand your input. Please enter sunny, cloudy, or rainy.")

