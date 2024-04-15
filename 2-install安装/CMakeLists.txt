cmake_minimum_required(VERSION 3.10)
project(myProject LANGUAGES C)

# 先自定义要安装的路径
set(INSTALL_DIR ${PROJECT_BINARY_DIR})
message("INSTALL_DIR1: ${INSTALL_DIR}")

add_subdirectory(lib_add)
add_subdirectory(calc)

