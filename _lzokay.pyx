from cpython cimport array
import array

from lzokay_wrap cimport (
    decompress as c_decompress,
    compress as c_compress,
    EResult as c_EResult,
)


class LookbehindOverrun(Exception):
    pass


class OutputOverrun(Exception):
    pass


class InputOverrun(Exception):
    pass


class Error(Exception):
    pass


class InputNotConsumed(Exception):
    pass


result_mapping = {
    c_EResult.LookbehindOverrun: LookbehindOverrun,
    c_EResult.OutputOverrun: OutputOverrun,
    c_EResult.InputOverrun: InputOverrun,
    c_EResult.Error: Error,
    c_EResult.InputNotConsumed: InputNotConsumed,
}


def compress_worst_size(s: int) -> int:
    return s + s // 16 + 64 + 3


def decompress(data: bytes, expected_output_size: int = None) -> bytes:
    if expected_output_size is None:
        expected_output_size = len(data)
    
    cdef size_t actual_out_size = 0    
    cdef array.array b = array.array('B')
    array.resize(b, expected_output_size)
    
    code = c_EResult.OutputOverrun
    while code == c_EResult.OutputOverrun:
        code = c_decompress(data, len(data), b.data.as_uchars, len(b), actual_out_size)
        if code == c_EResult.OutputOverrun:
            array.resize(b, 2 * len(b))
    
    array.resize(b, actual_out_size)

    if code in result_mapping:
        raise result_mapping[code]()

    return b.tobytes()

    
def compress(data: bytes) -> bytes:
    expected_out_size = compress_worst_size(len(data))

    cdef size_t actual_out_size = 0    
    cdef array.array b = array.array('B')
    array.resize(b, expected_out_size)
    
    code = c_compress(data, len(data), b.data.as_uchars, len(b), actual_out_size)
    array.resize(b, actual_out_size)

    if code in result_mapping:
        raise result_mapping[code]()

    return b.tobytes()

    