"""Type stubs for the native _lzokay module."""

# Exception hierarchy
class LzokayError(Exception):
    """Any kind of error."""
    ...

class LookbehindOverrunError(LzokayError):
    """Likely indicates bad compressed LZO input."""
    ...

class OutputOverrunError(LzokayError):
    """Output buffer was not large enough to store the compression/decompression result."""
    ...

class InputOverrunError(LzokayError):
    """Compressed input buffer is invalid or truncated."""
    ...

class LzokayUnknownError(LzokayError):
    """Unknown error."""
    ...

class InputNotConsumedError(LzokayError):
    """Decompression succeeded, but input buffer has remaining data."""
    ...

def compress(data: bytes) -> bytes:
    """
    Compress data using LZO compression.
    
    Args:
        data: The input bytes to compress
        
    Returns:
        The compressed data as bytes
        
    Raises:
        OutputOverrunError: If compression buffer is too small
        LzokayUnknownError: For other compression errors
    """
    ...

def decompress(data: bytes, buffer_size: int) -> bytes:
    """
    Decompress LZO compressed data.
    
    Args:
        data: The compressed input bytes
        buffer_size: Expected size of the decompressed output
        
    Returns:
        The decompressed data as bytes
        
    Raises:
        LookbehindOverrunError: If compressed data is invalid
        OutputOverrunError: If output buffer is too small
        InputOverrunError: If input buffer is invalid or truncated
        InputNotConsumedError: If input has remaining data after decompression
        LzokayUnknownError: For other decompression errors
    """
    ...