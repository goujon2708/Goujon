/*****************************************************************
*		Fichier :  	C1LSTOP.C
*		Format :	Source C 
*		Version  : 	27/9/95
*		Programmeurs :	Futtersack, Delozanne, Jacoboni, Leroux
*		Contenu :      définitions des opérations classiques étudiées au cours n°1
*		sur les listes à l'aide des opérations primitives du TDA liste
******************************************************************/

#include "c1lstop.h"
#include <stdio.h>

void ListeAfficher(LISTE L) {
	POSITION p = ListePremier(L), fin = ListeSentinelle(L);
		printf("\n(");
		while(p!= fin) {
			ElementAfficher(ListeAcceder(p, L));
			p = ListeSuivant(p, L);
		}
		printf(")\n");
}

POSITION ListePrecedent (POSITION p, LISTE L) {
	POSITION avant, courant, fin ;
	avant = ListePremier (L) ;
	courant = ListeSuivant (avant, L) ;
	fin = ListeSentinelle(L) ;

	for(;p !=courant && courant !=fin; avant=courant, courant=ListeSuivant(courant,L));
	return (courant == p ? avant : fin);
}

POSITION ListeLocaliser (ELEMENT x, LISTE L) {
	POSITION p, fin ;
	p = ListePremier (L) ;
	fin = ListeSentinelle(L) ;

	for (; p != fin && !ElementIdentique(x, ListeAcceder(p, L)) ;)
		p = ListeSuivant (p,L) ;
	return p ;
}


LISTE ListePurger (LISTE L, LISTE LL ) {
	ELEMENT x ;
	POSITION p, q, fin ;

	fin = ListeSentinelle (LL) ;
	p = ListePremier (LL); q =  ListePremier (L);
	for ( ; p != fin ; p = ListeSuivant(p, LL) ){
	     	ElementAffecter(&x, ListeAcceder(p, LL));
		if (ListeLocaliser(x,L) == ListeSentinelle(L)) {
			ListeInserer (x, q, L) ;
			q = ListeSuivant(q, L);
			}
		 }
	return L ;
}
void ListeRaz (LISTE L)	{                 /* en o(n) */
	POSITION p= ListePremier(L);
	while(ListeSuivant(p, L)) ListeSupprimer(p, L);
}

void ListeNettoyer (LISTE L)	{                 /* en o(n) */
	POSITION p = ListePremier(L);
        ELEMENT elt ;
	while(! ListeVide(L))    {
		ElementAffecter(&elt, ListeAcceder(p, L)) ;
                ElementDetruire(elt) ;
		ListeSupprimer(p, L);
		}
	ListeDetruire(L) ;      /* equivaut à free(L)*/
}
