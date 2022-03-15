#include <stdio.h>
#include <stdlib.h>

#include "CodeLongMax.h"
#include "gold.h"
#include "jpl.h"



int main()
{
	int val;
	
	printf( "\n\n\t\t########## TESTS DES CODES PSUEDOS ALÉATOIRES #########\n\n" );
	printf( "1 : Longueur Maximale\n" );
	printf( "2 : Gold\n" );
	printf( "3 : JPL\n" );
	printf( "0 : Quitter\n\n" );
	
	printf( "Choisir le programme à tester : " ); 
	scanf( "%d" , &val );
	
	switch( val )
	{	
		case 0:
		break;
		
		case 1:
			test_longMax();
			break;
			
		case 2:
			test_gold();
			break;
		
		case 3:
			test_jpl();
			break;
			
		default:
		printf( "Valeur saisie incorrecte\n" );
	}
	
}