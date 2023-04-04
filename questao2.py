encontrar = int(input("digite o numero:"))

a = 0
b = 1

while a < encontrar:
    a, b = b, a + b

if(a == encontrar):
    print("pertence")      
else:
    print("Nao pertence")

