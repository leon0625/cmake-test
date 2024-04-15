cmake_minimum_required(VERSION 3.10)
project(calc LANGUAGES C)

add_executable(calc calc.c)

# 这里添加编译要链接的库，自动会先编译add/dec的库
target_link_libraries(calc add dec)