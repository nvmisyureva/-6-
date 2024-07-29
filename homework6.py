#Практическое задание по теме: "Словари и множества"
my_dict={'битва на Калке':1223,' Невская битва':1240,'Ледовое побоище':1242,'Куликовская битва':1380}
print(my_dict)
print(my_dict['битва на Калке'])
print(my_dict.get('Полтавская битва'))
a={'Полтавская битва':1709,'Бородинское сражение':1812}
my_dict.update(a)
print(my_dict)
del my_dict['Полтавская битва']
print(a.values())
print(my_dict)

my_set={1,2,3,1,3,5,2,'a','s','a',False,(5,2,5)}
print(my_set)
my_set.add(90)
my_set.add(25)
print(my_set)
my_set.discard(3)
print(my_set)


