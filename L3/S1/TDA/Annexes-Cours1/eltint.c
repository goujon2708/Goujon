/*****************************************************************
*		Fichier :  	ELTINT.C
*		Format :	Source C 
*		Version  : 	19/9/96
*		Programmeurs :	Delozanne, Jacoboni , Futtersack
*		Contenu :      	Définition des primitives pour une réalisatioon
*				par des entiers du TDA ELEMENT.
*		
******************************************************************/

/* définition des primitives du type concret ELEMENT entier */

#include "eltprim.h"
#include <stdio.h>

#define ELEMENT_VIDE 32767

void ElementLire(ELEMENT * i)	{
        printf(" un entier svp :") ;
	scanf("%d",i);
}

void ElementAfficher(ELEMENT elt)	{
	printf(" %d  ",elt);
}

ELEMENT ElementAffecter(ELEMENT * e1, ELEMENT e2)   {
	return  *e1 = e2  ;
}

bool ElementIdentique(ELEMENT e1, ELEMENT e2)  {
	/* retourne vrai si les deux arguments sont identiques */
	return 	e1 == e2 ;
}
ELEMENT ElementCreer (void) {
	return ELEMENT_VIDE ;
}
void   ElementDetruire (ELEMENT elt) {
	/* ne fait rien en stockage direct*/
}
