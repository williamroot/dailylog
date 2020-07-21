/* Data: 2020-07-20 */

#include <stdio.h>

int main(int argc, char **argv) {
	/*
	 * Como regra, primeio declaramos as variáveis
	 * e seus tipos, e depois damos a elas os
	 * valores.
	 */
	double grana;
	int vendas;
	/* 
	 * Mas há outras formas de fazer isso:
	 * 1. quanto houver mais de uma variável do
	 * mesmo tipo, podemos fazer:
	 * Ex.: double grana, preco;
	 * 2. podemos assinalar os valores no momento
	 * em que há a declaração:
	 * Ex.: int vendas = 17;
	 */
	
	vendas = 17;
	grana = 832.12;
	printf("Ontem houve %d vendas no total de %.2f reais.\n", vendas, grana);
	/*
	 * A variável pode ser reescrita.
	 */
	vendas = 22;
	grana = 1092.5;
	/*
	 * O double agora terá duas casas decimais 
	 * com o uso de %.2f, mesmo que haja apenas 
	 * uma casa no valor assinalado.
	 */
	printf("Hoje, vendemos %d produtos, e a receita foi de %.2f reais.\n", vendas, grana);
	return 0;
}

/* INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./04_variables_and_types
 * 
 * OUTPUT:
 * Ontem houve 17 vendas no total de 832.12 reais.
 * Hoje, vendemos 22 produtos, e a receita foi de 1092.50 reais.
 * Press ENTER to continue...
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 04_variables_and_types - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/04_variables_and_types'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/04_variables_and_types/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/04_variables_and_types @"04_variables_and_types.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/04_variables_and_types'
 * ====0 errors, 0 warnings====
 */
 