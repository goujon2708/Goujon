#============================
# Makefile du Cours 2 / PILE
#============================

#-------------
# Executables 
#-------------

testpile : testpile.o eltprim.o pileprim.o 
	gcc testpile.o eltprim.o pileprim.o  -o testpile

testpile.o : testpile.c
	gcc -c testpile.c -o testpile.o 

#----------
# Modules
#----------

# TDA ELEMENT
#

# -- Primitives avec realisation par "int"
#
eltprim.o : eltint.c eltprim.h
	gcc -c eltint.c -o eltprim.o

eltprim.h : eltsdd.h
	touch eltprim.h

eltsdd.h : eltint.h
	touch eltsdd.h

# -- Operations 
#

# TDA FFILE
#

# -- Primitives avec realisation par faux pointeurs : 
#

pileprim.o : piltabdy.c pileprim.h
	gcc -c piltabdy.c -o pileprim.o

pileprim.h : pilesdd.h 
	touch pileprim.h

pilesdd.h : piltabdy.h 
	touch pilesdd.h

# -- Operations 
#

#----------------------------
# Gestion generale du projet 
#----------------------------

all : testpile

clean :
	rm *.o

tags : 
	etags *.c *.h
