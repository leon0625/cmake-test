cmake_minimum_required(VERSION 3.20)
project(test LANGUAGES C)

add_subdirectory(lib)

add_executable(test test.c)
target_link_libraries(test PRIVATE lib)