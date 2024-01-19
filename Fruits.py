list1 = ['Яблоко', 'Груша', 'Слива']
def show_list(list):
    for i in list:
       print(i)
list1.append('Помело')
list1.append('Банан')
list1.pop(2)
list1.remove("Груша")
list1[1] = 'Красное помело'
show_list(list1)