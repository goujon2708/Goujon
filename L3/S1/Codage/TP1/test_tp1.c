/*
*   Fichier : test_tp1.c
*   Programmeurs, SCHERRER, RICHEFEU
*   Contenu :   fichier test des différents codages implémentés durant le TP
*
*
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "hadam.h"


int main ()
{
    int ** had , ** msg , ** msgReponse;
    int * etalement , *l;
    int i , j , lHad , lMax , nb_user , num_canal;
    char * s; // chaine des msg

    printf("---- TP1 ---- \n#### Tests sur la séquence d'HADAMARD ####\n\n");

    // Saisie du nb d'utilisateurs
    do
    {
        printf("Saisir le nb d'utilisateur(s) (1, 2, 4, 8 ou 16) : ");
        scanf("%d", &nb_user);

    }while ( nb_user != 1 && nb_user != 2 && nb_user != 4 && nb_user != 8 && nb_user != 16 );


    do
    {
        printf( "Saisissez le numéro du canal sur lequel vous voulez émettre : " );
        scanf( "%d" , &num_canal );
        
    }while( num_canal < 1 || num_canal >= nb_user );

    // Création des matrices qui vont stocker les messages
    msg = MatriceCreer( nb_user , TAILLE_MSG );
    msgReponse = MatriceCreer( nb_user , TAILLE_MSG );

    // Création de la matrice 
    lHad = MatriceLongueur ( nb_user ); // calcul de la longueur
    had = MatriceCreer( lHad , lHad );

    // remplissage de la matrice
    HadamardMatrice( had , lHad );


    // Saisie du message et remplissage des séquences 

    l = malloc( sizeof(int) * nb_user ); 
    for( i=0 ; i<nb_user ; i++ )
    {
        printf( "Saisir un message : " );
        s = MessageSaisir();

        for(j = 0; j < strlen(s); j++)
        {
            msg[i][j] = s[j] - '0';
            l[i] = strlen(s);
        } 
    }


    // Recherche de la séquence la plus longue 
    for (i = 0; i < nb_user ; i++)
        if( l[i] > lMax ) 
            lMax = l[i];



    /****************************/
    /**** TEST DES FONCTIONS ****/
    /****************************/

    printf( "\n##### Matrice de Hadamard\n\n" );
    MatriceAfficher( had , lHad , lHad );


    printf( "\n##### Etalement #####\n\n" );
    etalement = HadamardEtalement (nb_user , msg , had , l , lMax );
	

    printf( "\n##### Affichage résultat étalement ##### \n\n" );
	for( i=0 ; i<(lHad * lMax) ; i++ ) 
        printf( "%2d|", etalement[i] );
    printf("\n\n");


    printf( "\n##### Désetalement #####\n\n" );
    HadamardDesetalament( nb_user , lMax , msgReponse , had , etalement , lHad );
    MatriceAfficher( msgReponse , nb_user , lMax );


    // libération de mémoire
    free(s);
    free(l);
    free(etalement);

    MatriceDetruire( &msg , nb_user );
    MatriceDetruire( &msgReponse , nb_user );
    MatriceDetruire( &had , lHad );
}