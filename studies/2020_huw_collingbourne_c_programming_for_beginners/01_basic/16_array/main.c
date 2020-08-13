/* Data: 2020-08-12 */

#include <stdio.h>
#include <math.h>

int intarray[5];

int main(int argc, char **argv) {
	int i;
	
	/* Algum cálculo qualquer só para deixar divertido */
	intarray[0] = 1;
	intarray[1] = pow((intarray[0] + 1), 2);
	intarray[2] = pow((intarray[1] + 1), 2);
	intarray[3] = pow((intarray[2] + 1), 2);
	intarray[4] = pow((intarray[3] + 1), 2);
	
	for (i = 0; i < 5; i++) {
		printf("%d\n", intarray[i]);
	}
}

/*
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./16_array
 * 
 * OUTPUT:
 * 1
 * 4
 * 25
 * 676
 * 458329
 * Hit any key to continue...
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 16_array - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/16_array'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/16_array/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/16_array @"16_array.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/16_array'
 * ====0 errors, 0 warnings====
 */