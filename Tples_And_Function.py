# in tuples we use {} to make the list while in list we use []
shopping_list ={"Milk", "Bread", " Water"}
print(shopping_list)

# Using Function in Python
# simple using of Function 
"""def say_hello():
  print(" Hello There")
  print("I am here")
  
print("====================================")
say_hello()
print("====================================")"""

# Function with input 
"""def say_hello(name):
  print(" Hello " + name)
  print("I am here")
  
first_name = "Reza"
print("====================================")
say_hello( first_name)
print("====================================")"""

# with Two 
"""def say_hello(name , age):
  print(" Hello " + name + " You are " + age)
  print("I am here")
  
first_name = "Reza"
age = "40"
print("====================================")
say_hello(first_name, age)
print("====================================")"""

# using retune
def add_numbers(a ,b):
  c = a + b
  return c
  
num1 = 50
num2 = 10

print("====================================")
result = add_numbers(num1, num2)
print(result)

print("====================================")