/*
********************************************************************
*		Fichier :  	PILTABDY.C
*		Format :	Source C 
*		Version  : 	21/9/96
*		Programmeurs :	Delozanne/Jacoboni, Futtersack
*		Contenu :      	Définition des primitives pour une réalisation du TDA PILE
*				par tableau alloué en mémoire dynamique.
*		
******************************************************************/


/* Réalisation du TDA PILE par tableau dynamique

    Un objet pile est un pointeur sur une structure qui contient
    * l'indice courant du sommet
    * la profondeur maximale de la pile, spécifiée par la primitive de création de pile
    * un pointeur vers une zone de taille : profondeur*(sizeof(ELEMENT)) octets
    qui contient les éléments de la pile
    
Toutes les opérations sont en o(1) (sauf afficher bien évidemment )*/

#include "pileprim.h"
#include <stdlib.h>
#include <stdio.h>

 PILE PileCreer (int profondeur)	{
 /* renvoie l'adresse d'une structure dont le champ éléments est un pointeur sur une 
 zone mémoire de profondeur*taille(ELEMENT) */
 	PILE p;

	p=(PILE)malloc(sizeof(pile));
	if (! p) {
		printf("pb de mémoire") ;
		exit(0) ;
                }
 	p->elements=(ELEMENT *)malloc(profondeur*sizeof(ELEMENT)) ;
 	p->sommet=0	;
 	p->profMax=profondeur	;
 	
 	return(p);
 }
 	
 bool PileVide(PILE P)	{
 	return(P->sommet==0);
 }
 
 ELEMENT PileDepiler(PILE P)	{
	ELEMENT elt ;
 	if (!PileVide(P)) 	{
		ElementAffecter(&elt,(P->elements)[P->sommet]);
 		P->sommet--;
 		return(elt);
 	}
	else return (ElementCreer());
 }
 
bool PileEmpiler(ELEMENT elt, PILE P)	{
 	if(P->sommet < P->profMax)	{
 		(P->sommet)++;
		ElementAffecter(&(P->elements)[P->sommet], elt);
 		return(VRAI);
 	}
 	else {
 		printf("Pile pleine\n");
		return(FAUX);
	}
 }
 
 ELEMENT PileSommet(PILE P)	{
	if (! PileVide(P))
		return( (P->elements)[P->sommet] );
		else return (ElementCreer()) ;
 }
 
 void PileDetruire(PILE P)	{
 	free(P->elements);
 	free(P);
 }

 void PileAfficher (PILE P) {
	int i ;
	for (i = 1 ; i <= P -> sommet; i++)
		ElementAfficher(P -> elements [i]) ;
}
