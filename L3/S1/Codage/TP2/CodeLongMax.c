#include <stdio.h>
#include <stdlib.h>
#include "CodeLongMax.h"

void CodeLongMax( int cour[] , int gen[] , int Lcour , int nbXor , int ML[] )
{
    int i = 1, j, tmp;
	
    ML[0] = cour[Lcour - 1];
	
    //printf("cour[Lcour-1] = %d" , cour[Lcour-1] );
	
	// Affichage première valeur
	for( j=0 ; j<Lcour ; j++ ) 
        printf("%d", cour[j]);

	printf( " ===> %d\n", cour[Lcour - 1] );		
    

    for( i=0 ; i<LSEQ ; i++ ) // Parcours de la séquence
    {       
        tmp = cour[gen[0] - 1]; // MAJ de l'entree

        for( j=1 ; j<nbXor ; j++ )
            tmp ^= cour[gen[j] - 1]; // Décalge à droite avec l'opérateur XOR

        for( j=0 ; j<Lcour ; j++ )
            cour[Lcour - j] = cour[Lcour - j - 1]; // Ajout dans le décaleur de la valeur décalée


       	cour[0] = tmp;
        ML[i] = cour[Lcour - 1];

        // Affichage
        for( j=0 ; j<Lcour ; j++ ) 
            printf( "%d" , cour[j] );	

        printf( " ===> %d\n" , cour[Lcour - 1] );	
	}
}

void test_longMax()
{
	printf( "\n\n##### LONGUEUR MAXIMALE #####\n\n" );

	int i;
	int r[5] = { 1 , 1 , 1 , 1 , 1 };
	int g[2] = {5,2};

	int test[LSEQ];

	CodeLongMax( r , g , 5 , 2 , test );

	printf( "\n" );



	printf( "%2d" , test[0] );
	for( i=0 ; i<LSEQ ; i++ )
		printf( "%2d" , test[i] );

	printf("\n\n");
}
