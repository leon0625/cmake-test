>介绍add_custom_command安装
>因为install在build之后，所以当存在多个子目录时，如果target1 build依赖target2 install后的头文件怎么办呢？

关键函数：  
* add_custom_command 功能很多的函数
add_custom_command(TARGET)属于事件的使用：
```cmake
add_custom_command(TARGET <target>
                   PRE_BUILD | PRE_LINK | POST_BUILD
                   COMMAND command1 [ARGS] [args1...]
                   [COMMAND command2 [ARGS] [args2...] ...]
                   [BYPRODUCTS [files...]]
                   [WORKING_DIRECTORY dir]
                   [COMMENT comment]
                   [VERBATIM]
                   [COMMAND_EXPAND_LISTS])
```
模式事件是POST_BUILD。

```cmake
add_custom_command(
  TARGET add POST_BUILD
  COMMAND sleep 2 # 延迟2s,以便看到编译calc前确实在等这个命令执行完
  COMMAND mkdir -p ${CMAKE_INSTALL_PREFIX}/include
  COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/inc/add.h ${CMAKE_INSTALL_PREFIX}/include/
  COMMAND echo "======================="
  COMMENT "install lib add header file..."     # 执行时会打印
)
```


疑问： 
**为何两种方式ninja构建器都编译不过呢? **