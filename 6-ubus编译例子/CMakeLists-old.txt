cmake_minimum_required(VERSION 3.20)
project(ubus-sample LANGUAGES C)

################### json-c 编译 ###################
set(JSON_C_PKG json-c-0.17-20230812)
add_custom_command(
    OUTPUT json-c-${JSON_C_PKG}
    COMMAND wget https://github.com/json-c/json-c/archive/refs/tags/${JSON_C_PKG}.tar.gz
    COMMAND tar -xf ${JSON_C_PKG}.tar.gz
)

add_custom_target(build_jsonc
    DEPENDS json-c-${JSON_C_PKG}
    COMMAND cmake -S json-c-${JSON_C_PKG} -B jsonc-build
                    -DCMAKE_INSTALL_PREFIX=install
                    -G ${CMAKE_GENERATOR}
    COMMAND cmake --build jsonc-build
    COMMAND cmake --install jsonc-build
)
###################################################

#################### libubox编译 ##############################
add_custom_command(
    OUTPUT libubox
    COMMAND git clone https://git.openwrt.org/project/libubox.git
)

# 编译libubox，全部使用相对路径
add_custom_target(build_libubox
    # 先配置环境变量，指定pkg-config的路径，不然找不到json-c
    COMMAND PKG_CONFIG_PATH=${CMAKE_BINARY_DIR}/install/lib/pkgconfig 
            cmake -S libubox -B build_libubox
                -DBUILD_LUA=OFF
                -DBUILD_STATIC=ON
                -DCMAKE_INSTALL_PREFIX=install
                -G ${CMAKE_GENERATOR}
    COMMAND cmake --build build_libubox
    COMMAND cmake --install build_libubox
    DEPENDS libubox  # 依赖下载的源代码
)

######################  ubus 编译 ##################################
add_custom_command(
    OUTPUT ${CMAKE_BINARY_DIR}/ubus
    COMMAND git clone https://git.openwrt.org/project/ubus.git
)

# 全部使用绝对路径
# 编译ubus，不需要指定libubox的路径安装路径，cmake自动会到CMAKE_INSTALL_PREFIX位置里面找
set(UBUS_BUILD_DIR ${CMAKE_BINARY_DIR}/build_ubus)
add_custom_target(build_ubus
    COMMAND cmake -S ${CMAKE_BINARY_DIR}/ubus -B ${UBUS_BUILD_DIR}
                -DBUILD_LUA=OFF 
                -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/install
                -DBUILD_STATIC=ON
                -G ${CMAKE_GENERATOR}
    COMMAND cmake --build ${UBUS_BUILD_DIR}
    COMMAND cmake --install ${UBUS_BUILD_DIR}
    DEPENDS ${CMAKE_BINARY_DIR}/ubus
)

# 设置头文件和库文件的搜索路径
INCLUDE_DIRECTORIES(${CMAKE_BINARY_DIR}/install/include)
LINK_DIRECTORIES(${CMAKE_BINARY_DIR}/install/lib)

ADD_EXECUTABLE(server server.c count.c)
TARGET_LINK_LIBRARIES(server ubus ubox blobmsg_json json-c)

ADD_EXECUTABLE(client client.c count.c)
TARGET_LINK_LIBRARIES(client ubus ubox blobmsg_json json-c)

add_dependencies(build_libubox build_jsonc)
add_dependencies(server build_ubus)
add_dependencies(client build_ubus)
add_dependencies(build_ubus build_libubox)
