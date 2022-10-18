sirka=int(input('zadaj sirku:'))
znak=(input('zadaj znak:'))
def obdlznik(sirka:int, znak:str):
    print(znak*sirka)
    print(znak + (sirka-2)*' '+znak)
    print(znak*sirka)
print(obdlznik(sirka, znak))