/* Data: 2020-08-07 */

/* 
 * Vamos ver como fica a função de classificação de
 * ASCII usando apenas if-else. Em seguida, faremos
 * a mesma função, mas com switch e case.
 */

#include <stdio.h>

char *chartype;

void findchartype(int i) {
	if ( i == 0 ) {
		chartype = "NULL";
	} else if (i == 7) {
		chartype = "Bell";
	} else if (i == 78) {
		chartype = "Backspace";
	} else if (i == 9) {
		chartype = "Tab";
	} else if (i == 10) {
		chartype = "LineFeed";
	} else if (i == 13) {
		chartype = "Carriage";
	} else if (i == 32) {
		chartype = "Space";
	} else if ((i >= 48) && (i <= 57)) {
		chartype = "Number";
	} else {
		chartype = "Character";
	}
}

void showascii() {
	int i;
	for (i = 0; i <= 127; i++) {
		findchartype(i);
		printf("%d = %c\t\t[%s]\n", i, i, chartype);
		/* "'%c',i" interpreta int (i) como código ASCII e retorna char (c) */
	}
}

int main(int argc, char **argv) {
	showascii();
	return 0;
}
/* 
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./14_switch_statements_1
 * 
 * OUTPUT:
 * 0 = 		[NULL]
 * 1 = 		[Character]
 * 2 = 		[Character]
 * 3 = 		[Character]
 * 4 = 		[Character]
 * 5 = 		[Character]
 * 6 = 		[Character]
 * 7 = 		[Bell]
 * 8 =     	[Character]
 * 9 = 			[Tab]
 * 10 = 
 * 		[LineFeed]
 * 11 = 
 *      		[Character]
 * 12 = 
 *      		[Character]
 * 13 =    	[Carriage]
 * 14 = 		[Character]
 * 15 = 		[Character]
 * 16 = 		[Character]
 * 17 = 		[Character]
 * 18 = 		[Character]
 * 19 = 		[Character]
 * 20 = 		[Character]
 * 21 = 		[Character]
 * 22 = 		[Character]
 * 23 = 		[Character]
 * 24 = 		[Character]
 * 25 = 		[Character]
 * 26 = �		[Character]
 * 27 = 		 haracter]
 * 28 = 		[Character]
 * 29 = 		[Character]
 * 30 = 		[Character]
 * 31 = 		[Character]
 * 32 =  		[Space]
 * 33 = !		[Character]
 * 34 = "		[Character]
 * 35 = #		[Character]
 * 36 = $		[Character]
 * 37 = %		[Character]
 * 38 = &		[Character]
 * 39 = '		[Character]
 * 40 = (		[Character]
 * 41 = )		[Character]
 * 42 = *		[Character]
 * 43 = +		[Character]
 * 44 = ,		[Character]
 * 45 = -		[Character]
 * 46 = .		[Character]
 * 47 = /		[Character]
 * 48 = 0		[Number]
 * 49 = 1		[Number]
 * 50 = 2		[Number]
 * 51 = 3		[Number]
 * 52 = 4		[Number]
 * 53 = 5		[Number]
 * 54 = 6		[Number]
 * 55 = 7		[Number]
 * 56 = 8		[Number]
 * 57 = 9		[Number]
 * 58 = :		[Character]
 * 59 = ;		[Character]
 * 60 = <		[Character]
 * 61 = =		[Character]
 * 62 = >		[Character]
 * 63 = ?		[Character]
 * 64 = @		[Character]
 * 65 = A		[Character]
 * 66 = B		[Character]
 * 67 = C		[Character]
 * 68 = D		[Character]
 * 69 = E		[Character]
 * 70 = F		[Character]
 * 71 = G		[Character]
 * 72 = H		[Character]
 * 73 = I		[Character]
 * 74 = J		[Character]
 * 75 = K		[Character]
 * 76 = L		[Character]
 * 77 = M		[Character]
 * 78 = N		[Backspace]
 * 79 = O		[Character]
 * 80 = P		[Character]
 * 81 = Q		[Character]
 * 82 = R		[Character]
 * 83 = S		[Character]
 * 84 = T		[Character]
 * 85 = U		[Character]
 * 86 = V		[Character]
 * 87 = W		[Character]
 * 88 = X		[Character]
 * 89 = Y		[Character]
 * 90 = Z		[Character]
 * 91 = [		[Character]
 * 92 = \		[Character]
 * 93 = ]		[Character]
 * 94 = ^		[Character]
 * 95 = _		[Character]
 * 96 = `		[Character]
 * 97 = a		[Character]
 * 98 = b		[Character]
 * 99 = c		[Character]
 * 100 = d		[Character]
 * 101 = e		[Character]
 * 102 = f		[Character]
 * 103 = g		[Character]
 * 104 = h		[Character]
 * 105 = i		[Character]
 * 106 = j		[Character]
 * 107 = k		[Character]
 * 108 = l		[Character]
 * 109 = m		[Character]
 * 110 = n		[Character]
 * 111 = o		[Character]
 * 112 = p		[Character]
 * 113 = q		[Character]
 * 114 = r		[Character]
 * 115 = s		[Character]
 * 116 = t		[Character]
 * 117 = u		[Character]
 * 118 = v		[Character]
 * 119 = w		[Character]
 * 120 = x		[Character]
 * 121 = y		[Character]
 * 122 = z		[Character]
 * 123 = {		[Character]
 * 124 = |		[Character]
 * 125 = }		[Character]
 * 126 = ~		[Character]
 * 127 = 		[Character]
 * Hit any key to continue...
 *
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 14_switch_statements_1 - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/14_switch_statements_1'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/14_switch_statements_1/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/14_switch_statements_1 @"14_switch_statements_1.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/14_switch_statements_1'
 * ====0 errors, 0 warnings====
 */