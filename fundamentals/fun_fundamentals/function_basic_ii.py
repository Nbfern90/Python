#1
def countdown(num):
  holder=[]
  for i in range(num,-1,-1):
    holder.append(i)
  return holder

print(countdown(5))

#2
def print_and_return(list):
  print(list[0])
  return list[1]

#3
print(print_and_return([1,2]))

def first_plus_length(list):
 return list[0] + len(list)

print(first_plus_length([15,2,3,4,5]))

#4
def values_greater_than_second(list):
  if len(list) < 2:
    return False
  new_list=[]
  for i in range(0,len(list)):
    if list[i] > list[1]:
      new_list.append(list[i])
  print(len(new_list))
  return new_list

#5
def length_and_value(size,value):
  new_list =[]
  for i in range(0,size):
    new_list.append(value)
  return new_list

print(length_and_value(4,7))
