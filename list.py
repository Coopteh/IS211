list1 = ['яблоко', 'груша', 'слива']
list2 = ['помело', 'банан']
def show_list(list):
    for i in list:
        print(i)
def add_list(list1, list2):
    for i in list2:
        list1.append(i)
add_list(list1, list2)
list1.pop(2)
list1.remove('груша')
list1[1] = 'красное помело'
show_list(list1)

