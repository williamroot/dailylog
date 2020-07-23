/* Data: 2020-07-22 */

#include <stdio.h>

int main(int argc, char **argv) {
	/*
	 * 	int subtotal, total, tax;
	 * 	double taxrate;
	 * 
	 * Fazer cálculos com valores numéricos
	 * de tipos diversos (como int e decimal)
	 * pode gerar resultado inesperado.
	 * Segundo o instrutor,
	 * 		"the calculated values are all integers. 
	 * 		When the value of tax is displayed, it may be 
	 * 		either 34 or 35, depending on what compiler 
	 * 		you use, the optimizations used, whether the 
	 * 		program is a 32-bit program or a 64-bit program 
	 * 		and what processor you are running on. On 
	 * 		CodeLite on Windows, the result is 34. On Visual 
	 * 		Studio on Windows it is 35. On CodeLite on a Mac 
	 * 		it is 35 too (though even these values may 
	 * 		differ according to factors such as compiler 
	 * 		optimizations). The problem is that there is a 
	 * 		loss of precision when the tax is calculated and 
	 * 		the program may do different things to convert 
	 * 		the floating point value of subtotal * taxrate 
	 * 		to the integer value tax."
	 * Portanto, convertemos int em double.
	 */
	
	double subtotal, total, tax, taxrate;
	
	subtotal = 200;
	taxrate = 0.175;
	tax = subtotal * taxrate;
	total = subtotal + tax;
	
	/*
	 * printf("Com taxa aplicada ao valor de %d, há acréscimo de %d e o total vai para %d.\n", subtotal, tax, total);
	 * 
	 * Esta seria a linha para trazer o resultado com int.
	 * Mas como estamos trabalhando com double, precisamos
	 * adequá-la para receber ponto flutuante.
	 */
	printf("Com taxa aplicada ao valor de %.2f, há acréscimo de %.2f e o total vai para %.2f.\n", subtotal, tax, total);
	return 0;
}

/* 
 * INPUT:
 * $ /bin/sh -f /usr/lib/codelite/codelite_exec ./05_first_calcs
 * 
 * OUTPUT:
 * Com taxa aplicada ao valor de 200.00, há acréscimo de 35.00 e o total vai para 235.00.
 * Press ENTER to continue...
 * 
 * BUILD INPUT:
 * /bin/sh -c '/usr/bin/make -j8 -e -f  Makefile'
 * 
 * BUILD OUTPUT:
 * ----------Building project:[ 05_first_calcs - Debug ]----------
 * make[1]: Entering directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/05_first_calcs'
 * /usr/bin/gcc -c  "/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/05_first_calcs/main.c" -g -O0 -Wall  -o ./Debug/main.c.o -I. -I.
 * /usr/bin/g++ -o ./Debug/05_first_calcs @"05_first_calcs.txt" -L.
 * make[1]: Leaving directory '/home/rodolfo/Documents/Github/dailylog/studies/2020_huw_collingbourne_c_programming_for_beginners/01_basic/05_first_calcs'
 * ====0 errors, 0 warnings====
 */