a=float(input("First Number:"))
b=float(input("Second Number:"))
o=input("choose one(+,-,*,/): ")
if o == "+":
  result=a+b
elif o == "-":
  result=a-b
elif o == "*":
  result=a*b
elif o == "/":
  if(b == 0):
    result=print("Cannot divide by zero")
  else:
    result=a/b
else:
  print("Invalid")
if 'result' in locals():
  if result.is_integer():
    print("Answer:",int(result))
  else:
    print("Answer:",result)