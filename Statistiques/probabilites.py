from exo_entrées import data
import argparse
import sys
import re
import os
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

    print("Exercice choisis : %s"% exo)
    print('Nombre d\'états différents : %d'%data[exo]['nombre_etats'])
    
    for cle, etat in etats.items():
        print(' ', cle, ' = ', etat['nom_complet'])
        print('     Transitions possibles :')
        for trans, valeur in etat['transitions'].items():
            print('      ->', trans, ' : ', valeur)

    formuleA = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['A'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['A']

    formuleC = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['C'] + etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['C']

    formuleE = etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['E'] + etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['E']

    A=formuleA
    C=formuleC
    E=formuleE

    print('Exercice C1 :')
    
    print('Cycle 1 :')
    print(A)
    print(C)
    print(E)
    nb=2

    while(nb<=10):
        formuleA = A * etats['etat_A']['transitions']['A'] + C * etats['etat_C']['transitions']['A']
        formuleC = A * etats['etat_A']['transitions']['C'] + E * etats['etat_E']['transitions']['C']
        formuleE = C * etats['etat_C']['transitions']['E'] + E * etats['etat_E']['transitions']['E']

        A=formuleA
        C=formuleC
        E=formuleE

        print ('Cycle n°',nb,' :')
        print(A)
        print(C)
        print(E)
    
        nb=nb+1
    