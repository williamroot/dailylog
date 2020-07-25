/* Data: 2020-07-25 */

#include <stdio.h>

int main(int argc, char **argv)
{
	/*
	 * Outra forma de definir constantes em
	 * compiladores modernos é usando const
	 * e tratando como se fosse variável:
	 * 		const double PI = 3.141593;
	 * Mas há diferença entre #define e
	 * const, como aponta o instrutor:
	 * 		"#define and const are two quite 
	 * 		different things. #define is an 
	 * 		instruction to replace an 
	 * 		identifier with a value. By long 
	 * 		tradition, #define is used to 
	 * 		define values such as PI which 
	 * 		should not be changed. In fact, 
	 * 		however, C allows you to change 
	 * 		its value (it can be redefined) 
	 * 		so it is not a true constant. A 
	 * 		more modern addition to C is the 
	 * 		keyword const which lets you 
	 * 		define values that cannot be 
	 * 		changed and are therefore true 
	 * 		constants. Not all C compilers 
	 * 		support const, however, and even 
	 * 		where it is supported, many 
	 * 		programmers prefer to use the more 
	 * 		traditional #define directive."
	 * Então temos #define, que suporta 
	 * alterações (não sendo "true constant")
	 * e const, que não suporta.
	 */
	#define VALOR_COM_DEFINE 18.19
	const double VALOR_COM_CONST = 81.91;
	printf("VALOR_COM_DEFINE = %.2f\nVALOR_COM_CONST = %.2f\n", VALOR_COM_DEFINE, VALOR_COM_CONST);
	/* 
	 * OUTPUT:
	 * VALOR_COM_DEFINE = 18.19
	 * VALOR_COM_CONST = 81.91
	 */
	#define VALOR_COM_DEFINE 19.18
	printf("Novo VALOR_COM_DEFINE = %.2f\n", VALOR_COM_DEFINE);
	/* 
	 * OUTPUT:
	 * (1 warning, mas compila)
	 * main.c:45: warning: "VALOR_COM_DEFINE" redefined
	 */
	const double VALOR_COM_CONST = 91.81;
	printf("Novo VALOR_COM_CONST = %.2f\n", VALOR_COM_CONST);
	/*
	 * OUTPUT:
	 * (1 erro, não compila)
	 * main.c:52:15: error: redefinition of 'VALOR_COM_CONST'
	 */	
	return 0;
}
