
/*****************************************************************
* Fichier :  	C1LSTOP.H
*		Format :	Source C 
*		Version  : 	27/9/95
*		Programmeurs :	Delozanne, Jacoboni, Leroux
*		Contenu :      déclarations des opérations classiques étudiées au cours N°1
*		sur les listes 
******************************************************************/

#ifndef _C1LSTOP_H                   /* pour l'inclusion conditionnelle */
#define _C1LSTOP_H


#include "lstprim.h"

/*  opérations d'affichage */

void ListeAfficher(LISTE L) ;
	/* affiche un par un les élements de la liste L */
	/* remarque le type Element doit posséder une fonction d'affichage */


/* opérations d'accès aux positions */

POSITION ListePrecedent (POSITION p, LISTE L) ;
	/*retourne la position précédent p dans L si elle existe, sinon retourne la sentinelle */

POSITION ListeLocaliser (ELEMENT x, LISTE L);
	/* retourne la premiere position de x dans L ou la sentinelle */


/* opérations de modification */

LISTE ListePurger (LISTE L, LISTE LL) ;
	/* retourne dans L une copie de LL d'où toutes les répétitions sont éliminées
	L doit être une liste vide, sinon il faut disposer d'une opération qui permet de la vider(ListeRaz)*/

void ListeRaz(LISTE L) ;
	/* vide la liste : i.e. la transforme en liste vide mais sans changer son adresse
	cette primitive est utile pour sécuriser certaines opérations Cf. TD2  et fichierlistop.c */


/* gestion de mémoire */

void ListeNettoyer(LISTE L);
	/* utilisation : uniquement en stockage indirect pour une liste propriétaire de son contenu
	libère la mémoire dynamique allouée pour les éléments pointés et pour la liste
	ATTENTION : cette primitive pour fonctionner correctement suppose que le paramètre ne contient pas deux fois le même élément
	dans le doute il pourrait être prudent de faire une petite purge (Cf. les opérations sur les listes */

#endif
