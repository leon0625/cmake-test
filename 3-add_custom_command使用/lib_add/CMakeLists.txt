add_library(add SHARED add.c)

# 使用PRIVATE，表示add_lib的头文件包含关系不会传递给使用它的目标
target_include_directories(add PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/inc)


# 因为install命令只在cmake --install .时才会执行，而我们build calc时就需要头文件了。所以需要在build时就安装头文件

if(${METHOD} STREQUAL "1")
  # 方法1,使用 add_custom_command
  # 借助add_custom_command来实现builld之前就安装
  add_custom_command(
    TARGET add PRE_BUILD
    COMMAND sleep 2 # 延迟2s,以便看到编译calc前确实在等这个命令执行完
    COMMAND mkdir -p ${CMAKE_INSTALL_PREFIX}/include
    COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/inc/add.h ${CMAKE_INSTALL_PREFIX}/include/
    COMMAND echo "======================="
    COMMENT "install lib add header file..."     # 执行时会打印
  )
endif()

add_custom_target(install_add_header
    COMMENT "install lib add header file..."     # 执行时会打印
    COMMAND sleep 2 # 延迟2s,以便看到编译calc前确实在等这个命令执行完
    COMMAND mkdir -p ${CMAKE_INSTALL_PREFIX}/include
    COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/inc/add.h ${CMAKE_INSTALL_PREFIX}/include/
    COMMAND echo "======================="
  )

if(${METHOD} STREQUAL "2")
  # 添加依赖，让install_add_header在add之前执行
  add_dependencies(add install_add_header)
endif()