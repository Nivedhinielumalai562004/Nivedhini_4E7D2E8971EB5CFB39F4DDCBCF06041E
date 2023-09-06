num =int(input("Enter the year:"))

if(num%4 == 0):
  if(num%100 == 0):
    if(num%400 == 0):
      print("%d is a Leap year"%num)
    else:
      print("%d is not"%num)
  else:
    print("%d is a Leap year"%num)
else:
  print("%d is not"%num)
  
