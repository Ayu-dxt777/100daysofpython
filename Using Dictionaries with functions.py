# Making a Simple Calculator using Dictionaries with Functions

print(logo)

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1/n2
n1 = int(input("What's the first number? "))
operation = str(input("Pick an operation: \n + \n - \n * \n / \n "))
n2 = int(input("What's the next number?: \n"))
dict = {"+": add, "-": sub, "*": multiply, "/": divide}
function = dict[operation]
result = function(n1,n2)
print(f"{n1} {operation}  {n2} : {result}")
calculation_finished = False
while not calculation_finished : 
  n1 = result
  wish_continue = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, type 'exit' to exit: "))
  if wish_continue == "y":
    operation = str(input("Pick an operation: \n + \n - \n * \n / \n"))
    function = dict[operation]
    n2 = int(input("What's the next number?"))
    result2 = function(n1,n2)
    print(f"{n1}  {operation} {n2} : {result2}")
  elif wish_continue == 'n':
    print(logo)
    n1 = int(input("What's the first number?"))
    operation = str(input("Pick an operation: \n + \n - \n * \n / \n"))
    n2 = int(input("What's the next number?"))
    result = dict[operation]
    print(f"{n1} {operation} {n2} : {result}")
  elif wish_continue == 'exit':
    calculation_finished = True
  else:
    print("try again")
