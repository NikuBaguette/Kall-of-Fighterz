def Encodage_CBC(texte:str = "ENSA", key:str = "01010101", init:str = "11010110")->str:
    if texte == "": return ''
    else:
        new, l = [], [lettre for lettre in bin(ord(texte[0]))[2:]], 
        space, new_init = 8-len(l), ""
        for i in range(space): new.append(int(init[i]))
        for b in range(space,len(l)+space): new.append(int(l[b-space])^int(init[b]))
        for b in range(len(new)): new[b] = new[b]^int(key[b])
        for string in new: new_init += str(string)
        return chr(int(new_init, 2)) + Encodage_CBC(texte[1:], key, new_init)

def Decodage_CBC(texte:str = "ENSA", key:str = "01010101", init:str = "11010110")->str:
    if texte == "": return ''
    else:
        new, l = [], [lettre for lettre in bin(ord(texte[0]))[2:]], 
        space, new_init, text = 8-len(l), "".join(l), ""
        for i in range(space): new.append(int(init[i]))
        for b in range(space,len(l)+space): new.append(int(l[b-space])^int(key[b]))
        for b in range(len(new)): new[b] = new[b]^int(init[b])
        for j in new: text += str(new[j])
        return chr(int(text, 2)) + Decodage_CBC(texte[1:], key, new_init)
print(Decodage_CBC(Encodage_CBC("Ta gueule")))