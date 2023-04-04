str = input("Digite a palavra:")
averso=''
i = len(str)
while i > 0: 
    averso += str[i-1]
    i = i - 1
print( averso) 