import json



def jsonForHeat(read_file, write_file):
    with open(read_file, "r") as r_file:
        data = {}
        time = u''

        for line in r_file:
            lineDic = json.loads(line)
            if (not (time is lineDic[u'building'])):
                time = lineDic[u'changedon']
                print(time)
            #print(lineDic[u'building'])
            #print(lineDic[u'hapmacaddress'])
            #print(lineDic[u'hmacaddress'])
    with open(write_file, "w") as w_file:
        json.dump()



jsonForHeat("20180505Wed1209.json", "jsonforheat.json")

