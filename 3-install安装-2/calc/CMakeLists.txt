add_executable(calc calc.c)

# 这里添加编译要链接的库，自动会先编译add的库
target_link_libraries(calc add)

# 设置头文件路径为安装目录
target_include_directories(calc PRIVATE ${CMAKE_INSTALL_PREFIX}/include)