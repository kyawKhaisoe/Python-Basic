my_name = 'Mg Mg'
fav_number = 23
height_in_feet = 5.8
drinks_coffee = True


print("My name is ", my_name)
print("My fav number is", fav_number)
print("My height is", height_in_feet)
print("I drink coffee.(True/False)" , drinks_coffee)


num_students = 25
avarage_score = 88.5
course_name = "Python Programming"
is_course_finished = False


#test with type() function


print("\n-- Data Types Checking ---")
print("num_students's Data Type:", type(num_students))
print("avarage_score's Data Type:", type(avarage_score))
print("course name's Data Type:", type(course_name)) 
print("is course finished's Data Type:", type(is_course_finished) )




num1 = 32
num2 = 23

addition = num1 + num2
substration = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
remainder = num1 % num2
power = num1 ** num2


print("\n-- Maths, Calculations --")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {substration}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {floor_division}")
print(f"{num1} % {num2} = {remainder}")
print(f"{num1} ** {num2} = {power}")




first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name) 


greeting = "Hello "
repeated_greeting = greeting * 3
print(repeated_greeting)




my_string = 'Python is FUN! '
print("\n-- String Operations --")
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Trim: ", my_string.strip())
print("Replace: ", my_string.replace("FUN", "AWESOME"))
print("Length: ", len(my_string))   


#change string into integer
str_num = 123
int_num = int(str_num)
print(int_num,type(int_num))

#change string into float
str_float = 12.34
float_num = str(str_float)
print(str_float,type(str_float))

#change integer into string
num = 100
str_from_num = str(num)
print(str_from_num,type(str_from_num))



#build simple calculator
num_str1 = input("Enter first number: ")
num_str2 = input("Enter second number: ")

#change those string to integer

num_int1 = int (num_str1)
num_int2 = int (num_str2)

#sum these two
sum_result = num_int1 + num_int2

print(f'Sum of two number is {sum_result}')

#product these two
product_result = num_int1 * num_int2

print(f"Product of two number is {product_result}")

#divided these two

divided_result = num_int1 // num_int2
print(type(divided_result))

print(f"Deivde of two number is {divided_result}")



























