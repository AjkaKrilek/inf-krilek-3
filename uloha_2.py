n = int(input('zadaj pocet:'))
text = input('zadaj text:')
def riadok(n:int,text):
    if text !='':
        print('*'*(n/2), text, '*'*(n/2))
print(riadok(n,text))
