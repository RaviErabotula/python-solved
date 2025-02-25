#Q: https://datalemur.com/questions/python-compound-interest


def compound_interest(principal, rate, contribution, years):
  
  new_pricipal = principal
  for year in range(1,years+1):
    
    interest_amt = new_pricipal*(rate/100)
    new_pricipal = new_pricipal+interest_amt+contribution
    
  return round(new_pricipal,2)
