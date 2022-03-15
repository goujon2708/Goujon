/*****************************************************************
*		Fichier :  	LSTTAB.H
*		Format :	Source C 
*		Version  : 	19/9/96
*		Programmeurs :	Delozanne, Jacoboni , Futtersack
*		Contenu :      	Déclaration de la strucure de données
*				pour réaliser le TDA LISTE PAR TABLEAU
*				(correspondant au cours 1).
*		
******************************************************************/

#ifndef _LSTTAB_H                   /* pour l'inclusion conditionnelle */
#define  _LSTTAB_H


#include "eltprim.h"     /* inclusion du fichier des primitives du TDA ELEMENT*/



/************************************/
/* déclaration de la strucure de données adoptée pour une réalisation par tableau du TDA LISTE
Rappel :
- une liste est un pointeur sur une structure de données fondamentale (SDF)
- si la liste L est vide, le premier élement de la liste est la sentinelle*/

/* une liste est un pointeur sur une structure composée d'un tableau
et du nombre d'élements significatifs du tableau*/

#define LongMax 100	/* longueur maximale d'une liste */

typedef int POSITION ;
	
typedef struct {
	ELEMENT elements[LongMax];       /* tableau automatique */
	int dernier;
} laStruct,*LISTE;



#endif
