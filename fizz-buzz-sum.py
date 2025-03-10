#Q- https://datalemur.com/questions/python-fizz-buzz-sum

def fizz_buzz_sum(target):
  
  multiples_list = []
  for item in range(target):
    if item%3==0 or item%5==0:
      multiples_list.append(item)
      
  
  
  return sum(multiples_list)
