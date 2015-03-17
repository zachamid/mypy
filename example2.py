'''
Use the fibonacci function to complete the task
'''
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
  	return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)

'''
The print_fibonacci function is used to print the 
result for the output
'''
def print_fibonacci(n):
  print fibonacci(n)