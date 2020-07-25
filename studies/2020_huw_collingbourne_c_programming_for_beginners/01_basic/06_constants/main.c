/* Data: 2020-07-25 */

#include <stdio.h>
#include <math.h>

int main(int argc, char **argv)
{
	/*
	 * Ao contrário de variáveis, que podem ter
	 * os valores alterados, constantes torna os
	 * valores atribuídos imutáveis.
	 * Ele é feito da seguinte forma:
	 * 		#define NOME valor
	 * (sem sinal de = e sem ; no final)
	 */ 
	#define PI 2.141593 /* valor errado para teste */
	printf("%f\n", PI);
	printf("%f\n", M_PI);
	return 0;
}

/*
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./06_constants
 * 
 * OUTPUT:
 * 2.141593
 * 3.141593
 * Press ENTER to continue...
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 06_constants - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/06_constants'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/06_constants/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/06_constants @"06_constants.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/06_constants'
 * ====0 errors, 0 warnings====
 */