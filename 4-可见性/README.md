>Cmake可见性实验

# 原理
从 modern cmake(>=3.0) 开始，使用的范式从 director-oriented 转换到了 target-oriented。 这其中最重要的有三个概念：

* target  
* target相应的properties  
* 可见性  

所谓target就是编译的目标，一般就三种：  

* 静态库: 使用add_library()
* 动态库: 使用add_library() 指定SHARED关键字
* 可执行文件: 使用add_executable

所谓properties就是target的属性，最常见的有以下五种：

* 编译标志：使用target_complie_option
* 预处理宏标志：使用 target_compile_definitions
* 头文件目录：使用 target_include_directories
* 链接库：使用 target_link_libraries
* 链接标志：使用 target_link_options

所谓可见性就是上述这些属性在不同target之间的传递性。有三种：

* PRIVATE：只有自己用
* PUBLIC：自己和使用自己的别人都用
* INTERFACE：自己不用，只给使用的人用
  
上面的这些都是很好理解。但INTERFACE是不好理解的。我们详细讲解。

# INTERFACE
说到INTERFACE，我们先来看其他两种可见性：PUBLIC和PRIVATE。

假设我们有目标A和目标B。目标A编译成可执行文件，是我们最终要运行的目标。而目标B则编译成目标A的一个依赖，比如说，静态库。

PUBLIC的意思就是 目标B的属性 不仅自己使用，还传递给依赖它的目标A。

PRIVATE的意思就是 目标B的属性 不会传递，只给目标B自己使用。

而INTERFACE则极为特殊：它的属性都 不会自己使用，只传递给目标A。

## 什么情况下会使用INTERFACE呢
（1）如纯头文件的库，自己不会生成任何文件。
```cmake
add_library(Eigen INTERFACE)

target_sources(Eigen INTERFACE
  FILE_SET HEADERS
    BASE_DIRS src
    FILES src/eigen.h src/vector.h src/matrix.h
)

add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 Eigen)
```
如上，Eigen库只有头文件，target sources也是一种属性，会传递给exe1。exe1链接时，就能使用到这些源文件。

（2）一些库会导出一些专门给别人用的头文件，而自己不会用。那么应该也是可以通过INTERFACE来指定的。

# 参考
[彻底弄懂cmake中的 INTEFACE 可见性/传递性 问题](https://chunleili.github.io/cmake/understanding-INTERFACE)