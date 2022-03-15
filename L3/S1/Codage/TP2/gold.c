#include <stdio.h>
#include <stdlib.h>
#include "CodeLongMax.h"
#include "gold.h"

void Gold( int reg1[] , int reg2[] , int lengthReg1 , int lengthReg2 , int generation1[] , int nbXor1 , int generation2[] , int nbXor2 , int gold[] )
{
	int i , j;
	int ml1[LSEQ];
	int ml2[LSEQ];

	// Génération code de Longueur Maximal
	CodeLongMax( reg1 , generation1 , lengthReg1 , nbXor1 , ml1 );
	printf("\n");
	CodeLongMax( reg2 , generation2 , lengthReg2 , nbXor2 , ml2 );
	printf("\n");
	

	// Calcul du décalage(XOR)
	for( i=0 ; i<LSEQ ; i++ )
	    gold[i] = ml1[i] ^ ml2[i];
    

	for( j=0 ; j<LSEQ ; j++ ) 
		printf( "%d %d = %d\n" , ml1[j] , ml2[j] , gold[j] );
		
	printf("\n");
}

void test_gold()
{
	printf("\n\n########### GOLD ###########\n\n");
	
    int r1[5] = { 1 , 1 , 1 , 1 , 1 },    
		r2[5] = { 1 , 1 , 1 , 1 , 1 };
		
    int g1[2] = { 5 , 2 },          
		g2[4] = { 5 , 4 , 3 , 2 };
		
    int gold[LSEQ];

    Gold( r1 , r2 , 5 , 5 , g1 , 2 , g2 , 4 , gold );
    printf( "\n\n" );
}