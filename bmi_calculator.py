body_weight_str = input("Enter your body weight in kg: ")
height_str = input ("Enter your height in meter: ")

#covert string to float
body_weight_float = float(body_weight_str)
height_float = float(height_str)

BMI = body_weight_float // (height_float * height_float)

print(f'BMI Calculation is : {BMI}')





