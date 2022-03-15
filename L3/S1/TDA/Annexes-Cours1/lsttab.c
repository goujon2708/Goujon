/*****************************************************************
*		Fichier :  	LISTTAB.C
*		Format :	Source C 
*		Version  : 	19/9/96
*		Programmeurs :	Delozanne, Jacoboni   , Futtersack
*		Contenu :      	Définition des primitives pour une réalisatioon
*				par tableau du TDA LISTE.
*		
******************************************************************/



/* définition des primitives du type concret LISTE par tableau*/

#include "lstprim.h"

#include <stdlib.h>
#include <stdio.h>
/* Implantation des primitives du TAD LISTE dans une réalisation par tableau*/

LISTE ListeCreer(void)	{
	LISTE L;
	L=(LISTE)malloc(sizeof(laStruct));
	if(!L) {
		printf("probléme de mémoire") ;
		exit(0) ;
	}
	L->dernier=0;
	return(L);
}

bool ListeVide(LISTE L) {
	return L->dernier ==0;
}	
	
POSITION ListeSentinelle(LISTE L) {
	return(L->dernier+1);
}

POSITION ListePremier(LISTE L) {
/* retourne la position du premier élément ou la sentinelle si L est vide */
	return 1;
}

POSITION ListeSuivant(POSITION p,LISTE L){
	if (p>L->dernier || p<0 ) return(L->dernier+1);
	else return(p+1);
}

bool ListeInserer (ELEMENT x, POSITION p, LISTE L){
	POSITION q;
	if ( (L->dernier<LongMax) && (p<=L->dernier+1)){
		for(q = L->dernier; q>= p; q--)
			ElementAffecter(&L->elements[q+1], L->elements[q]);
		ElementAffecter(&L->elements[p], x);
		(L->dernier)++;
		return(VRAI);
		}
		else return(FAUX);
}

bool ListeSupprimer (POSITION p, LISTE L){
	POSITION q;
	if ( (p>=1) && (p<=L->dernier)){
			for(q=p;q<=L->dernier;q++)
				ElementAffecter(&L->elements[q], L->elements[q+1]);
			(L->dernier)--;
			return(VRAI);
		}
		else return(FAUX);
}

ELEMENT ListeAcceder(POSITION p, LISTE L) {
	if ( (p<=L->dernier) && (p>=1) && (L->dernier!=0) )
	return(L->elements[p]);
	else return(ElementCreer());
}

void ListeDetruire(LISTE L){
	free(L);
}

