import random

# verison 2: generate random numbers between 10 and 100
a = 10
b = 100
print('Loading function')

def lambda_handler(event, context):
  print(random.randint(a, b))
