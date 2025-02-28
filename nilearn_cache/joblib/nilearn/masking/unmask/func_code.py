# first line: 933
def unmask(X, mask_img, order="F"):
    """Take masked data and bring them back into 3D/4D.

    This function can be applied to a list of masked data.

    Parameters
    ----------
    X : :class:`numpy.ndarray` (or :obj:`list` of)
        Masked data. shape: (samples #, features #).
        If X is one-dimensional, it is assumed that samples# == 1.

    mask_img : Niimg-like object
        See :ref:`extracting_data`.
        Must be 3-dimensional.

    Returns
    -------
    data : :class:`nibabel.nifti1.Nifti1Image`
        Unmasked data. Depending on the shape of X, data can have
        different shapes:

        - X.ndim == 2:
          Shape: (mask.shape[0], mask.shape[1], mask.shape[2], X.shape[0])
        - X.ndim == 1:
          Shape: (mask.shape[0], mask.shape[1], mask.shape[2])
    """
    # Handle lists. This can be a list of other lists / arrays, or a list or
    # numbers. In the latter case skip.
    if isinstance(X, list) and not isinstance(X[0], numbers.Number):
        ret = [unmask(x, mask_img, order=order) for x in X]
        return ret

    # The code after this block assumes that X is an ndarray; ensure this
    X = np.asanyarray(X)

    mask_img = _utils.check_niimg_3d(mask_img)
    mask, affine = load_mask_img(mask_img)

    if np.ndim(X) == 2:
        unmasked = _unmask_4d(X, mask, order=order)
    elif np.ndim(X) == 1:
        unmasked = _unmask_3d(X, mask, order=order)
    else:
        raise TypeError(
            f"Masked data X must be 2D or 1D array; got shape: {str(X.shape)}"
        )

    return new_img_like(mask_img, unmasked, affine)
