# encoding: UTF-8

##
# Auteur SCHERRER
# Version 0.1 : Date : Fri Oct 22 11:43:11 CEST 2021
#

class Livre

# 	=begin	
# 	
# 		Un livre
# 			- ont un numéro d'enregistrement ==> VI @enregistrement
# 			- un titre ==> VI titre
# 			- un auteur ==> VI auteur
# 			- un nb de pages ==> VI nbPages
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
# 	=end




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

	def Livre.ranger( numEnr , titre , auteur , nbPage , dispo )
	
		new( numEnr , titre , auteur , nbPage , dispo )
		
	end 



	

	def initialize( numEnr , titre , auteur , nbPage , dispo )
	
		@enregistrement = numEnr
		@titre 			= titre
		@auteur 		= auteur
		@nbPage			= nbPage
		@etat			= 'ok'
		@dispo 			= true
		
	end 



	def to_s

		"Numero enregistrement : #{@enregistrement} \nTitre : #{@titre} \nAuteur : #{@auteur} \nNombre de page : #{@nbPage} \nEtat : #{@etat} \nDisponibilité : #{@dispo}"
	
	end

	

end # Livre




########################################
# PROGRAMME DE TEST DE LA CLASSE LIVRE #
########################################



monLivre = Livre.ranger( 001 , "Ruby pour les nuls" , "SCHERRER" , 2 , true )

print monLivre










