# 使用
```
mkdir build
cd build
cmake ../
make
```

使用Ninja构建（更快）
```
cmake -B build -S. -GNinja
cmake --build build
```