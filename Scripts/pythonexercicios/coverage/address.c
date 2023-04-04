#include <stdio.h>

int main(void)
{
    char *s = "HI!"; //string sosmente com a biblioteca cs50.h
    printf("%s\n", s);
    printf("%p\n", s); //endereço da memoria com tipo pointer (%p)
    printf("%p\n", &s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]); //ultimo caracter de uma string é o espaço em branco("\0")
}