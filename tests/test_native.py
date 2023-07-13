import lzokay
import pytest


@pytest.mark.parametrize(
    "data",
    [
        b"Hello World",
        (
            b"Hello Worldello Worldello Worldello Worldello Worldello Worldello Worldello "
            b"Worldello Worldello Worldello Worldello Worldello Worldello Worldello World"
        ),
    ],
)
def test_compress_and_decompress(data):
    compressed = lzokay.compress(data)

    decompressed = lzokay.decompress(compressed)

    assert decompressed == data
