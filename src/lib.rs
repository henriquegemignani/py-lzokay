use pyo3::prelude::*;
use pyo3::exceptions::PyException;
use lzokay;

pyo3::create_exception!(lzokay, LzokayError, PyException, "Any kind of error.");

// Custom Python exception classes for each lzokay::Error variant
pyo3::create_exception!(lzokay, LookbehindOverrunError, LzokayError, "Likely indicates bad compressed LZO input.");
pyo3::create_exception!(lzokay, OutputOverrunError, LzokayError, "Output buffer was not large enough to store the compression/decompression result.");
pyo3::create_exception!(lzokay, InputOverrunError, LzokayError, "Compressed input buffer is invalid or truncated.");
pyo3::create_exception!(lzokay, LzokayUnknownError, LzokayError, "Unknown error.");
pyo3::create_exception!(lzokay, InputNotConsumedError, LzokayError, "Decompression succeeded, but input buffer has remaining data.");

// Helper function to convert lzokay::Error to appropriate Python exception
fn lzokay_error_to_pyerr(error: lzokay::Error) -> PyErr {
    match error {
        lzokay::Error::LookbehindOverrun => LookbehindOverrunError::new_err("lookbehind overrun"),
        lzokay::Error::OutputOverrun => OutputOverrunError::new_err("output overrun"),
        lzokay::Error::InputOverrun => InputOverrunError::new_err("input overrun"),
        lzokay::Error::Error => LzokayUnknownError::new_err("unknown error"),
        lzokay::Error::InputNotConsumed => InputNotConsumedError::new_err("input not consumed"),
    }
}

/// Decompress
#[pyfunction]
fn decompress(data: &[u8], buffer_size: usize) -> PyResult<Vec<u8>> {
    let mut dst = vec![0u8; buffer_size];

    lzokay::decompress::decompress(data, &mut dst).map_err(lzokay_error_to_pyerr)?;

    Ok(dst)
}

/// Formats the sum of two numbers as string.
#[pyfunction]
fn compress(data: &[u8]) -> PyResult<Vec<u8>> {
    let ret = lzokay::compress::compress(data).map_err(lzokay_error_to_pyerr)?;
    Ok(ret)
}

#[pymodule]
fn _lzokay(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(compress, m)?)?;
    m.add_function(wrap_pyfunction!(decompress, m)?)?;
    
    // Add exception classes to the module
    m.add("LzokayError", m.py().get_type::<LzokayError>())?;
    m.add("LookbehindOverrunError", m.py().get_type::<LookbehindOverrunError>())?;
    m.add("OutputOverrunError", m.py().get_type::<OutputOverrunError>())?;
    m.add("InputOverrunError", m.py().get_type::<InputOverrunError>())?;
    m.add("LzokayUnknownError", m.py().get_type::<LzokayUnknownError>())?;
    m.add("InputNotConsumedError", m.py().get_type::<InputNotConsumedError>())?;
    
    Ok(())
}
