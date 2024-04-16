>如何安装编译出来的二进制和头文件，库文件
>可执行程序和库二者没有依赖关系，作为一个整体构建，单纯讲安装


# 指定安装目录前缀
CMAKE_INSTALL_PREFIX，安装目录的路径如果是相对路径，是相当于该变量的相对路径  

# install函数
这个函数相当复杂，功能很多。这个例子只是简要使用了下。  
`install(TARGETS <target>)`会自动安装它认为需要安装的，一般包含可执行文件，库，公共头文件  
需要输出的公共头文件通过`set_target_properties(<target> PROPERTIES PUBLIC_HEADER <head file>>)`设置  

如果要自定义target安装目录,则需要加如下参数  
```cmake
# 安装targets
install(TARGETS <target>
        LIBRARY DESTINATION <dir>  # 库
        PUBLIC_HEADER DESTINATION <dir> # 头文件
        RUNTIME DESTINATION <dir> # 可执行文件
        )

# 安装普通文件
install(FILES <file> DESTINATION <dir>)
```

# 效果
本例支持用两种方法配置工程  
（1）cmake ../ -DINSTALL_TYPE1=ON  编译后安装结构为：
```
install
├── bin
│   └── calc
├── help.txt
├── include
│   └── add.h
└── lib
    └── libadd.so
```
(2) cmake ../ -DINSTALL_TYPE2=ON  编译后安装结构为：
```
myinstall/
├── _bin
│   └── calc
├── help.txt
├── _include
│   └── add.h
└── _lib
    └── libadd.so
```