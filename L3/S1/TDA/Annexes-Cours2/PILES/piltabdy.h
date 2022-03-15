/******************************************************************
*		Fichier :  	PILTABDYN.H
*		Format :	Source C 
*		Version  : 	21/9/96
*		Programmeurs :	Delozanne/Jacoboni , Futtersack
*		Contenu :      	Déclaration de la structure de données pour une
*				réalisation du TDA PILE par tableau alloué dynamiquement.
*		
******************************************************************/

#ifndef PILTABDYN_H
#define PILTABDYN_H     /* pour inclusion conditionnelle */

/* Implantation du TDA PILE par tableau dynamique
Structure de donnée retenue :
    Un objet pile est un pointeur sur une structure qui contient
    * l'indice courant du sommet
    * la profondeur maximale de la pile, spécifiée par la primitive de création de pile
    * un pointeur vers une zone mémoire allouée dynamiquement de taille : profondeur*(sizeof(ELEMENT)) octets
    qui contient les éléments de la pile   
*/

typedef struct {
 	ELEMENT *elements ;
 	int sommet ;
 	int profMax ;
 } pile,	*PILE ;
 
#endif
