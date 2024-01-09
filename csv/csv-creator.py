import os
namefile="ALUSECGRADOINDPAR"
directory="C:/Users/Utente/Desktop/Mat didattico/Tesi magistrale/PortaleScuola"
out = ["a"]
for file in os.listdir(directory):
    if file.startswith(namefile):
        #print(file)
        f = open(directory+"/"+file,"r")
        lines = f.readlines()
        out[0] = lines[0]
        out.extend(lines[1:len(lines)])
        f.close()
f = open(namefile+"-complete.csv","x")
f.writelines(out)
f.close()
print("Fatto!")