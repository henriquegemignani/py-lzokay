from cpython cimport array
import array

from lzokay_wrap cimport (
    decompress as c_decompress,
    compress as c_compress,
    EResult as c_EResult,
)


def compress_worst_size(s: int) -> int:
    return s + s // 16 + 64 + 3


def decompress(data: bytes) -> bytes:
    expected_out_size = compress_worst_size(len(data))

    cdef size_t actual_out_size = 0    
    cdef array.array b = array.array('B')
    array.resize(b, expected_out_size)
    
    code = c_decompress(data, len(data), b.data.as_uchars, len(b), actual_out_size)
    array.resize(b, actual_out_size)

    if code != c_EResult.Success:
        raise ValueError("Error: {}".format(code))

    return b.tobytes()

    
def compress(data: bytes) -> bytes:
    expected_out_size = compress_worst_size(len(data))

    cdef size_t actual_out_size = 0    
    cdef array.array b = array.array('B')
    array.resize(b, expected_out_size)
    
    code = c_compress(data, len(data), b.data.as_uchars, len(b), actual_out_size)
    array.resize(b, actual_out_size)

    if code != c_EResult.Success:
        raise ValueError("Error: {}".format(code))

    return b.tobytes()

    