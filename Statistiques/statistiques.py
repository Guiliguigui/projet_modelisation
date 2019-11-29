from exo_entrées import data
import argparse
import sys
import re


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


