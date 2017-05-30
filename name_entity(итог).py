import re
import os


def main(folder, reg_exp3,reg_exp2, reg_exp1):
    for root, dirs, files in os.walk('.//Corpora//'):
        for folder in dirs:
            for root, dirs, files in os.walk('.//Corpora//' + folder + '//'):
                for fname in files:
                    if fname[len(fname) - 3::] == 'txt' and fname[len(fname) - 7::] != 'RES.txt':
                        print(fname)
            try:
                file = open('.//Corpora//' + folder + '//' + fname, 'r', encoding = 'utf-8').read()
                all_capitals3 = set(re.findall(reg_exp3, file))
                all_capitals2 = set(re.findall(reg_exp2, file))
                all_capitals1 = set(re.findall(reg_exp1, file))
            except:
                continue

            
            capitals2, capitals1 = named_entity(all_capitals3, all_capitals2, all_capitals1)
            create_xml(file, fname, capitals2, capitals1, all_capitals3, folder + '//')



def named_entity(all_capitals3, all_capitals2, all_capitals1):
    capitals2 = []
    capitals1 = []

    
    lem_freq = open('lemma.txt', 'r', encoding = 'utf-8').read().split()
    lem_freq1 = [i[:-1] for i in lem_freq]


    

    for k in all_capitals2:
        i = k.lower()
        if i[:-1] not in lem_freq or i[:-1] not in lem_freq1 or i not in lem_freq or i not in lem_freq1:
            capitals2.append(k)

    for k in all_capitals1:
        i = k.lower()
        if i[:-1] not in lem_freq or i[:-1] not in lem_freq1 or i not in lem_freq or i not in lem_freq1:
            capitals1.append(k)
    

    return capitals2, capitals1
    
        
def create_xml(file, name, capitals2, capitals1, all_capitals3, way):
    cit = open('cities_alltheworld.txt', 'r', encoding = 'utf-8').read().split()
    fileRES = open('.//Corpora//' + way + name[:-4] + ' XML_RESULT.xml', 'w', encoding = 'utf-8-sig')
    fileRES.write('<?xml version="1.0" encoding="utf-8"?><html>\r\n<head>\r\n</head>\r\n<body>\n')
    
    cit1 = [i[:-1] + 'е' for i in cit]
    cit2 = [i[:-1] + 'ой' for i in cit]
    cit3 = [i[:-1] + 'ом' for i in cit]
    cit4 = [i[:-1] + 'ем' for i in cit]
    cit5 = [i[:-1] + 'я' for i in cit]
    cit6 = [i[:-1] + 'ы' for i in cit]
    cit7 = [i[:-1] + 'а' for i in cit]

    citisall = []
    for gorod in capitals2 and capitals1:
        city = gorod[:-2]
        if city in cit or city in cit1 or city in cit2 or city in cit3 or city in cit4 or city in cit5 or city in cit6 or city in cit7 and len(gorod) > 4:
            citisall.append(gorod)
    
    citisall.sort(key = len)
    citisall.reverse()

    for NE3 in all_capitals3:
        if NE3 in file and NE3 + '</' not in file:
            file = file.replace(NE3, '<ne name="' + NE3 + '" type = "PERSON">' + NE3 + '</ne>')

##    for N_geo in citisall:
##        x1 = set(re.findall('(' + N_geo + '[\w]*\\b)', file))
##        for i in x1:
##            if i + '</' not in file:
##                file = file.replace(N_geo, '<ne name="' + N_geo + '" type = "GEO">' + N_geo + '</ne>')
            
    for element in capitals2:
        x2 = set(re.findall('(' + element + '[\w]*\\b)', file))
        for NE2 in x2:
            if NE2 in file and '>' + NE2 + '</' not in file and NE2 + '</' not in file and '="' + NE2 not in file and NE2 + '" type' not in file:
                file = file.replace(NE2, '<ne name="' + NE2 + '" type = "NE">' + NE2 + '</ne>')

    for elem in capitals1:
        x = set(re.findall('(' + elem + '[\w]*\\b)', file))
        for NE in x:
            if NE in file and '>' + NE + '</' not in file and NE + '</' not in file and '="' + NE not in file and NE + '" type' not in file:
                file = file.replace(NE, '<ne name="' + NE + '" type = "NE">' + NE + '</ne>')

        
    fileRES.write(file)
    fileRES.write('</body>\n</html>')

    fileRES.close()

main('.//texts', '([А-Я][а-я]{2,10} [А-Я][а-я]+ [А-Я][а-я]+)', '([А-Я][а-я]{3,10} [А-Я][а-я]+)[-.?!)(,:]? ?[^\W]','[^./?!]([А-Я][а-я]{3,30}?) [^\W]')
