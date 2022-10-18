def pektroj (riadok:int):
    s = riadok + 1
    for i in range(riadok+1):
        for s in range(s):
            print(end=' ')
        print('*'*(i*2+1))
pektroj(8)