/* Data: 2020-07-19 */

#include <stdio.h>

int main(int argc, char **argv) {
	/*
	 * `argc` é o cálculo automático 
	 * da quantidade de argumentos 
	 * (por isso é int), enquanto 
	 * `**argv` é uma array de 
	 * caracteres (por isso é char).
	 */
	int i;
	for (i = 0; i < argc; i++) {
        printf("Total de argumentos = %d\nArgumento %d é %s\n", argc, i, argv[i]);
    }
	/*
	 * Quero fazer um for loop para
	 * mostrar cada uma das cadeias
	 * de caracteres. Para isso,
	 * preciso:
	 * 1. indicar que `i` (o contador) 
	 * é int;
	 * 2. criar o for loop dizendo que
	 * `i` é 0 inicialmente, e que
	 * enquanto `i` for menor que o 
	 * valor de `argc`, é preciso 
	 * adicionar 1 ao valor de `i`;
	 * 3. instruir a função para, a
	 * cada `i`, imprimir:
	 * 3.1. a quantidade total de 
	 * argumentos (%d para `argc`);
	 * 3.2. Uma frase com o número
	 * (%d para `i`) e o valor (%s
	 * para `argv[i]`) de cada
	 * argumento.
	 */
	return 0;
	/*
	 * Um programa em C retorna dados.
	 * Por isso, é preciso indicar o
	 * tipo de dado retornado. Isso é
	 * feito antes do nome da função
	 * (no caso, `main`). Zero (int)
	 * significa que o programa rodou
	 * corretamente. Caso o programa
	 * não retorne 0, algum erro 
	 * aconteceu.
	 */
}

/* 
 * INPUT:
 * /bin/sh -f /usr/lib/codelite/codelite_exec ./02_helloworld_with_args hello dear world
 * 
 * OUTPUT:
 * Total de argumentos = 4
 * Argumento 0 é ./02_helloworld_with_args
 * Total de argumentos = 4
 * Argumento 1 é hello
 * Total de argumentos = 4
 * Argumento 2 é dear
 * Total de argumentos = 4
 * Argumento 3 é world
 * Press ENTER to continue...
 * 
 * DEBUG INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * DEBUG OUTPUT:
 * ----------Building project:[ 02_helloworld_with_args - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/02_helloworld_with_args'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/02_helloworld_with_args/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/02_helloworld_with_args @"02_helloworld_with_args.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/02_helloworld_with_args'
 * ====0 errors, 0 warnings====
 */

