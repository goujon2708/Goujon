#include <stdio.h>
#include <stdlib.h>
#include "CodeLongMax.h"

#define LSEQ 20
#define T_TAB 100


void JPL( int *reg[] , int lengthReg[] , int *generation[] , int prime[] , int nbEncdr , int jpl[] , int lengthSeq[] )
{
	int *ml[nbEncdr];
	int l = 1;  // Longueur de la séquence
	int i, j, k;

    /* Taille de la séquence */
    for(i = 0; i < nbEncdr; i++)
        l *= lengthSeq[1 + i];


    /* Allocation de la mémoire */
    for(i = 0; i < nbEncdr; i++ )
		ml[i] = malloc(sizeof(int) * l);


    // /* Code Longueur Max de chaque séquence */
  //   for(i = 0; i < nbEncdr; i++)
  //       CodeLongMax( reg[i] , generation[i] , lengthReg[i] , prime[i] , lengthSeq[1 + i] , ml[i] );




    /* Copie des séquence généré + Affichage */
    for( i=0 ; i<nbEncdr ; i++ )
	{
        for( j=0 ; j<l ; j += lengthSeq[1 + i] )
		{
            for( k=0 ; k < lengthSeq[1 + i] ; k++ )
			{
                ml[i][j + k] = ml[i][k];
                printf( "%d" , ml[i][j + k] );
            }
        }
		
		printf("\n");
    }


    /* Calcul JPL */
    for(i = 0; i < l; i++)
	{
        jpl[i] = ml[0][i];
		
        for( j=1 ; j < nbEncdr ; j++ )
            jpl[i] ^= ml[j][i]; // XOR
    }

    /* Affichage */
 	printf("\n");
	
	for( i=0 ; i<l ; i++ ) 
		printf( "%d" , jpl[i] );
	
    printf("\n");
}


void test_jpl()
{
    printf("\n\n######### JPL #########\n\n");
	
	
    int arr[T_TAB], prime[T_TAB], jpl[T_TAB];
    int j , k , i;
    int n = 50, tmp = 0;

    /* Registre */
    int R1[5] = { 1 , 1 , 1 , 1 , 1 } , 
		R2[5] = { 1 , 1 , 1 , 1 , 1 } , 
		R3[6] = { 1 , 1 , 1 , 1 , 1 , 1 };
		
    int *reg[3] =  { R1 ,R2 ,R3 };
    int lengthReg[3] = { 5 , 5 , 6 };

    /* Génération */
    int G1[2] = { 5 , 2 } , 
		G2[4] = { 5 , 4 , 2 , 1 } , 
		G3[4] = { 5 , 4 , 2 , 1 };
		
    int *gen[3] = { G1, G2, G3 }; 
    int lengthGen[3] = { 2 , 4 , 4 };

	for (i = 1; i < n; i++)
	{
		tmp++;
		arr[i] = tmp;
	}

	prime[0] = 2;
	for(i = 0; i < n; i += 2)
		arr[i] = 0;

	prime[1] = 3;
	for (i = 0; i < n; i += 3)
		arr[i] = 0;

	i = 4; j = 2;
	while ( i++ < n )
	{
		while ( arr[i] != 0 )
		{
			prime[j++] = arr[i];
			tmp = arr[i];
			
			for( k=0 ; k<=n ; k+=tmp ) 
            	arr[k] = 0;
		}
	}
    JPL( reg , lengthReg , gen , lengthGen , 3 , jpl , prime );
}