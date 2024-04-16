>介绍add_custom_command安装
>因为install在build之后，所以当存在多个子目录时，如果target1 build依赖target2 install后的头文件怎么办呢？

关键函数：  
* add_custom_command
```cmake
add_custom_command(
  TARGET add POST_BUILD
  COMMAND sleep 2 # 延迟2s,以便看到编译calc前确实在等这个命令执行完
  COMMAND mkdir -p ${CMAKE_INSTALL_PREFIX}/include
  COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/inc/add.h ${CMAKE_INSTALL_PREFIX}/include/
  COMMAND echo "======================="
)
```


疑问： 
为何用ninja构建器编译不过呢? cmake bug?  
cmake版本3.22.1