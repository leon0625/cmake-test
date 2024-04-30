cmake_minimum_required(VERSION 3.20)
project(test LANGUAGES C)

set(GEN_TOOL ${CMAKE_SOURCE_DIR}/gen.py)

# 设置生成的头文件的名字和路径
set(GENERATED_HEADER "generated_header.h")

# 定义一个自定义命令来生成该头文件
add_custom_command(
    OUTPUT ${GENERATED_HEADER}
    COMMAND ${GEN_TOOL} h ${GENERATED_HEADER}
    DEPENDS ${GEN_TOOL}
)

# 创建一个自定义目标，确保头文件在构建过程中被生成
add_custom_target(GenerateHeader DEPENDS ${GENERATED_HEADER})

set(GENERATED_CCODE "test.c")
add_custom_command(
    OUTPUT ${GENERATED_CCODE}
    COMMAND ${GEN_TOOL} c ${GENERATED_CCODE}
    DEPENDS ${GEN_TOOL}
)
add_custom_target(GenerateCcode DEPENDS ${GENERATED_CCODE})

add_executable(test main.c ${GENERATED_CCODE})
target_include_directories(test PRIVATE ${CMAKE_CURRENT_BINARY_DIR})

# 确保在构建MyLibrary或MyExecutable前生成Header文件
add_dependencies(test GenerateHeader)
