#===========================================
# Makefile du TP1 de Codage de l'information
#===========================================

#-------------
# Executables 
#-------------


test_tp1 : test_tp1.o hadam.o 
	gcc test_tp1.o hadam.o -o test_tp1

test_tp1.o : test_tp1.c
	gcc -c test_tp1.c -o test_tp1.o 


#----------
# Modules
#----------

hadam.o : hadam.c
	gcc -c hadam.c -o hadam.o


#----------------------------
# Gestion generale du projet 
#----------------------------

all : test_tp1

clean :
	rm *.o

tags : 
	etags *.c *.h