/******************************************************************
*		Fichier :  	PILEPRIM.H
*		Format :	Source C 
*		Version  : 	21/9/96
*		Programmeurs :	Delozanne/Jacoboni, Futtersack
*		Contenu :      	Déclaration des primitives du TDA PILE
*
******************************************************************/


/* Indépendant de la réalisation*/
#ifndef PILEPRIM_H
#define PILEPRIM_H

#include "eltprim.h"	/*   le TDA PILE utilise le TDA ELEMENT */

#include "pilesdd.h"    /* inclure le fichier où est déclarée la représentation interne adoptée */

PILE PileCreer (int profondeur) ;
	/* crée et retourne une pile en lui allouant de la mémoire dynamique
	La pile ainsi crée est pour l'instant vide
	Le paramètre entier désigne la profondeur maximale de la pile (pleine)*/
void PileDetruire(PILE);
	/* libére la mémoire allouée dynamiquement pour la pile paramètre*/
bool PileVide(PILE);
	/* teste si la pile est vide */
ELEMENT PileSommet(PILE);
	/* retourne l'element au sommet de la pile (sans le dépiler) */
ELEMENT PileDepiler(PILE);
	/* retourne l'élément au sommet de la pile ET l'enlève de la pile) */
bool PileEmpiler(ELEMENT, PILE);
	/* ajoute l'élément au sommet de la pile */


void PileAfficher (PILE ) ; /* pour test et mise au point */
/* void PileRaz(PILE) ;
void PileNettoyer(PILE) ;  ça peut être utile à faire en exercice */
#endif
