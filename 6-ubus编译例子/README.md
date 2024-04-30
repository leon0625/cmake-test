# 说明
介绍add_custom_target 和 add_dependencies和add_custom_command

# 使用
```
cmake -B build -S. 
cmake --build build -j10
```

使用Ninja构建（更快）
```
cmake -B build -S. -GNinja
cmake --build build
```