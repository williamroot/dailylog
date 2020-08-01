/* Data: 2020-07-31 */

#include <stdio.h>

/*
 * Em C, eu devo especificar o tipo que será
 * retornado antes da função. Em caso de não
 * haver retorno (return), o tipo é void.
 */

void sayHello(){
	/* void, pois não há return */
	printf("Olá\n");
}

void greet(char name[]){
	/* [], pois pega uma array de caracteres sem limite estabelecido */
	printf("Olá, %s\n", name);
}

int soma(int n1, int n2){
	/* int, pois é inteiro no return */
	n1 += n2;
	return n1;
	/* Em vez das duas linhas acima eu poderia usar apenas uma: return n1 + n2 */
}

double divisao(int n1, int n2){
	return (double)n1 / n2;
	/* Especifico double no return para não ter resultado truncado, uma vez que a divisão acontece com dois int */
}

int main(){
	int result_1;
	double result_2;
	int n1;
	int n2;
	n1 = 10;
	n2 = 3;
	sayHello();
	greet("Rodolfo");
	result_1 = soma(n1, n2);
	result_2 = divisao(n1, n2);
	printf("%d é a soma; %.2f é a divisão\n", result_1, result_2);
	return 0;
}

/*
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./13_functions
 * 
 * OUTPUT:
 * Olá
 * Olá, Rodolfo
 * 13 é a soma; 3.33 é a divisão
 * Press ENTER to continue...
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 13_functions - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/13_functions'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/13_functions/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/13_functions @"13_functions.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/13_functions'
 * ====0 errors, 0 warnings====
 */