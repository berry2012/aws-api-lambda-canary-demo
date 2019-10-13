import random

# verison 1: generate random numbers between 1 and 10 but return null 
a = 0
b = 10
print('Loading function')

def lambda_handler(event, context):
  print(random.randint(a, b))



