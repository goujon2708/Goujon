/*
*   Fichier : HDBn.c
*   Programmeurs, SCHERRER, RICHEFEU
*   Contenu : implémentaiton de la séquence hadamard en C
*
*
*/
#include <stdio.h>
#include <stdlib.h>

#include "hadam.h"


/***************************/
/*** MATRICE DE HADAMARD ***/
/***************************/



void MatriceAfficher( int ** M , int colonnes , int lignes )
{
    int i, j;

    for( i=0 ; i<colonnes ; i++ )
    {
        for( j=0 ; j<lignes ; j++ )
            printf("%3d |", M[i][j]);

        printf("\n");
    }
}


int ** MatriceCreer( int lignes , int colonnes )
{
    int ** M = malloc( lignes * sizeof(* M) ); // allocation mémoire pour le nb de lignes
    int i , j;

    if( M == NULL )
    {
        printf( "Erreur création lignes\n" );
        return 0;
    }

    for( i=0 ; i<lignes ; i++ )
    {
        if( (M[i] = malloc(colonnes * sizeof(** M))) == NULL ) // allocation mémmoire pour le nb de colonnes
        {
            printf( "Erreur création de colonnes\n" );
            return 0;
        }

        for( j=0 ; j<colonnes ; j++ ) // initialisation de toutes les cases à zéro
            M[i][j] = 0;
    }

    return M;

}



void MatriceDetruire( int *** M , int lignes) 
{
    int i; 

    for( i=0 ; i<lignes ; i++ )
        free( (*M)[i] ); 

    free( *M );
}


void HadamardMatrice( int ** M , int a )
{
    int i , j , k;

    M[0][0] = 1; // initialisation de la première case

    for( i=1 ; i<a ; i+=i )
    {
        for( j=0 ; j<i ; j++ )
        {
            for( k=0 ; k<i ; k++ )
            {
                M[i+j][k] = M[j][k];        // Haut à droite
                M[j][k+i] =  M[j][k];       // Bas à gauche
                M[j+i][k+i] = -M[j][k];     // Bas à droite
            }
        }
    }

}



/*****************************/
/*** ETALEMENT DE HADAMARD ***/
/*****************************/



char * MessageSaisir ()
{
    char * s = malloc( sizeof(char) * TAILLE_MSG);

    if( s == NULL )
    {
            printf( "Erreur allocation : saisie du message\n" );
            exit( -1 );
    }
    
    scanf( "%s" , s );

    return s;
}


int MatriceLongueur ( int n )
{
    int l;

    for( l=1 ; l<n ; l *= 2 );

    return l;
}


int * HadamardEtalement(    int nbUser , 
                            int ** seq , 
                            int ** had , 
                            int * l , 
                            int lMax )
{
    int i, j, k;
    int lHad = MatriceLongueur( nbUser );
    int ** tmp = MatriceCreer( nbUser , lHad * lMax );
    int * res = malloc( sizeof(int) * (lHad * lMax)) ;

    if ( res == NULL )
    {
        printf( "Erreur allocation étalement\n" );
        exit(-1);
    }

    /* Codage des messages */
    for(i = 0; i < nbUser; i++) // Parcours nombre utilisateur             
    {  
        for(j = 0; j < l[i]; j++) // Parcours de la séquence de l'utilisateur i          
        {  
            for(k = 0; k < lHad ; k++) // Parcours de la matrice d'Hadamard
            {
                // Rempilssage de la matrice
                if( seq[i][j] == 1 )
                    tmp[i][(j * lHad) + k] = had[i][k];
                else 
                    tmp[i][(j * lHad) + k] = - had[i][k];
            }
        }
    }
    
    MatriceAfficher(tmp, nbUser, (lMax * lHad));
		
	/* Opération d'étalement */
    for( i=0 ; i<( lHad * lMax ) ; i++ )
        for( j=0 ; j<nbUser ; j++ )
            res[i] += tmp[j][i];

    /* Libération de la mémoire */
    MatriceDetruire( &tmp , nbUser );

    return res;
}


void HadamardDesetalament(  int nbUser , 
                            int lMax , 
                            int ** seq , 
                            int ** had , 
                            int * sortie , 
                            int lHad )
{
    int i , j , k;

    for( i=0 ; i<nbUser ; i++ ) // parcours du nombre d'utilisateur
    {                
        for( j=0 ; j<lMax ; j++ ) // parcours de la plus grande séquence
        {         
            for( k=0 ; k<lHad ; k++ )
                seq[i][j] += sortie[k + lHad * j] * had[i][k];

            seq[i][j] /= lHad;

            if( seq[i][j] == -1 )
                seq[i][j] = 0;
            
            else    
                seq[i][j] = 1;
        }
    }
}


