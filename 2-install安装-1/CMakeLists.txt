cmake_minimum_required(VERSION 3.10)
project(myProject LANGUAGES C)

option(INSTALL_TYPE1 "使用CMAKE_INSTALL_PREFIX变量安装" off)
option(INSTALL_TYPE2 "使用自定义变量安装" off)

if((NOT INSTALL_TYPE1) AND (NOT INSTALL_TYPE2))
    # 指定FATAL_ERROR将会停止配置过程
    message(FATAL_ERROR "请选择安装方式:INSTALL_TYPE1 or INSTALL_TYPE2")
endif()

if(INSTALL_TYPE1)
    set(CMAKE_INSTALL_PREFIX ${PROJECT_BINARY_DIR}/install)
    message("install dir: ${CMAKE_INSTALL_PREFIX}")
endif()

if(INSTALL_TYPE2)
    set(MY_INSTALL_DIR ${PROJECT_BINARY_DIR}/myinstall)
    set(MY_INSTALL_BIN_DIR ${MY_INSTALL_DIR}/_bin)
    set(MY_INSTALL_LIB_DIR ${MY_INSTALL_DIR}/_lib)
    set(MY_INSTALL_INC_DIR ${MY_INSTALL_DIR}/_include)
    message("install dir: ${MY_INSTALL_DIR}")
endif()

add_executable(calc calc.c)

add_library(add SHARED add.c)

# 这里添加编译要链接的库，自动会先编译add的库
target_link_libraries(calc add)

# 头文件目录
target_include_directories(calc PRIVATE inc)
target_include_directories(add PRIVATE inc)

# 需要输出安装的头文件
set_target_properties(add PROPERTIES PUBLIC_HEADER inc/add.h)

################### install ################################
if(INSTALL_TYPE1)
    # 命令默认会把target的public头文件安装到${CMAKE_INSTALL_PREFIX}/include目录
    # 把可执行文件安装到${CMAKE_INSTALL_PREFIX}/bin目录
    # 把库安装到${CMAKE_INSTALL_PREFIX}/lib目录
    install(TARGETS add)
    install(TARGETS calc)

    # 安装普通文件,不清楚类型，又没有通过TYPE指定，所以必须指定DESTINATION参数。安装到${CMAKE_INSTALL_PREFIX}下
    install(FILES help.txt DESTINATION .)
endif()

if(INSTALL_TYPE2)
    # 不能这样写两行，对于一个target，只能有一个install命令，不然其他文件会安装到默认位置
    # install(TARGETS add LIBRARY DESTINATION ${MY_INSTALL_LIB_DIR})
    # install(TARGETS add PUBLIC_HEADER DESTINATION ${MY_INSTALL_INC_DIR})

    # 在一个函数内完成target的所有安装
    install(TARGETS add
        LIBRARY DESTINATION ${MY_INSTALL_LIB_DIR}
        PUBLIC_HEADER DESTINATION ${MY_INSTALL_INC_DIR})
    
    install(TARGETS calc DESTINATION ${MY_INSTALL_BIN_DIR})
    
    # 安装普通文件
    install(FILES help.txt DESTINATION ${MY_INSTALL_DIR})
endif()

