# %%

A = 1
B = 5

print(A)
print(B)

# %%

C = A
A = B
B = C
print(A)
print(B)

# %%

A, B = B, A
print(A)
print(B)

# %%

A, B, *_ = 'Christian', [1,2,3],'Vieira','Masculino' 
print(A,B,_)

# %%

A,*_,B = 'Christian', [1,2,3],'Vieira','Masculino'
print(A,B,_)

# %%
*_,A,B = 'Christian', [1,2,3],'Vieira','Masculino'
print(A,B,_)

# %%

dados = {'nome':'Christian', 'sobrenome':'Vieira'}
for i,j in dados.items():
    print(i,j)

# %%
def soma (a, *args):
    total = a + sum(args)
    return total

soma(1,3,6,8,9)
# %%
def soma_quatro(a,b,c,d):
    return a+b+c+d

values = [1,2,3,4]
soma_quatro(*values)
# %%
soma(*values)
