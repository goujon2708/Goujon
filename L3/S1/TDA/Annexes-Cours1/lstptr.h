/*****************************************************************
*		Fichier :  	LSTPTR.H
*		Format :	Source C 
*		Version  : 	21/9/95
*		Programmeurs :	Delozanne, Jacoboni  , Futtersack
*		Contenu :      	Déclaration de la strucure de donée choisie du TDA LISTE par liste chainée
*				avec en-tête.
*		ici une liste est un pointeur sur la cellule en-tête
*		une position est un pointeur sur une cellulle
******************************************************************/

#ifndef _LSTPTR_H                   /* pour l'inclusion conditionnelle */
#define  _LSTPTR_H

/*////////////////////////////////////////////////////////////////////
RAPPEL :
- une cellule est une structure à deux champs
	un ELEMENT
	un pointeur sur la cellule suivant (ou NULL s'il n'y a pas de suivante)
- en stockage indirect un élément est un pointeur sur un objet pointé (un pointeur sur une SDF)
 en stockage direct un élément est l'objet stocké
- la position d'un element de la liste est un pointeur sur la cellule PRECEDENT la cellule contenant l'element.
- la position du premier element est un pointeur sur la cellule d'en-tete.
- la position retournee par ListeSentinelle(L) est donc sur la dernière cellule de la liste
- la position  retournee par ListeSentinelle(L) = Premier(L) quand L est vide
////////////////////////////////////////////////////////////////////*/


#include "eltprim.h"

/************************************/
/* Déclaration de la structure de données adoptée
pour la réalisation du type concret de données LISTE */

typedef struct cell{
	ELEMENT element;
	struct cell * suivant;
	} cellule, *LISTE;
	
typedef LISTE POSITION; 



#endif
