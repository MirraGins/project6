from operator import truth

my_dict={'Anna': '23/04/2002','Kiril': '14/10/1998','Anton': '11/11/1991'}
print(my_dict)
print(my_dict.get('Anna'))
print(my_dict.get('Piter', 'not found'))
my_dict['Sam']='22/03/1999'
my_dict['Mat']='30/05/2006'
print(my_dict)
a=my_dict.pop('Anna')
print(my_dict)
print(a)

my_set={1,3,3,3,4,5,4,'dog','apple',8,8}
print(my_set)
my_set.add(13)
my_set.add('cat')
print(my_set)
my_set.discard(3)
print(my_set)