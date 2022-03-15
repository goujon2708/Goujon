/*****************************************************************
*		Fichier :  	LISTPTR.C
*		Format :	Source C 
*		Version  : 	19/9/96
*		Programmeurs :	Delozanne, Jacoboni , Futtersack
*		Contenu :      	Implantation des primitives du TDA LISTE par liste chainée
*				avec en-tête.
*		ici une liste est un pointeur sur la cellule en-tête
*		une position est un pointeur sur une cellulle
******************************************************************/


/* remarque :
on ne vérifie pas la validité de la position passée en argument de la fonction.
Cette vérification, en o(n), qui alourdirait considérablement les fonctions primitives
est à la charge du programme appelant
*/

#include "lstprim.h"

#include <stdlib.h>
#include <stdio.h>


/* Implantation des primitives du TAD LISTE*/

LISTE ListeCreer(void)	{
			/*une liste vide est une liste qui ne contient que sa cellule d'en-tete*/
	LISTE L;
	L=(LISTE)malloc(sizeof(cellule));
	if (! L) {
		printf("problème de mémoire");
		exit(0);
		}
	L->suivant=(LISTE)NULL;
	return(L);
}

bool ListeVide(LISTE L) {			/* en o(1) */
	return(!L->suivant? VRAI: FAUX);
}	
	
POSITION ListeSentinelle(LISTE L) {		/* en o(n) */
	POSITION p = L  ;
	while (p->suivant) p = p -> suivant;
	return p ;
}

POSITION ListePremier(LISTE L) {                /* en o(1) */
			/* retourne la position du premier élément ou la sentinelle si L est vide */
	return L;
}

POSITION ListeSuivant(POSITION p,LISTE L){	  /* en o(1) */
	return p -> suivant;
}

bool ListeInserer (ELEMENT x, POSITION p, LISTE L){       /* en o(1) */
		/*insere une nouvelle cellule apres la cellule à la position p ;
		dans le cas où on passe l'argument p = Liste_Sentinelle(L) alors l'insertion se fait en fin de liste */

	cellule * cell;
	cell =(cellule *)malloc(sizeof(cellule));
	if(!cell) return(FAUX)   ;
        else	{
		ElementAffecter(&cell->element, x);
		cell->suivant = p->suivant;
		p->suivant = cell;
		return(VRAI);
	}
}

bool ListeSupprimer (POSITION p, LISTE L){        /* en o(1) */
			/*on dechaine la cellule de position p,c'est-a-dire celle dont l'adresse est
			dans p->suivant,et enfin on detruit la cellule elle-meme
			Remarques :
			1)on ne détruit l'element que dans le cas du stockage direct ;
			dans le cas du stockage indirect, en général cet élément est un pointeur vers un objet
			partagé avec d'autres listes
			2) comportement périlleux si p n'est pas une position valide ; avant de libérer la cellule
			il serait prudent de vérifier mais cela pénalise en efficcacité*/
	cellule *  temp ;
	if (! ListeVide(L)) {
	        temp = p->suivant;
		p->suivant=p->suivant->suivant;
		free(temp);    /*danger si p n'est pas valide*/
		return VRAI;
	}
	else return FAUX ;
}

ELEMENT ListeAcceder(POSITION p, LISTE L) {      /* en o(1) */
	if (! ListeVide(L))
		return  p->suivant->element;
		else return ElementCreer() ;
}

void ListeDetruire(LISTE L)	{                 /* en o(n) */
	if (L->suivant) ListeDetruire(L->suivant);
	free(L);			/*destruction de la cellule d'en-tete*/

}

