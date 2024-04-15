cmake_minimum_required(VERSION 3.10)
project(calc LANGUAGES C)

add_executable(calc calc.c)

# 这里添加编译要链接的库，自动会先编译add的库
target_link_libraries(calc add)

install(TARGETS calc DESTINATION ${INSTALL_DIR}/bin)

# 设置头文件路径为安装目录
target_include_directories(calc PRIVATE ${INSTALL_DIR}/include)