#include <stdio.h>

#include "add.h"
#include "dec.h"

int main(int argc, char *argv[])
{
    printf("1+2=%d\n", add(1,2));
    printf("5-2=%d\n", dec(5,2));
    return 0;
}