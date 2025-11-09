#advice pon on the weather\

wealther = input('how is the weather today? (sunny,cloudy,ranily):').lower()
temperature_val_str = input('How much temperature?: ')
temperature_val = float (temperature_val_str)

if wealther == 'sunny':
    if temperature_val > 30:
        print("It's hot today, drinks more water.   ")
    else:
        print("Shiny , go out and have fun!  ")

elif wealther == 'cloudy':
    print("It's cloudy today, take a walk outside.  ")
elif wealther == 'rainy':
    print ("It's rainy today, don't forget to take an umbrella.") 
    if temperature_val < 10:
        print("It's cold and rainy, wear warm clothes.  ")
    else:
        print("GO Sleep at home and read a book.  ")

    print ("Dont't understand your input. Please enter sunny, cloudy, or rainy.")