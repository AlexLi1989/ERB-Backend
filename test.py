# output = {x: ('odd' if x%2 else 'even') for x in range(1,11)}
# print(output)

# list=['apple','cat','python']
# output2={e:len(e)for e in list}
# print(output2)

# list2=['a','b','c']
# output3={x:list2[x] for x in range(len(list2))}
# print(output3)

# list3=['apple','banana']
# output4={e.upper():e for e in list3}
# print(output4)

# dict1={'a':9,'b':4,'c':12}
# output5={k:v for k,v in dict1.items() if not v%3}
# print(output5)

# list4 = ['a','b','c']
# list5 = [1,2,3]
# output6={k:v for k in list4 for v in list5 if list4.index(k)==list5.index(v)}
# print(output6)

# s = 'hello'
# output7 = {char:s.count(char) for char in s }
# print(output7)

matrix = [[1,2,3],[4,5,6]]
output8={} #{(0,0):1,(0,1):2,(1,0):3,(1,1):4}
for d1 in matrix:
  for d2 in d1:
    key = (matrix.index(d1),d1.index(d2))
    output8[key] = d2
print(output8)