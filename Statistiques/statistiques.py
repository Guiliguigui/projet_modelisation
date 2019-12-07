from exo_entrées import data
import argparse
import sys
import re
import os
import random
# coding=<utf-8>


if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('inexo')
    args=parser.parse_args()
    exo = args.inexo
    exos = data.keys()
    if not exo in exos :
        print("ERROR 101: \'%s\' n'est pas un exercice!" % exo)
        sys.exit(101)
    
    etats = data[exo]['etats']

    print('Exercice choisis : %s\n'% exo)
    print('Nombre d\'états différents : %d\n'%data[exo]['nombre_etats'])
    
    for cle, etat in etats.items():
        print(' ', cle, ' = ', etat['nom_complet'])
        print('     Transitions possibles :')
        for trans, valeur in etat['transitions'].items():
            print('      ->', trans, ' : ', valeur)

    print()
    objets_etat = int (input('Combien d\'objets par états? '))

    for cle, etat in etats.items():
        etat['nb_objets'] = objets_etat

    iteration = int( input('Combien d\'itération? '))
    print()

    history = [{}]
    for cle, etat in etats.items():
        temp = cle.split('_')
        history[0][temp[1]] = etat['nb_objets']

    for index in range(iteration):
        futur = {}
        for cle, etat in etats.items():
            for objet in range(etat['nb_objets']):
                randval = random.randint(0,100)
                probacum = 0
                for trans, valeur in etat['transitions'].items():
                    if not(futur.get(trans)):
                        futur[trans] = 0
                    if( probacum <= randval < probacum + valeur*100):
                        futur[trans] += 1
                    elif(randval == 100):
                        futur[trans] += 1
                        randval = -1    
                    probacum += valeur*100
        for cle, nbfutur in futur.items():
            etats['etat_'+cle]['nb_objets'] = nbfutur
        history.append(futur)
        
    somme = {}

    for i in range(len(history)):
        total = 0
        for cle, valeur in history[i].items():
            total += valeur
            if not(somme.get(cle)):
                somme[cle] = 0
            somme[cle] += valeur
        print('Iteration n°',i,' : ',history[i],' Total = ', total)

    sm=0
    print("\nMoyennes :")
    for cle, valeur in somme.items():
        print(cle,"-> ",valeur/(iteration+1))
        sm+=valeur/(iteration+1)
    print('total = ', sm)

    sf=0
    print("\nFréquences :")
    for cle, valeur in somme.items():
        print(cle,"-> ",valeur/(objets_etat*len(etats))/100)
        sf+=valeur/(objets_etat*len(etats))/100
    print('total = ', sf)

        


