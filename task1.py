import sys

count=len(sys.argv)-1
print(f'Count of arguments is {count}')

if len(sys.argv) > 2:
  second_argument=sys.argv[2].upper()
  print(f"Second argument is {second_argument}")
else:
  print("You do not have at least 2 arguments")