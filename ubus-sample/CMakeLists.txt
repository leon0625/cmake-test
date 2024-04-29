cmake_minimum_required(VERSION 3.20)
project(ubus-sample LANGUAGES C)

# 下载代码
if(NOT EXISTS ${CMAKE_SOURCE_DIR}/libubox)
    execute_process(COMMAND git clone https://git.openwrt.org/project/libubox.git WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

if(NOT EXISTS ${CMAKE_SOURCE_DIR}/ubus)
    execute_process(COMMAND git clone https://git.openwrt.org/project/ubus.git WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

# 编译libubox
set(LIBUBOX_BUILD_DIR ${CMAKE_BINARY_DIR}/build_libubox)
add_custom_target(config_libubox
    COMMAND cmake -S ${CMAKE_SOURCE_DIR}/libubox -B ${LIBUBOX_BUILD_DIR} 
        -DBUILD_LUA=OFF
        -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/install
        -G ${CMAKE_GENERATOR}
)

add_custom_target(build_libubox
    COMMAND cmake --build ${LIBUBOX_BUILD_DIR}
    COMMAND cmake --install ${LIBUBOX_BUILD_DIR}
)

# 编译ubus，不需要指定libubox的路径安装路径，cmake自动会到CMAKE_INSTALL_PREFIX位置里面找
set(UBUS_BUILD_DIR ${CMAKE_BINARY_DIR}/build_ubus)
add_custom_target(build_ubus
    COMMAND cmake -S ${CMAKE_SOURCE_DIR}/ubus -B ${UBUS_BUILD_DIR}
                -DBUILD_LUA=OFF 
                -DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/install
                -DBUILD_STATIC=ON
                -DUBUS_UNIX_SOCKET=/tmp/ubus.sock
                -G ${CMAKE_GENERATOR}
    COMMAND cmake --build ${UBUS_BUILD_DIR}
    COMMAND cmake --install ${UBUS_BUILD_DIR}
)

add_executable(ubus-sample main.c) 

add_dependencies(ubus-sample build_libubox)
add_dependencies(build_libubox config_libubox)


add_dependencies(ubus-sample build_ubus)
add_dependencies(build_ubus build_libubox)
