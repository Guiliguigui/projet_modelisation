from exo_entrées import data
import argparse
import sys
import re
import os
# coding=<utf-8>

def formuleC1(iteration):
    formuleA = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['A'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['A']

    formuleC = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['C'] + etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['C']

    formuleE = etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['E'] + etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['E']

    A=formuleA
    C=formuleC
    E=formuleE
    
    print('Cycle 1 :')
    print('A : ',A)
    print('C : ',C)
    print('E : ',E)
    nb=2

    while((nb)<=iteration):
        formuleA = A * etats['etat_A']['transitions']['A'] + C * etats['etat_C']['transitions']['A']
        formuleC = A * etats['etat_A']['transitions']['C'] + E * etats['etat_E']['transitions']['C']
        formuleE = C * etats['etat_C']['transitions']['E'] + E * etats['etat_E']['transitions']['E']

        A=formuleA
        C=formuleC
        E=formuleE

        print ('Cycle n°',nb,' :')
        print('A : ',A)
        print('C : ',C)
        print('E : ',E)
    
        nb=nb+1
    
def formuleC2(iteration):
    formuleB = etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['B'] + etats['etat_N']['nb_objets'] * etats['etat_N']['transitions']['B']

    formuleN = etats['etat_N']['nb_objets'] * etats['etat_N']['transitions']['N'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['N']+ etats['etat_P']['nb_objets'] * etats['etat_P']['transitions']['N']

    formuleP = etats['etat_P']['nb_objets'] * etats['etat_P']['transitions']['P'] + etats['etat_N']['nb_objets'] * etats['etat_N']['transitions']['P']

    B=formuleB
    N=formuleN
    P=formuleP
    
    print('Cycle 1 :')
    print('B : ',B)
    print('N : ',N)
    print('P : ',P)
    nb=2

    while(nb<=iteration):
        formuleB = B * etats['etat_B']['transitions']['B'] + N * etats['etat_N']['transitions']['B']

        formuleN = N * etats['etat_N']['transitions']['N'] + B * etats['etat_B']['transitions']['N']+ P * etats['etat_P']['transitions']['N']

        formuleP = P * etats['etat_P']['transitions']['P'] + N * etats['etat_N']['transitions']['P']

        B=formuleB
        N=formuleN
        P=formuleP
    
        print ('Cycle n°',nb,' :')
        print('B : ',B)
        print('N : ',N)
        print('P : ',P)
    
        nb=nb+1

def formuleC3(iteration):
    formuleN = etats['etat_N']['nb_objets'] * etats['etat_N']['transitions']['N'] + etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['N']+ etats['etat_O']['nb_objets'] * etats['etat_O']['transitions']['N']

    formuleS = etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['S'] + etats['etat_O']['nb_objets'] * etats['etat_O']['transitions']['S']

    formuleE = etats['etat_N']['nb_objets'] * etats['etat_N']['transitions']['E'] + etats['etat_S']['nb_objets'] * etats['etat_S']['transitions']['E']

    formuleO = etats['etat_N']['nb_objets'] * etats['etat_N']['transitions']['O'] + etats['etat_S']['nb_objets'] * etats['etat_S']['transitions']['O']

    N=formuleN
    S=formuleS
    E=formuleE
    O=formuleO
    
    print('Cycle 1 :')
    print('N : ',N)
    print('S : ',S)
    print('E : ',E)
    print('O : ',O)
    nb=2

    while(nb<=iteration):
        formuleN = N * etats['etat_N']['transitions']['N'] + E * etats['etat_E']['transitions']['N']+ O * etats['etat_O']['transitions']['N']

        formuleS = E * etats['etat_E']['transitions']['S'] + O * etats['etat_O']['transitions']['S']

        formuleE = N * etats['etat_N']['transitions']['E'] + S * etats['etat_S']['transitions']['E']

        formuleO = N * etats['etat_N']['transitions']['O'] + S * etats['etat_S']['transitions']['O']

        N=formuleN
        S=formuleS
        E=formuleE
        O=formuleO

        print ('Cycle n°',nb,' :')
        print('N : ',N)
        print('S : ',S)
        print('E : ',E)
        print('O : ',O)
    
        nb=nb+1

def formuleC4(iteration):
    formuleA = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['A'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['A'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['A']

    formuleB = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['B'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['B'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['B']

    formuleC = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['C'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['C'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['C']

    A=formuleA
    B=formuleB
    C=formuleC
    
    print('Cycle 1 :')
    print('A : ',A)
    print('B : ',B)
    print('C : ',C)
    nb=2

    while(nb<=iteration):
        formuleA = A * etats['etat_A']['transitions']['A'] + B * etats['etat_B']['transitions']['A'] + C * etats['etat_C']['transitions']['A']

        formuleB = A * etats['etat_A']['transitions']['B'] + B * etats['etat_B']['transitions']['B'] + C * etats['etat_C']['transitions']['B']

        formuleC = A * etats['etat_A']['transitions']['C'] + B * etats['etat_B']['transitions']['C'] + C * etats['etat_C']['transitions']['C']

        A=formuleA
        B=formuleB
        C=formuleC

        print ('Cycle n°',nb,' :')
        print('A : ',A)
        print('B : ',B)
        print('C : ',C)
    
        nb=nb+1
    
def formuleC5(iteration):
    formuleA = etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['A']

    formuleB = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['B'] + etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['B'] + etats['etat_D']['nb_objets'] * etats['etat_D']['transitions']['B']

    formuleC = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['C'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['C'] + etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['C']

    formuleD = etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['D']

    formuleE = etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['E'] + etats['etat_D']['nb_objets'] * etats['etat_D']['transitions']['E']

    A=formuleA
    B=formuleB
    C=formuleC
    D=formuleD
    E=formuleE
    
    print('Cycle 1 :')
    print('A : ',A)
    print('B : ',B)
    print('C : ',C)
    print('D : ',D)
    print('E : ',E)
    nb=2

    while(nb<=iteration):
        formuleA = C * etats['etat_C']['transitions']['A']

        formuleB = A * etats['etat_A']['transitions']['B'] + E * etats['etat_E']['transitions']['B'] + D * etats['etat_D']['transitions']['B']

        formuleC = A * etats['etat_A']['transitions']['C'] + B * etats['etat_B']['transitions']['C'] + E * etats['etat_E']['transitions']['C']

        formuleD = B * etats['etat_B']['transitions']['D']

        formuleE = C * etats['etat_C']['transitions']['E'] + D * etats['etat_D']['transitions']['E']

        A=formuleA
        B=formuleB
        C=formuleC
        D=formuleD
        E=formuleE

        print ('Cycle n°',nb,' :')
        print('A : ',A)
        print('B : ',B)
        print('C : ',C)
        print('D : ',D)
        print('E : ',E)
    
        nb=nb+1
    
def formuleC6(iteration):
    formuleD = etats['etat_D']['nb_objets'] * etats['etat_D']['transitions']['D'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['D']

    formuleC = etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['C'] + etats['etat_D']['nb_objets'] * etats['etat_D']['transitions']['C']
 
    D=formuleD
    C=formuleC
    
    print('Cycle 1 :')
    print('D : ',D)
    print('C : ',C)
    nb=2

    while(nb<=iteration):
        formuleD = D * etats['etat_D']['transitions']['D'] + C * etats['etat_C']['transitions']['D']

        formuleC = C * etats['etat_C']['transitions']['C'] + D * etats['etat_D']['transitions']['C']
 
        D=formuleD
        C=formuleC
    
        print ('Cycle n°',nb,' :')
        print('D : ',D)
        print('C : ',C)
    
        nb=nb+1
    
def formuleB1(iteration):
    formuleA = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['A'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['A']

    formuleC = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['C'] + etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['C']

    formuleE = etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['E'] + etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['E']
    
    formuleV = etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['V'] + etats['etat_V']['nb_objets'] * etats['etat_V']['transitions']['V']
    

    A=formuleA
    C=formuleC
    E=formuleE
    V=formuleV
    
    print('Cycle 1 :')
    print('A : ',A)
    print('C : ',C)
    print('E : ',E)
    print('V : ',V)
    nb=2

    while((nb)<=iteration):
        formuleA = A * etats['etat_A']['transitions']['A'] + C * etats['etat_C']['transitions']['A']
        formuleC = A * etats['etat_A']['transitions']['C'] + E * etats['etat_E']['transitions']['C']
        formuleE = C * etats['etat_C']['transitions']['E'] + E * etats['etat_E']['transitions']['E']
        formuleV = E * etats['etat_E']['transitions']['V'] + V * etats['etat_V']['transitions']['V']
    

        A=formuleA
        C=formuleC
        E=formuleE
        V=formuleV

        print ('Cycle n°',nb,' :')
        print('A : ',A)
        print('C : ',C)
        print('E : ',E)
        print('V : ',V)
    
        nb=nb+1
    
def formuleB2(iteration):
    formuleB = etats['etat_N']['nb_objets'] * etats['etat_N']['transitions']['B']

    formuleN = etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['N']+ etats['etat_G']['nb_objets'] * etats['etat_G']['transitions']['N']

    formuleG = etats['etat_P']['nb_objets'] * etats['etat_P']['transitions']['G'] + etats['etat_N']['nb_objets'] * etats['etat_N']['transitions']['G']

    formuleP = etats['etat_G']['nb_objets'] * etats['etat_G']['transitions']['N']

    B=formuleB
    N=formuleN
    G=formuleG
    P=formuleP
    
    print('Cycle 1 :')
    print('B : ',B)
    print('N : ',N)
    print('G : ',G)
    print('P : ',P)
    nb=2

    while(nb<=iteration):
        formuleB = N * etats['etat_N']['transitions']['B']

        formuleN = B * etats['etat_B']['transitions']['N'] + G * etats['etat_G']['transitions']['N']

        formuleG = P * etats['etat_P']['transitions']['G'] + N * etats['etat_N']['transitions']['G']

        formuleP = G * etats['etat_G']['transitions']['N']

        B=formuleB
        N=formuleN
        G=formuleG
        P=formuleP
    
        print ('Cycle n°',nb,' :')
        print('B : ',B)
        print('N : ',N)
        print('G : ',G)
        print('P : ',P)
    
        nb=nb+1

def formuleB3(iteration):
    formuleN = etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['N']+ etats['etat_O']['nb_objets'] * etats['etat_O']['transitions']['N']

    formuleS = etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['S'] + etats['etat_O']['nb_objets'] * etats['etat_O']['transitions']['S']

    formuleE = etats['etat_N']['nb_objets'] * etats['etat_N']['transitions']['E'] + etats['etat_S']['nb_objets'] * etats['etat_S']['transitions']['E']

    formuleO = etats['etat_N']['nb_objets'] * etats['etat_N']['transitions']['O'] + etats['etat_S']['nb_objets'] * etats['etat_S']['transitions']['O']

    N=formuleN
    S=formuleS
    E=formuleE
    O=formuleO
    
    print('Cycle 1 :')
    print('N : ',N)
    print('S : ',S)
    print('E : ',E)
    print('O : ',O)
    nb=2

    while(nb<=iteration):
        formuleN = E * etats['etat_E']['transitions']['N']+ O * etats['etat_O']['transitions']['N']

        formuleS = E * etats['etat_E']['transitions']['S'] + O * etats['etat_O']['transitions']['S']

        formuleE = N * etats['etat_N']['transitions']['E'] + S * etats['etat_S']['transitions']['E']

        formuleO = N * etats['etat_N']['transitions']['O'] + S * etats['etat_S']['transitions']['O']

        N=formuleN
        S=formuleS
        E=formuleE
        O=formuleO

        print ('Cycle n°',nb,' :')
        print('N : ',N)
        print('S : ',S)
        print('E : ',E)
        print('O : ',O)
    
        nb=nb+1

def formuleB4(iteration):
    formuleA = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['A'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['A'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['A']

    formuleB = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['B'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['B'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['B']

    formuleC = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['C'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['C'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['C']

    formuleP = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['P'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['P'] + etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['P'] + etats['etat_P']['nb_objets'] * etats['etat_P']['transitions']['P']

    A=formuleA
    B=formuleB
    C=formuleC
    P=formuleP
    
    print('Cycle 1 :')
    print('A : ',A)
    print('B : ',B)
    print('C : ',C)
    print('P : ',P)
    nb=2

    while(nb<=iteration):
        formuleA = A * etats['etat_A']['transitions']['A'] + B * etats['etat_B']['transitions']['A'] + C * etats['etat_C']['transitions']['A']

        formuleB = A * etats['etat_A']['transitions']['B'] + B * etats['etat_B']['transitions']['B'] + C * etats['etat_C']['transitions']['B']

        formuleC = A * etats['etat_A']['transitions']['C'] + B * etats['etat_B']['transitions']['C'] + C * etats['etat_C']['transitions']['C']
        
        formuleP = A * etats['etat_A']['transitions']['P'] + B * etats['etat_B']['transitions']['P'] + C * etats['etat_C']['transitions']['P'] + P * etats['etat_P']['transitions']['P']

        A=formuleA
        B=formuleB
        C=formuleC
        P=formuleP

        print ('Cycle n°',nb,' :')
        print('A : ',A)
        print('B : ',B)
        print('C : ',C)
        print('P : ',P)
    
        nb=nb+1
    
def formuleB5(iteration):
    formuleA = etats['etat_H']['nb_objets'] * etats['etat_H']['transitions']['A']

    formuleB = etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['B'] + etats['etat_G']['nb_objets'] * etats['etat_G']['transitions']['B']

    formuleC = etats['etat_H']['nb_objets'] * etats['etat_H']['transitions']['C']

    formuleD = etats['etat_F']['nb_objets'] * etats['etat_F']['transitions']['D'] + etats['etat_J']['nb_objets'] * etats['etat_J']['transitions']['D']

    formuleE = etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['E'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['E'] + etats['etat_I']['nb_objets'] * etats['etat_I']['transitions']['E']

    formuleF = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['F'] + etats['etat_D']['nb_objets'] * etats['etat_D']['transitions']['F'] + etats['etat_J']['nb_objets'] * etats['etat_J']['transitions']['F']

    formuleG = etats['etat_A']['nb_objets'] * etats['etat_A']['transitions']['G'] + etats['etat_B']['nb_objets'] * etats['etat_B']['transitions']['G'] + etats['etat_I']['nb_objets'] * etats['etat_I']['transitions']['G']

    formuleH = etats['etat_C']['nb_objets'] * etats['etat_C']['transitions']['H']

    formuleI = etats['etat_E']['nb_objets'] * etats['etat_E']['transitions']['I'] + etats['etat_G']['nb_objets'] * etats['etat_G']['transitions']['I']

    formuleJ = etats['etat_D']['nb_objets'] * etats['etat_D']['transitions']['J'] + etats['etat_F']['nb_objets'] * etats['etat_F']['transitions']['J']

    A=formuleA
    B=formuleB
    C=formuleC
    D=formuleD
    E=formuleE
    F=formuleF
    G=formuleG
    H=formuleH
    I=formuleI
    J=formuleJ
    
    print('Cycle 1 :')
    print('A : ',A)
    print('B : ',B)
    print('C : ',C)
    print('D : ',D)
    print('E : ',E)
    print('F : ',F)
    print('G : ',G)
    print('H : ',H)
    print('I : ',I)
    print('J : ',J)
    nb=2

    while(nb<=iteration):
        formuleA = H * etats['etat_H']['transitions']['A']

        formuleB = E * etats['etat_E']['transitions']['B'] + G * etats['etat_G']['transitions']['B']

        formuleC = H * etats['etat_H']['transitions']['C']

        formuleD = F * etats['etat_F']['transitions']['D'] + J * etats['etat_J']['transitions']['D']

        formuleE = C * etats['etat_C']['transitions']['E'] + B * etats['etat_B']['transitions']['E'] + I * etats['etat_I']['transitions']['E']

        formuleF = A * etats['etat_A']['transitions']['F'] + D * etats['etat_D']['transitions']['F'] + J * etats['etat_J']['transitions']['F']

        formuleG = A * etats['etat_A']['transitions']['G'] + B * etats['etat_B']['transitions']['G'] + I * etats['etat_I']['transitions']['G']

        formuleH = C * etats['etat_C']['transitions']['H']

        formuleI = E * etats['etat_E']['transitions']['I'] + G * etats['etat_G']['transitions']['I']

        formuleJ = D * etats['etat_D']['transitions']['J'] + F * etats['etat_F']['transitions']['J']

        A=formuleA
        B=formuleB
        C=formuleC
        D=formuleD
        E=formuleE
        F=formuleF
        G=formuleG
        H=formuleH
        I=formuleI
        J=formuleJ
        print ('Cycle n°',nb,' :')
        print('A : ',A)
        print('B : ',B)
        print('C : ',C)
        print('D : ',D)
        print('E : ',E)
        print('F : ',F)
        print('G : ',G)
        print('H : ',H)
        print('I : ',I)
        print('J : ',J)
    
        nb=nb+1


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

    print("Exercice choisis : %s\n"% exo)
    print('Nombre d\'états différents : %d\n'%data[exo]['nombre_etats'])
    
    for cle, etat in etats.items():
        print(' ', cle, ' = ', etat['nom_complet'])
        print('     Transitions possibles :')
        for trans, valeur in etat['transitions'].items():
            print('      ->', trans, ' : ', valeur)

    iteration = int( input('Combien d\'itération? '))

    if (exo=='C1'):
        formuleC1(iteration)
    if(exo=='C2'):
        formuleC2(iteration)
    if(exo=='C3'):
        formuleC3(iteration)
    if(exo=='C4'):
        formuleC4(iteration)
    if(exo=='C5'):
        formuleC5(iteration)
    if(exo=='C6'):
        formuleC6(iteration)
    if (exo=='B1'):
        formuleB1(iteration)
    if(exo=='B2'):
        formuleB2(iteration)
    if(exo=='B3'):
        formuleB3(iteration)
    if(exo=='B4'):
        formuleB4(iteration)
    if(exo=='B5'):
        formuleB5(iteration)
