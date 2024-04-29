cmake_minimum_required(VERSION 3.10)
project(myProject LANGUAGES C)

set(CMAKE_INSTALL_PREFIX ${PROJECT_BINARY_DIR}/install)
option(METHOD "使用哪种方式解决编译头文件问题" 1)

add_subdirectory(lib_add)
add_subdirectory(calc)

