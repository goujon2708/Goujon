/************  FICHIER  Testfile.C  **************/
/* programme de test, cours N °2, sur les files */

#include "fileprim.h"
#include <stdio.h>

int main()
{
	
	FFILE P = FileCreer(4);
	ELEMENT elt ;

        printf ("\nVoila la file vide :");
	FileAfficher(P) ;
        printf ("\n");

	printf ("\tet sa représentation interne :");
	FileRadiographier(P) ;       
	printf ("\n");
	getchar() ;

	FileEntrer(1, P) ;
	printf ("\n+++Entrée de 1 \n Voila la file :");
	FileAfficher(P) ;
	printf ("\tet sa représentation interne :");
	FileRadiographier(P) ;
	printf ("\n");

	getchar() ;
	FileEntrer(2, P) ;
	printf ("\n+++Entrée de 2 \n Voila la file :");
	FileAfficher(P) ;	
	printf ("\n");

	printf ("\tet sa représentation interne :");
	FileRadiographier(P) ;
	printf ("\n");

   	getchar() ;

	printf("\n---Sortie de : %d ", FileSortir(P)) ;

       	printf ("\nVoila la file:");
	FileAfficher(P) ;	
	printf ("\n");

	printf ("\tet sa représentation interne :");
	FileRadiographier(P) ;
	printf ("\n");

	getchar() ;

	printf("\n---Sortie de : %d ", FileSortir(P)) ;
	printf ("\nVoila la file vide:");
	FileAfficher(P) ;
	printf ("\n");

	printf ("\tet sa représentation interne :");
	FileRadiographier(P) ;
	printf ("\n");

	getchar() ;
	FileEntrer(2, P) ;
	printf ("\n+++Entrée de 2 \n Voila la file :");
	FileAfficher(P) ;	
	printf ("\n");
	printf ("\tet sa représentation interne :");
	FileRadiographier(P) ;
	printf ("\n");

	getchar() ;

	FileEntrer(3, P) ;
	printf ("\nEntrée de 3 ; Voila la file :");
	FileAfficher(P) ;
	printf ("\n\tet sa représentation interne :");
	FileRadiographier(P) ;
	printf ("\n");

	getchar() ;
	FileEntrer(4, P) ;
	printf ("\nEntrée de 4 ; Voila la file :");
	FileAfficher(P) ;
	printf ("\n\tet sa représentation interne :");
	FileRadiographier(P) ;
	printf ("\n");

	getchar() ;

	printf ("\nEntrée de 5\n" );
	FileEntrer(5, P) ;
	printf ("\nVoila la file :");
	FileAfficher(P) ;
	printf ("\n\tet sa représentation interne :");
	FileRadiographier(P) ;
	printf ("\n");

	FileDetruire(P) ;
		/* stockage direct pas d'élément à supprimer    */
	 exit( 0 );



}

