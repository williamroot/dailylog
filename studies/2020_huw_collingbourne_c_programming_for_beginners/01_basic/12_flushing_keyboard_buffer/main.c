#include <stdio.h>

#define STRLEN 5

/*
 * C tem uma função para limpar o buffer de input
 * (fflush()) e outra para setar a leitura para o
 * começo da sequência (rewind()). Contudo, são
 * funções que dependem do sistema operacional
 * para serem utilizadas de maneira correta.
 * Por isso, vamos criar uma forma alternativa de
 * limpar o buffer de entrada -- não exatamente
 * efetuando a limpeza, mas setando o descarte de
 * caracteres extras e a posição inicial do stream
 * seguinte.
 * Aqui, os caracteres serão guardados um a um.
 */

int readln(char s[], int maxlen){ /* Preciso de dois argumentos: stream (s) e limite de caracteres (maxlen) */
	char ch;
	int i;
	int chars_remain;
	i = 0;
	chars_remain = 1; /* (True) */
	while (chars_remain){ /* Enquanto houver caractere... */
		ch = getchar(); /* ...pegue o caractere... */
		if ((ch == '\n') || (ch == EOF)){ /* ...e se ele for nova linha ou fim do stream... */
			chars_remain = 0; /* (False) */
		} else if (i < maxlen - 1){ /* ...e se a posição dele for menor que a posição final - 1 (pois o último caractere é \0)... */
			s[i] = ch; /* ...essa posição serão a posição no stream... */
			i++; /* ... e adicionamos 1 ao valor da posição. */
		}
	}
	s[i] = '\0'; /* A posição final no stream será \0 */
	return i;
}

int main(int argc, char **argv) {
	char firstname[STRLEN];
	char lastname[STRLEN];
	int len_firstname;
	int len_lastname;
	printf("Nome: ");
	len_firstname = readln(firstname, STRLEN);
	printf("Sobrenome: ");
	len_lastname = readln(lastname, STRLEN);
	printf("Olá, %s %s\n", firstname, lastname);
	printf("Tamanho de nome = %d\nTamanho de sobrenome = %d/n", len_firstname, len_lastname);
}

/*
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./12_flushing_keyboard_buffer
 * 
 * OUTPUT:
 * Nome: Rodolfo
 * Sobrenome: Viana
 * Olá, Rodo Vian
 * Tamanho de nome = 4
 * Tamanho de sobrenome = 4
 * Press ENTER to continue...
 * 
 * Nome: Ana
 * Sobrenome: Sé
 * Olá, Ana Sé
 * Tamanho de nome = 3
 * Tamanho de sobrenome = 3
 * Press ENTER to continue...
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 12_flushing_keyboard_buffer - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/12_flushing_keyboard_buffer'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/12_flushing_keyboard_buffer/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/12_flushing_keyboard_buffer @"12_flushing_keyboard_buffer.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/12_flushing_keyboard_buffer'
 * ====0 errors, 0 warnings====
 */