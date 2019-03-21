import json

def searchbuiding(dictlist, attr, value):
    dictlen = len(dictlist)
    if (dictlen > 0):
        for p in range(dictlen):
            if dictlist[p][attr] == value:
                return p, 1 #exist in dictlist

    return 0, 0 #not exist in dictlist



def searchperson(dictlist, attr, value):
    dictlen = len(dictlist)
    if (dictlen > 0):
        for p in range(dictlen):
            if (value in dictlist[p][attr]):
                
                return p, 1 #exist in dictlist

    return 0, 0 #not exist in dictlist


def jsonForHeat(read_file, write_file):
    dictlist = []
    dictlistrecordmacid = []
    history = []
    count = 0
    with open(read_file, "r") as r_file:
        data = {}
        time = u''
        #dictlist = []
   
        for line in r_file:
            lineDic = json.loads(line)
            addre_index, addre_exist = searchbuiding(dictlist, "label", lineDic[u'building']) #name is buiding name
            if (addre_exist == 1):
                #dictlist[addre_index]["y"] = dictlist[addre_index]["y"] + 1
                person_index, person_exist = searchperson(dictlistrecordmacid, "macaddr", lineDic[u'hmacaddress'].encode("utf-8"))
                if (person_exist == 1):
                    dictlistrecordmacid[person_index]["macaddr"].remove(lineDic[u'hmacaddress'].encode("utf-8"))
                    dictlistrecordmacid[addre_index]["macaddr"].append(lineDic[u'hmacaddress'].encode("utf-8"))
                    dictlist[addre_index]["y"] = dictlist[addre_index]["y"] + 1
                    dictlist[person_index]["y"] = dictlist[person_index]["y"] - 1
                
                else:
                    dictlistrecordmacid[addre_index]["macaddr"].append(lineDic[u'hmacaddress'].encode("utf-8"))
                    dictlist[addre_index]["y"] = dictlist[addre_index]["y"] + 1
            else:
                dictlist.append({"label":lineDic[u'building'].encode("utf-8"),"y":1})
                person_index, person_exist = searchperson(dictlistrecordmacid, "macaddr", lineDic[u'hmacaddress'].encode("utf-8"))
                if (person_exist == 1):
                    dictlistrecordmacid[person_index]["macaddr"].remove(lineDic[u'hmacaddress'].encode("utf-8"))
                    dictlistrecordmacid.append({"name":lineDic[u'building'].encode("utf-8"),"macaddr":[lineDic[u'hmacaddress'].encode("utf-8")]})
                    
                    dictlist[len(dictlist)-1]["y"] = 1
                    dictlist[person_index]["y"] = dictlist[person_index]["y"] - 1
                else:
                    dictlistrecordmacid.append({"name":lineDic[u'building'].encode("utf-8"),"macaddr":[lineDic[u'hmacaddress'].encode("utf-8")]})
                    dictlist[len(dictlist)-1]["y"] = 1


            history.append(sorted(dictlist, key=lambda k: k["y"], reverse=True)[0:20])
    
    
    print(history[0:1000])
            #print(dictlist)
            #if (not (time == lineDic[u'changedon'])):
            #    time = lineDic[u'changedon']
            #    print(time)
            #print(lineDic[u'building'])
            #print(lineDic[u'hapmacaddress'])
            #print(lineDic[u'hmacaddress'])
    #with open(write_file, "w") as w_file:
        #json.dump()
    #print(dictlist)
    #newlist = sorted(dictlist, key=lambda k: k["y"])[0:20]
    #newlist = sorted(dictlist, key=lambda k: k["visittoday"], reverse=True)
    #print(newlist)
    #print(dictlistrecordmacid)


jsonForHeat("20180505Wed1209.json", "jsonforheat.json")

