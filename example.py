'''
Use the fibonacci function to complete the task
'''
def fibonacci(n):
  if( n == 0):
    return 0
  else:
    x = 0
    y = 1
    for i in range(1,n):
      z = (x + y)
      x = y
      y = z
    return y

'''
The print_fibonacci function is used to print the 
result for the output
'''
def print_fibonacci(n):
  print fibonacci(n)