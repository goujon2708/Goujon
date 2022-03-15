#-------------
# Executables 
#-------------

main : main.o CodeLongMax.o gold.o jpl.o
	gcc main.o CodeLongMax.o gold.o jpl.o -o main

main.o : main.c
	gcc -c main.c -o main.o 

#----------
# Modules
#----------


CodeLongMax.o : CodeLongMax.c CodeLongMax.h
	gcc -c CodeLongMax.c -o CodeLongMax.o

gold.o : gold.c gold.h
	gcc -c gold.c -o gold.o
	
jpl.o : jpl.c jpl.h
	gcc -c jpl.c -o jpl.o

#----------------------------
# Gestion generale du projet 
#----------------------------

all : main

clean :
	rm *.o

tags : 
	etags *.c *.h