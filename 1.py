list1 = ["яблоко", "груша", "слива"]
def show_list(list):
  for i in list:
    print (i)
list1.append("помело")
list1.append("банан")
list1.pop (2)
list1.remove("груша")
list1[-2]= "красное помело"
show_list(list1)