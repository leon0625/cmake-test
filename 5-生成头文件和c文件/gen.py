#!/usr/bin/env python3

import sys

cdata = r'''
#include <stdio.h>
#include "generated_header.h"

void test(void)
{
    printf("%s\n", HELLO);
}
'''

hdata = r'''
#pragma once
#define HELLO "hello,world2"

void test(void);
'''

if sys.argv[1] == "c":
    print(cdata, file=open(sys.argv[2], "w"))
elif sys.argv[1] == "h":
    print(hdata, file=open(sys.argv[2], "w"))

