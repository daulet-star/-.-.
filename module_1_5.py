immutable_var= 1,2,'ban','man',0,5,1.5
print(immutable_var)

#immutable_var[0]=4
#выдает ошибку и говорит нам что он не потдерживает обращение по элементам

mutable_list=([0,1],'два',[3,4],'пять')
print(mutable_list)
mutable_list[0][0]='ноль'
print(mutable_list)
mutable_list[2][0]='три'
print(mutable_list)
mutable_list[2][1]='четыре'
print(mutable_list)
