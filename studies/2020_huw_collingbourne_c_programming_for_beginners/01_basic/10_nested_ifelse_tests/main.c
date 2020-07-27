/* Data: 2020-07-27 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	char idade[4];
	int idade_int;
	double salario, bonus, total;
	
	printf("Digite sua idade: ");
	fgets(idade, 4, stdin);
	idade_int = atoi(idade);
	/*
	 * O if-else externo serve para validar se
	 * o input (sempre char) pode ser convertido
	 * para int. Se não pode, ele retorna zero e
	 * nenhuma operação é realizada.
	 */
	if (idade_int == 0) {
		printf("Você digitou valor inválido.\nNão é possível calcular seu bônus.\n");
	} else {
		/*
		 * O if-else interno é usado caso o valor 
		 * digitado possa ser convertido para int. 
		 * Aqui ele aplica o índice do bônus de 
		 * acordo com a idade.
		 */
		if (idade_int >= 45) {
			salario = 4000;
			bonus = salario * ((double)idade_int / 100); /* (double) converte int para double */
			total = salario + bonus;
			printf("Idade: %d\nSalário: %.2f\nBônus: %.2f\nTotal: %.2f\n", idade_int, salario, bonus, total);
		} else {
			salario = 3500;
			bonus = salario * ((double)idade_int / 125);
			total = salario + bonus;
			printf("Idade: %d\nSalário: %.2f\nBônus: %.2f\nTotal: %.2f\n", idade_int, salario, bonus, total);
		}
	}
	return 0;
}

/* 
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./10_nested_ifelse_tests
 * 
 * OUTPUT:
 * Digite sua idade: 52
 * Idade: 52
 * Salário: 4000.00
 * Bônus: 2080.00
 * Total: 6080.00
 * Press ENTER to continue...
 * 
 * Digite sua idade: Qwe
 * Você digitou valor inválido.
 * Não é possível calcular seu bônus.
 * Press ENTER to continue...
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 10_nested_ifelse_tests - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/10_nested_ifelse_tests'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/10_nested_ifelse_tests/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/10_nested_ifelse_tests @"10_nested_ifelse_tests.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/10_nested_ifelse_tests'
 * ====0 errors, 0 warnings====
 */