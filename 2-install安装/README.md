>如何安装编译出来的二进制和头文件，库文件

# 指定安装目录前缀
CMAKE_INSTALL_PREFIX  

# 安装头文件
```cmake
# 设置PUBLIC_HEADER属性
set_target_properties(add PROPERTIES PUBLIC_HEADER inc/add.h)

# 安装add目标的PUBLIC_HEADER头
install(TARGETS add PUBLIC_HEADER)

# 也可以自定义安装目录，安装目录使用相对目录，它是相对变量CMAKE_INSTALL_PREFIX
install(TARGETS add PUBLIC_HEADER DESTINATION myinclude)
```

关键函数：  
* install
* add_custom_command

疑问：
为何用ninja构建器编译不过呢，它会先编译calc