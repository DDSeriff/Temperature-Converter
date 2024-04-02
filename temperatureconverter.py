convert = input("What temperature type are we converting? C for Celsius, F for Fahrenheit.\n")
temp = int(input("What temperature number?"))
fahr = 0
celc = 0
if convert.lower() == "c":
  fahr += (temp * 9) / 5 + 32
  print (str(temp) + " Celsius is " + str(round(fahr, 2)) + " Fahrenheit.")
elif convert.lower() == "f":
  celc += (temp - 32) * 5 / 9
  print (str(temp) + " Fahrenheit is " + str(round(celc, 2)) + " Celsius.")
else:
    print("Invalid input")