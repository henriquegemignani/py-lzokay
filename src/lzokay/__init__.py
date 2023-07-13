from . import version
from lzokay._lzokay import decompress, compress, compress_worst_size

__all__ = [
    "decompress",
    "compress",
    "compress_worst_size",
    "VERSION",
    "__version__",
]


__version__ = version.version
VERSION = version.version
