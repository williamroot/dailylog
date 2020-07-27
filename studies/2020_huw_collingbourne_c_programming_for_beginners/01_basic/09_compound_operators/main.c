/* Data: 2020-07-26 */

#include <stdio.h>

int main(int argc, char **argv)
{
	int a, b, c;
	a = 10;
	b = 2;
	a += b;
	printf("Compound operators:\n\na = 10\nb = 2\na += b é igual a a = a + b, cujo resultado é %d\n", a);
	a = 10;
	b = 2;
	a -= b;
	printf("a -= b é igual a a = a - b, cujo resultado é %d\n", a);
	a = 10;
	b = 2;
	a *= b;
	printf("a *= b é igual a a = a * b, cujo resultado é %d\n", a);
	a = 10;
	b = 2;
	a /= b;
	printf("a /= b é igual a a = a / b, cujo resultado é %d\n(Como a é int, o resultado é int. Caso fosse fração, os valores fracionados seriam ignorados.)\n", a);
	/* Postfix operator */
	a = 10;
	c = a++;
	printf("\nPostfix operator:\n\na = 10\nc = a++ significa que c = a e, depois, a += 1. Assim, c = %d e a = %d\n", c, a);
	a = 10;
	c = a--;
	printf("c = a-- significa que c = a e, depois, a -= 1. Assim, c = %d e a = %d\n", c, a);
	/* Prefix operator */
	a = 10;
	c = ++a;
	printf("\nPrefix operator:\n\na = 10\nc = ++a significa que c = a, mas antes, a += 1. Assim, c = %d e a = %d\n", c, a);
	a = 10;
	c = --a;
	printf("c = --a significa que c = a, mas antes, a -= 1. Assim, c = %d e a = %d\n", c, a);
	return 0;
}

/*
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./09_compound_operators
 * 
 * OUTPUT:
 * Compound operators:
 * 
 * a = 10
 * b = 2
 * a += b é igual a a = a + b, cujo resultado é 12
 * a -= b é igual a a = a - b, cujo resultado é 8
 * a *= b é igual a a = a * b, cujo resultado é 20
 * a /= b é igual a a = a / b, cujo resultado é 5
 * (Como a é int, o resultado é int. Caso fosse fração, os valores fracionados seriam ignorados.)
 * 
 * Postfix operator:
 * 
 * a = 10
 * c = a++ significa que c = a e, depois, a += 1. Assim, c = 10 e a = 11
 * c = a-- significa que c = a e, depois, a -= 1. Assim, c = 10 e a = 9
 * 
 * Prefix operator:
 * 
 * a = 10
 * c = ++a significa que c = a, mas antes, a += 1. Assim, c = 11 e a = 11
 * c = --a significa que c = a, mas antes, a -= 1. Assim, c = 9 e a = 9
 * Press ENTER to continue...
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 09_compound_operators - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/09_compound_operators'
 * make[1]: Nothing to be done for 'all'.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/09_compound_operators'
 * ====0 errors, 0 warnings====
 */