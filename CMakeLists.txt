cmake_minimum_required(VERSION 3.18...3.22)

cmake_policy(SET CMP0148 OLD)

project(lzokay CXX)

find_package(Cython REQUIRED)
find_package(PythonExtensions REQUIRED)

add_subdirectory(native/lzokay)

add_cython_target(_lzokay _lzokay.pyx CXX PY3)
add_library(_lzokay MODULE ${_lzokay})
python_extension_module(_lzokay)

target_link_libraries(_lzokay lzokay)

install(TARGETS _lzokay LIBRARY DESTINATION .)