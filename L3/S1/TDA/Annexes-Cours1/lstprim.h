/*****************************************************************
* Fichier :  	LSTPRIM.H
*		Format :	Source C 
*		Version  : 	19/9/96
*		Programmeurs :	Delozanne, Jacoboni , Futtersack
*		Contenu :      	Déclaration des primitives du TDA LISTE
*				(correspondant au cours 1).
******************************************************************/
#ifndef _LSTPRIM_H                   	/* pour l'inclusion conditionnelle */
#define  _LSTPRIM_H

#include "eltprim.h" 			/* le TDA Liste utilise le TDA ELEMENT */

#include "lstsdd.h"     		/* inclusion du fichier où est indiquée la structure de donnée retenue pour réaliser le TDA LISTE

/************************************/
/* Déclaration des primitives du TDA LISTE*/

/* primitive de test */

	/* teste si la liste est vide */
    bool ListeVide (LISTE);

/* primitives d'accès */

    /* accès aux éléments */
	/*retourne l'élément à la position p dans la liste, sans modifier la liste
	retourne l'élément vide si la liste est vide ou si la position est mauvaise */
    ELEMENT ListeAcceder(POSITION,LISTE);

    /* accès aux positions */
	/* retourne la position qui suit la position du dernier élément de la liste*/
    POSITION ListeSentinelle(LISTE);

	/* retourne la première position de la liste si la liste est non vide
	ou ListeSentinelle */
    POSITION ListePremier(LISTE);

POSITION ListeSuivant(POSITION,LISTE);
	/* retourne la position qui suit la position paramètre dans la liste si la liste est non vide
	ou ListeSentinelle */

/* primitives de modification de la liste */
bool ListeInserer (ELEMENT,POSITION,LISTE);
	/* modifie la liste en insérant l'élément à la position ;
	retourne faux si la liste est pleine ou si la position est mauvaise */
bool ListeSupprimer (POSITION, LISTE);
	/*  supprime de la liste l'élément dont la position est passée en paramètre ;
	retourne faux si la liste est vide */


/* primitives de création et de destruction */
LISTE ListeCreer(void);
	/* crée et retourne une liste vide en lui allouant de la mémoire dynamique*/
void ListeDetruire(LISTE);
	/* libére la mémoire dynamique allouée pour la liste */


#endif
