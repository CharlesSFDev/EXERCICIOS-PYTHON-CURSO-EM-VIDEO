lanche = ('Hamburguer', 'Suco', 'Pizza', 'Refrigerante', 'Pudim', 'Batata Frita')


print(lanche)

print('*********')

print(sorted(lanche))

print('*********')

for item in lanche:
    print(item)
print('*********')

for cont in range(0,len(lanche)):
    print(lanche[cont], ' ', cont)
print('*********')

for pos, cont in enumerate(lanche):
    print(lanche[pos], ' ' ,pos)