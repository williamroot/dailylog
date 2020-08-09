/* Data: 2020-08-09 */

/* 
 * Depois de ver a função de classificação de ASCII 
 * com if-else, vamos reproduzi-la com switch e case.
 */

#include <stdio.h>

char *chartype;

void findchartype(int i) {
	switch(i) {
		case 0:
			chartype = "Null";
			break;
		case 7:
			chartype = "Bell";
			break;
		case 8:
			chartype = "Backspace";
			break;
		case 9:
			chartype = "Tab";
			break;
		case 10:
			chartype = "Linefeed";
			break;
		case 13:
			chartype = "Carriage return";
			break;
		case 32:
			chartype = "Space";
			break;
		case 48 ... 57:
			/* 
			 * Este ... indica range. Segundo o instrutor.
			 * 	"ranges in switch-case are an extension to 
			 * 	standard C and this syntax is not supported 
			 * 	by all C compilers."
			 * No caso de ... não ser válido, a alternativa
			 * é esta:
			 * 	case 48:
			 * 	case 49:
			 * 	case 50:
			 * etc.
			 * 		chartype = "Número";
			 * 		break;
			 */
			chartype = "Número";
			break;
		case 65 ... 90:
			chartype = "Letra maiúscula";
			break;
		case 97 ... 122:
			chartype = "Letra minúscula";
			break;
		default:
			/* 
			 * Default é tudo que não está nos cases; seria 
			 * o else de uma if statement, por analogia
			 */
			chartype = "Sinal gráfico";
			break;
	}
}

/*
 * Uma outra forma de escrever esta função seria
 * com char em vez de int. Ficaria assim:
 * void findchartype(char i) {
 * 	switch(i) {
 * 		case '\0':
 * 			chartype = "Null";
 * 			break;
 * 		case '\a':
 * 			chartype = "Bell";
 * 			break;
 * 		case '\b':
 * 			chartype = "Backspace";
 * 			break;
 * 		case '\t':
 * 			chartype = "Tab";
 * 			break;
 * 		case '\n':
 * 			chartype = "Linefeed";
 * 			break;
 * 		case '\r':
 * 			chartype = "Carriage return";
 * 			break;
 * 		case ' ':
 * 			chartype = "Space";
 * 			break;
 * 		case '0' ... '9':
 * 			chartype = "Número";
 * 			break;
 * 		case 'A' ... 'Z':
 * 			chartype = "Letra maiúscula";
 * 			break;
 * 		case 'a' ... 'z':
 * 			chartype = "Letra minúscula";
 * 			break;
 * 		default:
 * 			chartype = "Sinal gráfico";
 * 			break;
 * 	}
 * }
 */

void showascii() {
	int i;
	for (i = 0; i <= 127; i++) {
		findchartype(i);
		printf("%d = %c\t\t[%s]\n", i, i, chartype);
	}
}

int main(int argc, char **argv) {
	showascii();
	return 0;
}
/* 
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./15_switch_statements_2
 * 
 * OUTPUT:
 * 0 = 		[Null]
 * 1 = 		[Sinal gráfico]
 * 2 = 		[Sinal gráfico]
 * 3 = 		[Sinal gráfico]
 * 4 = 		[Sinal gráfico]
 * 5 = 		[Sinal gráfico]
 * 6 = 		[Sinal gráfico]
 * 8 =     	[Backspace]
 * 9 = 			[Tab]
 * 10 = 
 * 		[Linefeed]
 * 11 = 
 *      		[Sinal gráfico]
 * 12 = 
 *      		[Sinal gráfico]
 * 13 =    	[Carriage return]
 * 14 = 		[Sinal gráfico]
 * 15 = 		[Sinal gráfico]
 * 16 = 		[Sinal gráfico]
 * 17 = 		[Sinal gráfico]
 * 18 = 		[Sinal gráfico]
 * 19 = 		[Sinal gráfico]
 * 20 = 		[Sinal gráfico]
 * 21 = 		[Sinal gráfico]
 * 22 = 		[Sinal gráfico]
 * 23 = 		[Sinal gráfico]
 * 24 = 		[Sinal gráfico]
 * 25 = 		[Sinal gráfico]
 * 26 = �		[Sinal gráfico]
 * 27 = 		
 *                 inal gráfico]
 * 28 = 		[Sinal gráfico]
 * 29 = 		[Sinal gráfico]
 * 30 = 		[Sinal gráfico]
 * 31 = 		[Sinal gráfico]
 * 32 =  		[Space]
 * 33 = !		[Sinal gráfico]
 * 34 = "		[Sinal gráfico]
 * 35 = #		[Sinal gráfico]
 * 36 = $		[Sinal gráfico]
 * 37 = %		[Sinal gráfico]
 * 38 = &		[Sinal gráfico]
 * 39 = '		[Sinal gráfico]
 * 40 = (		[Sinal gráfico]
 * 41 = )		[Sinal gráfico]
 * 42 = *		[Sinal gráfico]
 * 43 = +		[Sinal gráfico]
 * 44 = ,		[Sinal gráfico]
 * 45 = -		[Sinal gráfico]
 * 46 = .		[Sinal gráfico]
 * 47 = /		[Sinal gráfico]
 * 48 = 0		[Número]
 * 49 = 1		[Número]
 * 50 = 2		[Número]
 * 51 = 3		[Número]
 * 52 = 4		[Número]
 * 53 = 5		[Número]
 * 54 = 6		[Número]
 * 55 = 7		[Número]
 * 56 = 8		[Número]
 * 57 = 9		[Número]
 * 58 = :		[Sinal gráfico]
 * 59 = ;		[Sinal gráfico]
 * 60 = <		[Sinal gráfico]
 * 61 = =		[Sinal gráfico]
 * 62 = >		[Sinal gráfico]
 * 63 = ?		[Sinal gráfico]
 * 64 = @		[Sinal gráfico]
 * 65 = A		[Letra maiúscula]
 * 66 = B		[Letra maiúscula]
 * 67 = C		[Letra maiúscula]
 * 68 = D		[Letra maiúscula]
 * 69 = E		[Letra maiúscula]
 * 70 = F		[Letra maiúscula]
 * 71 = G		[Letra maiúscula]
 * 72 = H		[Letra maiúscula]
 * 73 = I		[Letra maiúscula]
 * 74 = J		[Letra maiúscula]
 * 75 = K		[Letra maiúscula]
 * 76 = L		[Letra maiúscula]
 * 77 = M		[Letra maiúscula]
 * 78 = N		[Letra maiúscula]
 * 79 = O		[Letra maiúscula]
 * 80 = P		[Letra maiúscula]
 * 81 = Q		[Letra maiúscula]
 * 82 = R		[Letra maiúscula]
 * 83 = S		[Letra maiúscula]
 * 84 = T		[Letra maiúscula]
 * 85 = U		[Letra maiúscula]
 * 86 = V		[Letra maiúscula]
 * 87 = W		[Letra maiúscula]
 * 88 = X		[Letra maiúscula]
 * 89 = Y		[Letra maiúscula]
 * 90 = Z		[Letra maiúscula]
 * 91 = [		[Sinal gráfico]
 * 92 = \		[Sinal gráfico]
 * 93 = ]		[Sinal gráfico]
 * 94 = ^		[Sinal gráfico]
 * 95 = _		[Sinal gráfico]
 * 96 = `		[Sinal gráfico]
 * 97 = a		[Letra minúscula]
 * 98 = b		[Letra minúscula]
 * 99 = c		[Letra minúscula]
 * 100 = d		[Letra minúscula]
 * 101 = e		[Letra minúscula]
 * 102 = f		[Letra minúscula]
 * 103 = g		[Letra minúscula]
 * 104 = h		[Letra minúscula]
 * 105 = i		[Letra minúscula]
 * 106 = j		[Letra minúscula]
 * 107 = k		[Letra minúscula]
 * 108 = l		[Letra minúscula]
 * 109 = m		[Letra minúscula]
 * 110 = n		[Letra minúscula]
 * 111 = o		[Letra minúscula]
 * 112 = p		[Letra minúscula]
 * 113 = q		[Letra minúscula]
 * 114 = r		[Letra minúscula]
 * 115 = s		[Letra minúscula]
 * 116 = t		[Letra minúscula]
 * 117 = u		[Letra minúscula]
 * 118 = v		[Letra minúscula]
 * 119 = w		[Letra minúscula]
 * 120 = x		[Letra minúscula]
 * 121 = y		[Letra minúscula]
 * 122 = z		[Letra minúscula]
 * 123 = {		[Sinal gráfico]
 * 124 = |		[Sinal gráfico]
 * 125 = }		[Sinal gráfico]
 * 126 = ~		[Sinal gráfico]
 * 127 = 		[Sinal gráfico]
 * Press ENTER to continue...
 *
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 15_switch_statements_2 - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/15_switch_statements_2'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/15_switch_statements_2/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/15_switch_statements_2 @"15_switch_statements_2.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/15_switch_statements_2'
 * ====0 errors, 0 warnings====
 */