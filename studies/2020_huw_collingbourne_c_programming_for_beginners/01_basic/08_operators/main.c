/* Data: 2020-07-26 */

#include <stdio.h>
#include <stdlib.h> /* Onde está a função atoi() */

int main(int argc, char **argv) 
{
	/*
	 * Vamos declarar os tipos de todas as
	 * variáveis que vamos usar e deixar
	 * sem valores
	 */
	char idade[3]; /* Aceita 2 caracteres; o último é carriage return */
	int idade_int;
	int bonus;
	
	/*
	 * Agora, assinalamos os valores das
	 * variáveis, sendo:
	 * 		1. idade: o que o usuário digitar
	 * 		2. idade_int: idade convertida
	 * 		para int
	 * 		3. bonus: valor do bonus a 
	 * 		depender da idade
	 */
	printf("Coloque sua idade: ");
	fgets(idade, 3, stdin); /* fgets(variável, tamanho máximo, origem (arquivo, stind etc.)) */ 
	idade_int = atoi(idade); /*atoi() converte str para int */
	if (idade_int >= 45) {
	 bonus = 700;
	} else {
	 bonus = 500;
	}
	printf("Sua idade é %s e seu bônus é de %d reais.\n", idade, bonus);
	return 0;
}

/* 
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./08_operators
 * 
 * OUTPUT:
 * Coloque sua idade: 86
 * Sua idade é 86 e seu bônus é de 700 reais.
 * Press ENTER to continue...
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 08_operators - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/08_operators'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/08_operators/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/08_operators @"08_operators.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/08_operators'
 * ====0 errors, 0 warnings====
 */