>展示多目录有依赖关系时,cmake该如何编写

关键函数：  
* add_subdirectory  
添加子目录
* target_link_libraries  
可执行文件链接的库，如果这个库是cmake的目标，cmake会自动添加依赖。先去编译库  
* target_link_libraries  
库里面使用这个，可以免去使用库的人设置头文件查找路径  