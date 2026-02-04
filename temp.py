# fahrenheit=(celsius * 9/5) + 32
# kelvin = celsius + 273.15
celsius=0.0
fahrenheit=0.0
kelvin=0.0
arr = [celsius, fahrenheit, kelvin]
i=int(input("Enter which value do you want to enter(0 for celsius,1 for farhenheit,2 for kelvin):)"))
print(arr[i])

if(i==0):
    arr[i]=float(input("enter celsius:"))
    celsius=arr[i]
    fahrenheit=arr[i]*9/5+32
    kelvin=arr[i]+273.15
    print("Celsius is:",celsius)
    print("Fahrenheit is:",fahrenheit)
    print("Kelvin is:",kelvin)

elif(i==1):
    arr[i]=float(input("enter farhenheit:"))
    fahrenheit=arr[i]
    celsius=(arr[i]-32)*5/9
    kelvin=(arr[i]-32)*5/9+273.15
    print("Celsius is:",celsius)
    print("Fahrenheit is:",fahrenheit)
    print("Kelvin is:",kelvin)
elif(i==2):
    arr[i]=float(input("enter kelvin:"))
    kelvin=arr[i]
    celsius=arr[i]-273.15
    fahrenheit=(arr[i]-273.15)+9/5*32
    print("Celsius is:",celsius)
    print("Fahrenheit is:",fahrenheit)
    print("Kelvin is:",kelvin)
else:
    print("Invalid input")
