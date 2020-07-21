/* Data: 2020-07-19 */

#include <stdio.h>

main() {
	printf("This is a \'Hello world\' with printf.\n");
	/* 
	 * printf e puts são similares, com uma
	 * exceção: printf aceita especificação 
	 * de formato. Dois comuns são %d para
	 * int ou decimal, e %s para string.
	 */
	puts("And this is a \'Hello world\' with puts.\n");
	printf("But printf accepts format specifiers such as %s for strings and %s for numbers.\n", "%s", "%d");
	printf("Example: %d bottles of %s.\n", 20, "gin");
	/* 
	 * Depois de inserir os especificadores
	 * no printf, usamos, no final e na
	 * ordem em que aparecem, os valores
	 * que serão usados na substituição.
	 */ 
}

/* 
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./03_printf
 * 
 * OUTPUT:
 * This is a 'Hello world' with printf.
 * And this is a 'Hello world' with puts.
 * 
 * But printf accepts format specifiers such as %s for strings and %d for numbers.
 * Example: 20 bottles of gin.
 * Press ENTER to continue...
 *
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 03_printf - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/03_printf'
 * make[1]: Nothing to be done for 'all'.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/03_printf'
 * ====0 errors, 0 warnings====
 */
