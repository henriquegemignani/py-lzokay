"""
Python bindings for LZO compression/decompression using the Rust lzokay library.
"""

from lzokay._lzokay import (
    compress,
    decompress,
    LzokayError,
    LookbehindOverrunError,
    OutputOverrunError,
    InputOverrunError,
    LzokayUnknownError,
    InputNotConsumedError,
)


def compress_worst_size(length: int) -> int:
    """Returns the worst-case size for LZO compression of data of given length."""
    return length + (length // 16) + 64 + 3

__all__ = [
    "decompress",
    "compress",
    "compress_worst_size",

    "LzokayError",
    "LookbehindOverrunError",
    "OutputOverrunError",
    "InputOverrunError",
    "LzokayUnknownError",
    "InputNotConsumedError",
]
