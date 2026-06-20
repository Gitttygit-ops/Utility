print("Welcome to the text repeater")
print( )
text = input("What text would you like to repeat? ")
right = True

while right:
  repeat_amount = input("How many times would you like to repeat the text? ")
  if repeat_amount.isdigit():
      repeat_amount = int(repeat_amount)
      if repeat_amount > 0:
         repeat_amount = int(repeat_amount)
         for i in range(repeat_amount):
            print(text)
            right = False
      else:
          print("Please enter a number greater than 0")
  else:
      print("Please enter a number greater than 0 ")


