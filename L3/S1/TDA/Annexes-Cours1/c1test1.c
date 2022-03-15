/*****************************************************************
*		Fichier :  	c1test1.C
*		Format :	Source C 
*		Version  : 	19/9/96
*		Programmeurs :	Delozanne, Jacoboni
*		Contenu :      	Test du TDA LISTE
*		
******************************************************************/

/* programme de test des opérations du TDA LISTE du cours N°1 */

/* test de la réalisation du TDA liste  */
/* les éléments sont ici des entiers  stockage direct */
/* stockage indirect à tester Cf. TD2 et TP1 */

#include <stdio.h>
#include <stdlib.h>
#include "c1lstop.h"
#include "eltprim.h"
#include "lstprim.h"

int main( int nb_arg , char * tab_arg[] )	{
	LISTE L= ListeCreer(), L1= ListeCreer();
	ELEMENT elt;
	POSITION p;
	int i, n , nb_elem ;

	if( nb_arg != 2 )	{
	     fprintf( stderr, "Programme de test du TDA LISTE\n" );
	     fprintf( stderr, "Usage : %s <nombre d'elements> dans la liste\n", tab_arg[0] );

	     exit(-1);
	}

	sscanf( tab_arg[1] , "%d" , &nb_elem );

	/* saisir une liste de nb_elem élements*/
	printf ("\n Entrez une liste de %d entiers svp : \n", nb_elem ) ;

	p = ListePremier(L);

	for (i = 0; i < nb_elem  ; i++ ) 	{
		elt = ElementCreer() ;
		ElementLire(&elt) ;
		ListeInserer(elt, p, L);
		p = ListeSuivant(p, L);
	};

	ListeAfficher(L);
	ListePurger (L1, L);
	printf ("\n Après une petite purge : \n") ;
        ListeAfficher(L1);

	printf( "Affichage des positions\n");
	p = ListeSentinelle(L);
	for (i = nb_elem; i > 0  ; i--) 	{
		p = ListePrecedent(p, L);
		printf ("position : %lu ", p) ;
		printf ("element  : ") ;
		ElementAfficher(ListeAcceder(p, L) ) ;
		printf ("\n") ; 
	};

	ListeDetruire(L);
 	ListeNettoyer(L1);


	printf("\ntout va bien\n") ;

	exit(0) ;
}

