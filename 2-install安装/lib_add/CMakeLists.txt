cmake_minimum_required(VERSION 3.10)
project(add_lib LANGUAGES C)

add_library(add SHARED add.c)

# 使用PRIVATE，表示add_lib的头文件包含关系不会传递给使用它的目标
target_include_directories(add PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/inc)

# 因为install命令只在cmake --install .时才会执行，而我们build calc时就需要头文件了。所以需要在build时就安装头文件

# 借助add_custom_command来实现builld完成时就安装
# add_custom_command(
#   TARGET add POST_BUILD
#   COMMAND sleep 2
#   COMMAND mkdir -p ${INSTALL_DIR}/include
#   COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/inc/add.h ${INSTALL_DIR}/include/
#   COMMAND echo "======================="
# )

set_target_properties(add PROPERTIES PUBLIC_HEADER inc/add.h)

install(TARGETS add PUBLIC_HEADER)