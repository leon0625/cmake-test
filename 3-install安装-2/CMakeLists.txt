cmake_minimum_required(VERSION 3.10)
project(myProject LANGUAGES C)

set(CMAKE_INSTALL_PREFIX ${PROJECT_BINARY_DIR}/install)

add_subdirectory(lib_add)
add_subdirectory(calc)

