print ("python program convert celcius temp to farenhit");
print("accept the celcius temp from user");
celcius = float(input("please enter the temp in celcius -"));
farenheit = (celcius * 1.8)+32
print('%0.1f degree celcius is equal to %0.1f degree farenheit '%(celcius,farenheit));
temp = farenheit
if(temp >= 105):
  print ("it summer like weather")
elif (temp<=32):
    print ('wow must be pretty cold there')
else:
      print("the temp is right between spring and fall not too cold not to warm in my  opinion thats the best temp")