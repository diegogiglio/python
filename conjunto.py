'''
Um conjunto não suporta indices e não armazena valores duplicados
'''
#forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) 
print(s)
print(type(s))


#forma 2 (mais comum)
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))


a = {'a':1,'b':2,'c':3,'d':4,'e':5}
b = []

print(type(a))

if 13 in s:
    print('Tem o numero')
else:
    print('Não tem o numero')