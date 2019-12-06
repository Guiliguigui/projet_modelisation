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
    exos = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', ]
    if not exo in exos :
        print("ERROR 101: \'%s\' n'est pas un exercice!" % exo)
        sys.exit(101)
    
    etats = data[exo]['etats']

    print('Exercice choisis : %s'% exo)
    print('Nombre d\'états différents : %d'%data[exo]['nombre_etats'])
    
    for cle, etat in etats.items():
        print(' ', cle, ' = ', etat['nom_complet'])
        print('     Transitions possibles :')
        for trans, valeur in etat['transitions'].items():
            print('      ->', trans, ' : ', valeur)

    objets_etat = int (input('Combien d\'objets par Etats?'))

    for cle, etat in etats.items():
        etat['nb_objets'] = objets_etat

    iteration = int( input('Combien d\'itération?'))

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
                print(randval)
                for trans, valeur in etat['transitions'].items():
                    if( probacum < randval <= probacum + valeur*100):
                        if not(futur.get(trans)):
                            futur[trans] = 0
                        futur[trans] += 1
                        print('oui')
                    elif(99.99 < probacum <= 100):
                        futur[trans] += 1
                    else:
                        print('non')
                    probacum += valeur*100
        history.append(futur)
        for cle, etatfutur in futur.items():
            etats['etat_'+cle]['nb_objets'] = etatfutur
    for i in range(len(history)):
        print('Iteration n°',i,' : ',history[i])

