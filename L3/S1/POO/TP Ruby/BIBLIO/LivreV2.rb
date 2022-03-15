# encoding: UTF-8

##
# Auteur SCHERRER
# Version 0.1 : Date : Fri Oct 22 11:43:11 CEST 2021
#




class Livre

# 		Un livre a
# 			- un numéro d'enregistrement
# 			- un titre ==> VI @titre
# 			- un auteur ==> VI @auteur
# 			- un nb de pages ==> VI @nbPages
# 			- un état ==> VI etat
# 			- un booleen indicant la disponibilité du livre ==> VI bool
# 	
# 		
# 		Les variables d'instances de la classe Livre sont :
# 		
# 			@enregistrement ==> numéro d'enregistrement
# 			@titre			==> titre du livre 
# 			@auteur			==> auteur du livre
# 			@nbPage			==> nb de pages du livre
# 			@etat			==> etat général du livre
# 			@bool			==> indicateur de disponibilité du livre 
# 
# 
# 		Les variables de classe de la classe Livre sont : 
# 
# 			@@numeroLivre ==> numero du livre (incrémentée à chaque création)




	# comme c'est une sorte de compteur, il faut initiialiser cette variable de classe à 0
	@@numeroLivre = 0


	# on donne l'accès en lecture aux différentes VI
	attr_reader :numeroLivre , :titre , :auteur , :enregistrement , :nbPage , :etat , :dispo



	#	Méthode qui va creer les différents champs qui seront ensuite utilisés
	#
	#	5 paramètres : 
	#
	#		numEnr 		==> numero d'enregistrement
	#		titre		==> titre du livre
	#		auteur		==> auteur du livre
	#		nbPage		==> nombre de page contenues dans le livre
	#		dispo		==> booleen indicant la disponibilité du livre
	#
	#	Pour gérer la numérotation des livres, on utilise une variable de classe 
	#	qui va s'incrémenter à chaque création d'un livre
	

	def Livre.ranger( titre , auteur , nbPage )

		new( titre , auteur , nbPage )
		
	end 






	#	Initialisation des différentes variables d'instances
	#	@etat et @bool sont définis ainsi comme le demande l'énoncé
	#	
	#	on incrémente la variable de classe @@numero livre
	#
	#	3 paramètres : 
	#		titre 	==> titre du livre
	#		auteur	==> auteur du livre
	#		nbPage	==> nb de page du livre

	def initialize( titre , auteur , nbPage )
	
		@enregistrement = @@numeroLivre
		@@numeroLivre	+= 1
		@titre 			= titre
		@auteur 		= auteur
		@nbPage			= nbPage
		@etat			= 'ok'
		@dispo 			= true
		
	end 




	#	On implemente l'affichage de notre programme de test dans la méthode to_s afin
	#	de simplfier l'appel dans ce dernier
	# 	Il suffit juste d'appeler print et le Livre à afficher

	def to_s

		"Numero enregistrement : #{@@numeroLivre} \nTitre : #{@titre} \nAuteur : #{@auteur} \nNombre de page : #{@nbPage} \nEtat : #{@etat} \nDisponibilité : #{@dispo}\n"
	
	end

	

end # Livre







########################################
# PROGRAMME DE TEST DE LA CLASSE LIVRE #
########################################




monLivre = Livre.ranger( "Ruby pour les nuls" , "SCHERRER" , 435 )

print monLivre










