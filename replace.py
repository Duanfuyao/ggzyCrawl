import cpca
import json
import pandas as pd
def getLocation(text):
    locForLine = cpca.transform(text, cut=False, pos_sensitive=True)
    print(locForLine)
    locForLine = locForLine[locForLine["省"] != ""]
    locations = []
    for i in range(len(locForLine)):
        locations.append(locForLine.iat[i, 0] + '_' + locForLine.iat[i, 1] + "_" + locForLine.iat[i, 2])

    counts = pd.value_counts(locations)
    countedlocations = counts.index.values.tolist()
    if len(countedlocations) == 0:
        return None
    result = countedlocations[0].split("_")
    return "-".join(result)
file = './dataggzy__all.json'
fileout='./dataggzy___all.json'
with open(file, encoding='UTF-8') as f:
    fout=open(fileout,'w',encoding='utf-8')
    for line in f:
        js=json.loads(line)
        text=js['text']
        js['招标地点']=getLocation(text)
        fout.write(json.dumps(js,ensure_ascii=False)+'\n')
    fout.close()
