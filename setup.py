import os
import platform
from pathlib import Path

import setuptools_cmake_helper
from setuptools import setup

file_dir = Path(__file__).parent.absolute().relative_to(Path().absolute())
cmake_project_dir = file_dir.joinpath("native", "lzokay")
extra_compile_args = []

if platform.system() == "Windows":
    extra_compile_args.append("-DUNICODE")
    extra_compile_args.append("/std:c++17")
    extra_compile_args.append("/MD")
else:
    extra_compile_args.append("-std=c++17")

ext_modules = [
    setuptools_cmake_helper.CMakeExtension(
        "lzokay._lzokay",
        [
            os.fspath(file_dir.joinpath("_lzokay.pyx")),
        ],
        cmake_project=cmake_project_dir,
        cmake_targets=["lzokay"],
        language="c++",
        extra_compile_args=extra_compile_args,
        extra_objects=[],
    )
]

cythonized_ext_modules = setuptools_cmake_helper.cythonize_extensions(
    ext_modules,
    include_paths=[os.fspath(cmake_project_dir)],
    language_level="3",
)


setup(
    cmdclass={
        "build_ext": setuptools_cmake_helper.CMakeBuild,
    },
    ext_modules=cythonized_ext_modules,
)
