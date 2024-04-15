cmake_minimum_required(VERSION 3.10)
project(dec_lib LANGUAGES C)

add_library(dec dec.c)

# 编译calc程序时，会自动加上如下指定目录的头文件搜索
target_include_directories(dec PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})