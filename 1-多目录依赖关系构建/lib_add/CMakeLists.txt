cmake_minimum_required(VERSION 3.10)
project(add_lib LANGUAGES C)

add_library(add add.c)

# 编译calc程序时，会自动加上如下指定目录的头文件搜索
target_include_directories(add PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# 人为睡眠2s,测试编译的依赖关系
add_custom_command(
  TARGET add PRE_BUILD
  COMMAND sleep 2
  COMMAND echo "build target add"  
)