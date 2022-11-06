from typing import List

def merge_sort(data) -> None:
  if len(data) >1:
    mid = (len(data))//2
    data_left = data[:mid]
    data_right = data[mid:]
    merge_sort(data_left)
    merge_sort(data_right)
 
    a = 0 
    b = 0 
    c = 0 

    while a<len(data_left) and b<len(data_right):
      if data_left[a] <= data_right[b]:
        data[c] = data_left[a]
        a+=1
      else:
        data[c] = data_right[b]
        b+=1
      c+=1

    while a < len(data_left):
      data[c] = data_left[a]
      a+=1
      c+=1
    while b < len(data_right):
      data[c] = data_right[b]
      b+=1
      c+=1
    return data


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
