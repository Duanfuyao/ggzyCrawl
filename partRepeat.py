import random
f=open('./dataggzy_all.json','r',encoding='utf-8')
fout=open('./dataggzy__all.json','a',encoding='utf-8')
lines=f.readlines()
half=len(lines)/2
frontHalf=lines[0:int(half)]
lastHalf=lines[int(half):len(lines)]
for i in range(10):
    random.shuffle (frontHalf )
    random.shuffle (lastHalf )
    for x in frontHalf:
        fout.write(x)
    for x in lastHalf:
        fout.write(x)
