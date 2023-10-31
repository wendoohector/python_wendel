import random
import pickle
import os


def wend (non_uti):
     return non_uti.islower() and ' ' not in non_uti

non_uti = input("---Antre yon non ki pa gen espas epi ki an miniskil selman: ")
while  not wend(non_uti):
       print("---Non an pa valide, li pa sipoze gen espas epi tout let yo dwe an miniskil---")
       non_uti = input("----Antre yon non ki pa gen espas epi ki an miniskil selman: ")

jwe=True 
while jwe:
    nbre_ord = random.randint(0,100)
    print(nbre_ord)
        
    chans = 5
    sko = 0
    while(chans>0):
        nbre_uti = (input("---Antre yon nonb ki twouvel ant 0 a 100: "))
        while int(nbre_uti) < 0 or int(nbre_uti) > 100:
            nbre_uti = int(input("----Antre yon nonb ki twouvel ant 0 a 100: "))
        if nbre_ord==int(nbre_uti):
            print("-----Bravo, Ou genyen------")
        
            sko += chans*30
            break
        else:
            chans -=1
        
            if nbre_ord < int(nbre_uti):
                print(f"------Nonb ou antre a two gwo, ou rete: {chans} chans")
               
            elif nbre_ord > int(nbre_uti):
                  print(f"-----Nonb ou antre a two piti, ou rete: {chans} chans")
        if chans == 0:
                print(f"------Ou pedi, Nonb kache a se: {nbre_ord}")


    print(f"Sko {non_uti} fe pou pati sa se: {sko}")
    avi_jwe=input("----Peze k pouw kanpe jwet la,peze nenpot let pouw kontinye : ")
    if(avi_jwe.lower()=="k"):
        jwe=False
baz_de_done = {}
fichye = 'gere_sko'
baz_de_done[sko]=non_uti


if os.path.exists(fichye):
    with open(fichye,'rb') as paj:
        baz_de_done = pickle.load(paj)


with open (fichye,'wb') as paj:
    pickle.dump(baz_de_done,paj)

sko_ansyen= baz_de_done.get(non_uti,sko)
sko_total= sko + sko_ansyen
print(f"Sko total {non_uti} lan se: {sko_total}")

print("--------------------------")



                         

   



    
            
        


        

    


                    

