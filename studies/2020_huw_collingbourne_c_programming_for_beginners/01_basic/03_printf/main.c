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
