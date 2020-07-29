/* Data: 2020-07-28 */

#include <stdio.h>

void flush_input(){
	int ch; /* int porque o resultado será booleano (0 ou 1) */
	while ((ch = getchar()) != '\n' && ch != EOF); /* getchar() pega o caractere de stdin */
}

void getinput_gets(){
	/*
	 * Quando a quantidade de caracteres digitados 
	 * é maior que a limitação, gets() retorna todo 
	 * o bloco de memória onde o valor está alocado 
	 * e não apenas o valor. Com isso, o output é 
	 * imprevisível.
	 */
	char firstname[5]; /* Quero apenas 4 caracteres (o quinto é CR) */
	char lastname[5]; /* Idem */
	printf("Nome: ");
	gets(firstname);
	printf("Sobrenome: ");
	gets(lastname);
	printf("Olá, %s %s\n", firstname, lastname);
	/*
	 * INPUT:
	 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./11_gets_vs_fgets
	 * 
	 * OUTPUT (com caracteres abaixo do limite):
	 * Nome: Ana
	 * Sobrenome: Sé
	 * Olá, Ana Sé
	 * Press ENTER to continue...
	 * 
	 * OUTPUT (com caracteres acima do limite): 
	 * Nome: Rodolfo
	 * Sobrenome: Viana
	 * Olá, RodolViana Viana
	 * Press ENTER to continue...
	 * 
	 * BUILD INPUT:
	 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
	 * 
	 * BUILD OUTPUT:
	 * ----------Building project:[ 11_gets_vs_fgets - Debug ]----------
	 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets'
	 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
	 * /home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets/main.c: In function 'getinput_gets':
	 * /home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets/main.c:21:2: warning: implicit declaration of function 'gets'; did you mean 'fgets'? [-Wimplicit-function-declaration]
	 *   21 |  gets(firstname);
	 *      |  ^~~~
	 *      |  fgets
	 * /usr/bin/g++ -o ./Debug/11_gets_vs_fgets @"11_gets_vs_fgets.txt" -L.
	 * /usr/bin/ld: ./Debug/main.c.o: in function `getinput_gets':
	 * /home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets/main.c:14: warning: the `gets' function is dangerous and should not be used.
	 * make [1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets'
	 * ====0 errors, 2 warnings====
	 */
}

void getinput_fgets(){
	/*
	 * fgets() é mais seguro que gets(). Ele requer
	 * três argumentos: variável, máximo de 
	 * caracteres - 1 (pois o último é \0 (null 
	 * character), que mostra o fim da str), e 
	 * origem dos caracteres.
	 * Por outro lado, fgets() também causa erro
	 * se a quantidade de caracteres digitada for
	 * maior que o limite. Segundo o instrutor:
	 * 	"If you enter more characters than are actually 
	 * 	processed by your code, those characters remain 
	 * 	in memory (buffer), waiting to be processed. So 
	 * 	when you next try to read some characters from 
	 * 	the command line, the characters waiting to be 
	 * 	processed will be read in first."
	 * Desta forma, quando temos duas variáveis, parte
	 * dos caracteres da primeira variável fica na 
	 * segunda variável.
	 * O código abaixo sem flush_input() retorna o
	 * seguinte:
	 * 
	 * INPUT:
	 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./11_gets_vs_fgets
	 * 
	 * OUTPUT:
	 * Nome: Rodolfo
	 * Sobrenome: Olá, Rodo lfo
	 * Press ENTER to continue...
	 */
	char firstname[5]; /* Quero apenas 4 caracteres*/
	char lastname[5]; /* Idem */
	printf("Nome: ");
	fgets(firstname, 5, stdin); /* Guardo os 4 caracteres de stdin em firstname */
	printf("Sobrenome: ");
	flush_input();
	fgets(lastname, 5, stdin); /* Guardo os 4 caracteres de stdin em lastname */
	flush_input();
	printf("Olá, %s %s\n", firstname, lastname);
}

int main(int argc, char **argv){
	getinput_gets();
	getinput_fgets();
	return 0;
}

/*
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./11_gets_vs_fgets
 * 
 * OUTPUT:
 * Nome: Ana
 * Sobrenome: Sé
 * Olá, Ana Sé
 * Nome: Rodolfo
 * Sobrenome: Viana
 * Olá, Rodo Vian
 * Press ENTER to continue...
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 11_gets_vs_fgets - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets/main.c: In function 'getinput_gets':
 * /home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets/main.c:21:2: warning: implicit declaration of function 'gets'; did you mean 'fgets'? [-Wimplicit-function-declaration]
 *    21 |  gets(firstname);
 *       |  ^~~~
 *       |  fgets
 * /usr/bin/g++ -o ./Debug/11_gets_vs_fgets @"11_gets_vs_fgets.txt" -L.
 * /usr/bin/ld: ./Debug/main.c.o: in function `getinput_gets':
 * /home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets/main.c:21: warning: the `gets' function is dangerous and should not be used.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/11_gets_vs_fgets'
 * ====0 errors, 2 warnings====
 */