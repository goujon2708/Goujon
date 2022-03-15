/************  FICHIER  Testpile.C  **************/
/* programme de test, cours N °2, sur les piles
 */

#include "pileprim.h"
#include <stdio.h>

int main()
{
	int i ;
	PILE P = PileCreer(5);
	ELEMENT elt ;
	printf ("\nEntrez 4 élements :\n");

	for (i = 1 ; i  < 5 ; i++)	{
        elt = ElementCreer() ; // facultatif stockage direct */
		ElementLire(&elt) ;
		PileEmpiler(elt, P) ;
	};

	printf ("\nVoila toute la pile ;");
	PileAfficher(P) ;
	printf ("\n");

	printf("\n on dépile le sommet :");
	ElementAfficher(PileSommet(P)) ;
	ElementAfficher(PileDepiler(P)) ;
	printf ("\nVoila toute la pile ;");
	PileAfficher(P) ;
	printf ("\n");

	printf("\n on dépile le sommet :");
	ElementAfficher(PileSommet(P)) ;
	ElementAfficher(PileDepiler(P)) ;

	printf ("\nVoila toute la pile ;");
	PileAfficher(P) ;
	printf ("\n");

	printf("\n on dépile le sommet :");
	ElementAfficher(PileSommet(P)) ;
	ElementAfficher(PileDepiler(P)) ;

	printf ("\nVoila toute la pile ;");
	PileAfficher(P) ;
	printf ("\n");

	printf("\n on dépile le sommet :");
	ElementAfficher(PileSommet(P)) ;
	ElementAfficher(PileDepiler(P)) ;

	printf ("\nVoila toute la pile ;");
	PileAfficher(P) ;
	printf ("\n");


       PileDetruire(P) ;
		/* stockage direct pas d'élément à détruire,
		juste la pile à détruire */

       return 0;

}

