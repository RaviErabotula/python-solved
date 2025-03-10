#Q: https://datalemur.com/questions/python-weakest-strong-link



def weakest_strong_link(strength):

  col_di = {}
  row_di = dict(zip(range(len(strength)), strength))
  for i in range(len(strength)):
	  row_val = strength[i]
	  for j in range(len(strength[0])):
	    if j in col_di:
	      col_di[j].append(strength[i][j])
	    else:
	      col_di[j]=[strength[i][j]]
	
  for rno, val_li in row_di.items():
    
    row_min_val = min(val_li)
    row_min_idx = val_li.index(row_min_val)
    col_max_val = max(col_di[row_min_idx])
    
    if row_min_val==col_max_val:
      return col_max_val
    
  return -1
