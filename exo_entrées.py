data = {
    'C1' : {
        'nombre_etats' : 3 ,
        'nombre_transition' : 6 ,
        'nombre_objets_total' : 1 ,

        'etat_A' : {
            'nom_complet' : 'Atelier' ,
            'nb_objets' : 1 ,
            'transitions' : {
                'C' : 0.85,
                'A' : 0.15,
            },
        } ,
        'etat_C' : {
            'nom_complet' : 'Controle qualité' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'E' : 0.95,
                'A' : 0.05,
            },
        } ,
        'etat_E' : {
            'nom_complet' : 'Entrepot' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'E' : 0.99,
                'C' : 0.01,
            },
        },
    },
    'C2' : {
        'nombre_etats' : 3 ,
        'nombre_transition' : 7 ,
        'nombre_objets_total' : 1 ,
        'etat_B' : {
            'nom_complet' : 'Beau' ,
            'nb_objets' : 1 ,
            'transitions' : {
                'B' : 0.70,
                'N' : 0.30,
            },
        } 
        'etat_N' : {
            'nom_complet' : 'Nuage' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'B' : (1/3),
                'N' : (1/3),
                'P' : (1/3),
            },
        } 
        'etat_P' : {
            'nom_complet' : 'Pluie' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'P' : 0.10
                'N' : 0.90,
            },
        },
    },
    'C3' : {
        'nombre_etats' : 4 ,
        'nombre_transition' : 9 ,
        'nombre_objets_total' : 1 ,
        'etat_N' : {
            'nom_complet' : 'Nord' ,
            'nb_objets' : 1 ,
            'transitions' : {
                'N' : (1/3),
                'E' : (1/3),
                'O' : (1/3),
            },
        } 
        'etat_S' : {
            'nom_complet' : 'Sud' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'E' : 0.5,
                'O' : 0.5,
            }
        } 
        'etat_E' : {
            'nom_complet' : 'Est' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'N' : 0.5,
                'S' : 0.5,
            }
        } 
        'etat_O' : {
            'nom_complet' : 'Ouest' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'N' : 0.5,
                'S' : 0.5,
            }
        } 
    },
    'C4' : {
        'nombre_etats' : 3 ,
        'nombre_transition' : 9 ,
        'nombre_objets_total' : 150 ,
        'etat_A' : {
            'nom_complet' : 'Fourmilière_A' ,
            'nb_objets' : 50 ,
            'transitions' : {
                'A' : 0.5,
                'B' : 0.3,
                'C' : 0.2,
            },
        }, 
        'etat_B' : {
            'nom_complet' : 'Fourmilière_B' ,
            'nb_objets' : 50 ,
            'transitions' : {
                'A' : 0.2,
                'B' : 0.6,
                'C' : 0.2,
            },
        }, 
        'etat_C' : {
            'nom_complet' : 'Fourmilière_C' ,
            'nb_objets' : 50 ,
            'transitions' : {
                'A' : 0.4,
                'B' : 0.4,
                'C' : 0.2,
            },
        }, 
    },

    'C5' : {
        'nombre_etats' : 5 ,
        'nombre_transition' : 10 ,
        'nombre_objets_total' : 1 ,
        'etat_A' : {
            'nom_complet' : 'Alice' ,
            'nb_objets' : 1 ,
            'transitions' : {
                'B' : 0.4,
                'C' : 0.6,
            },
        }, 
        'etat_B' : {
            'nom_complet' : 'Bertrand' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'C' : 0.4,
                'D' : 0.6,
            },
        }, 
        'etat_C' : {
            'nom_complet' : 'Charlotte' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'E' : 0.4,
                'A' : 0.6,
            },
        }, 
        'etat_D' : {
            'nom_complet' : 'Dominique' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'B' : 0.4,
                'E' : 0.6,
            },
        }, 
        'etat_E' : {
            'nom_complet' : 'Etienne' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'C' : 0.4,
                'B' : 0.6,
            },
        }, 
    },
    'C6' : {
        'nombre_etats' : 2 ,
        'nombre_transition' : 4 ,
        'nombre_objets_total' : 1 ,
        'etat_D' : {
            'nom_complet' : 'Dormir' ,
            'nb_objets' : 1 ,
            'transitions' : {
                'D' : 0.7,
                'C' : 0.3,
            },
        },
        'etat_C' : {
            'nom_complet' : 'Chasser' ,
            'nb_objets' : 0 ,
            'transitions' : {
                'D' : 0.9,
                'C' : 0.1,
            },
        }, 
    },
    
}