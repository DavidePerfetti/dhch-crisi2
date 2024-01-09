# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 10:43:34 2023

@author: Utente
"""
import os

#PARAMETRI
namefile="ALUCORSOETASTA-SCUOLA PRIMARIA"
directory="C:/Users/Utente/Desktop/Scuola-aggregati"
filtercolumn = 3 #colonna di filtro (indice da 0)

#CODICE
filterdict = {}
header = ["FILE NOT FOUND"]
for file in os.listdir(directory):
    if file.startswith(namefile):
        #print(file)
        f = open(directory+"/"+file,"r")
        lines = f.readlines()
        header[0] = lines[0]
        #out.extend(lines[1:len(lines)])
        for line in lines[1:len(lines)]:
            #print(filterdict)
            data = line.split(",")
            x = filterdict.get(data[filtercolumn],header.copy())
            x.append(line)
            filterdict[data[filtercolumn]] = x
        f.close()
for key in filterdict:
    f = open(namefile+"-"+key+".csv","x")
    f.writelines(filterdict[key])
    f.close()
print("Fatto!")
