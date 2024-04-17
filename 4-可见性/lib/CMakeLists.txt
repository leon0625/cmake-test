cmake_minimum_required(VERSION 3.20)
project(test LANGUAGES C)


add_library(lib INTERFACE testlib.c testlib.h)
