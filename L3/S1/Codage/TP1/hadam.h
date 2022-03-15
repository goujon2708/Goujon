/*
*   Fichier : hadamard.h
*   Programmeurs, SCHERRER, RICHEFEU
*   Contenu :   contient les différentes variables et fonctions utilisées
*                pour l'implémentation de la séquence hadamard
*
*
*/

#ifndef _HADAM_H                   /* pour l'inclusion conditionnelle */
#define  _HADAM_H

#define TAILLE_MSG 30


void MatriceAfficher( int ** M , int colonnes , int lignes );

int ** MatriceCreer( int lignes , int colonnes );

void MatriceDetruire( int *** M , int lignes) ;

void MatriceHadamard( int ** M , int a );

char * MessageSaisir ();

int MatriceLongueur ( int n );

int * HadamardEtalement(    int nb_user , 
                            int ** seq , 
                            int ** had , 
                            int * l , 
                            int lMax 
                        );


void HadamardDesetalament(  int nb_user , 
                            int lMax , 
                            int ** seq , 
                            int ** had , 
                            int * sortie , 
                            int lHad );








#endif




