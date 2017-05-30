import re
import os
import random
import codecs


def meta_compile():
    meta_info = open('MetaInfo.csv', 'w')
    meta_info.write('Name of File;Source;Year of Production;Name;Resposible')
    for root,dirs,files in os.walk('.//Corpora'):
        for folder in dirs:
            #meta_info.write('\n' + folder + ';OralHistory;')
            for root,dirs,files in os.walk('.//Corpora//' + folder + '//'):
                for file in files:
                    if file[-7:] == 'RES.txt':
                        meta_info.write('\n' + folder + ';OralHistory;')
                        try:
                            
                            read_file = open('.//Corpora//' + folder + '//' + file, 'r', encoding = 'utf-8').read()#, encoding = 'utf-8').read()
                            full_name = re.sub('[0-9]','', file)
                            full_name = full_name.replace('_','')
                            full_name1 = re.sub('^-','', full_name)[:-7]
                            full_name2 = full_name1.replace('red','').replace('check', '').replace('edit', '').replace('ред', '')
                            year_prod1 = compile_data(read_file, '([1|2][\\d^7]{3}?) года')
                            year_prod = list(year_prod1)
                            #print(random.choice(year_prod))
                            meta_info.write(random.choice(year_prod) + ';')
                            meta_info.write(full_name2 + ';')
                            meta_info.write('Наумов Александр;')
                            
                        except:
                            meta_info.write(';;Наумов Александр;')
                            continue
                   
    meta_info.close()
                                

def compile_data(read_file, reg_exp):
    data = set(re.findall(reg_exp, read_file))
    return data
    


                      

meta_compile()
