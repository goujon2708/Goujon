/******************************************************************
*		Fichier :  	FILTABCI.H
*		Format :	Source C 
*		Version  : 	21/9/96
*		Programmeurs :	Delozanne/Jacoboni
*		Contenu :      	Déclaration de la struture de données
*				pour une réalisation du TDA FILE par tableau circulaire.
*		
******************************************************************/


/* Réalisation du TDA FILE par tableau circulaire

    Un objet file est un pointeur sur une structure qui contient
    * l'indice courant du début de la file
    * l'indice courant de la fin de la file
    * la taille maximale de la file, spécifiée par la primitive de création de pile
    * un pointeur vers une zone de taille : taille maximum *(sizeof(ELEMENT)) octets
    qui contient les éléments de la file
    
*/
#ifndef FILTABCI_H
#define FILTABCI_H


typedef struct {
 	ELEMENT *elements ;
	int debut ;
        int fin ;
 	int longMax ;
 } file,	*FFILE ;
 

#endif





