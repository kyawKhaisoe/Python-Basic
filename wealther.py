mark = input("Enter your mark:")
result_mark = int(mark)


if 90 <= result_mark <= 100:
    print("Grade A, Excellent")
elif 80 <= result_mark < 89:
    print("Grade B, Very Good")
elif 70 <= result_mark < 79:
    print("Grade C, Good")
elif 60 <= result_mark < 69:
    print("Grade D, Pass")
elif 0 <= result_mark < 59:
    print("Grade F, Fail")
elif result_mark < 0 or result_mark > 100:
    print("Invalid Mark! Please enter valid mark between 0 to 100") 
 
else:
    print("Error in input!")    


