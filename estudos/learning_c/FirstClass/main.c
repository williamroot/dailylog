#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main()
{
    printf("'Hello world!'\n\n");
    printf("(That is not an original line, for sure. ");
    printf("I have probably used it %d times in my life. ", 1074);
    printf("%d times now, I guess. ", 1075);
    printf("Does this self-reference count? Have I used it %d or %d times? ", 1074, 1075);
    printf("Let's settle this one as number %f.\n", 1074.5);
    printf("Shall we finally begin this class? Good.)\n");
    return 0;
}
