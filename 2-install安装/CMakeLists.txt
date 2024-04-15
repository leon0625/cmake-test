cmake_minimum_required(VERSION 3.10)
project(myProject LANGUAGES C)

set(CMAKE_INSTALL_PREFIX ${PROJECT_BINARY_DIR}/install)

# 先自定义要安装的路径
set(INSTALL_DIR ${PROJECT_BINARY_DIR})
message("INSTALL_DIR: ${INSTALL_DIR}")

add_subdirectory(lib_add)
add_subdirectory(calc)

