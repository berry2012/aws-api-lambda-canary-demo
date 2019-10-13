import random

# verison 3: generate random numbers between 10 and 100 and display the result on web via API Gateway url
a = 10
b = 100
print('Loading function')

def lambda_handler(event, context):
  result = random.randint(a, b)
  print(result)
  return result


