# python Operation with input 
num1 = input(" Please insert the first number: ")
num2 = input(" Please insert the second number: ")
operation = input(" Please inset your desired operation among +, -, *, /: ")

if operation == "+":
  result = float(num1) + float(num2)
  
  # print(result)
  
if operation == "-":
  result = float(num1) - float(num2)
  
if operation == "*":
  result = float(num1) * float(num2)
  
if operation == "/":
  result = float(num1) / float(num2)
else:
  print(" The operation is not /")  

  print(result)
  
  # we are going to else if (elif) to tell the program if the 1th Op is not true go to the 2th one
if operation == "+":
  result = float(num1) + float(num2)
elif operation == "-":
  result = float(num1) - float(num2)
elif operation == "*":
  result = float(num1) * float(num2)
elif operation == "/":
  result = float(num1) / float(num2)
else:
  result = " The operation you enter is  wrong"

  print(result) 
  
  # Operator most in math 
  
 # it could be - , /, * 
  
# this is assignment operator 

a = 10
a += 2


# compression operator > , < , => ,<+ , !=
age = input("please inset your age : ")
age = int(age)

if age <= 18:
  print(" Sorry , you are not allowed to enter ")
else:
  print(" Welcome")
name =  input(" Please inset your name")

if name == "Jack":
  print(" Sorry , you are not allowed to enter ")
else:
  print(" Welcome")
  
# Logic and / or

name =  input(" Please inset your name")
if name == "Jack" or  age < 18:
  print(" Sorry , you are not allowed to enter ")
else:
  print(" Welcome")
  
# in this case anyone can enter as long their name and age is not Jack with under 18

if name == "Jack" and  age < 18:
  print(" Sorry , you are not allowed to enter ")
else:
  print(" Welcome")