########################################################################
## human_size(size)
#  \param size human readable size
#
########################################################################
def human_size(size: str) -> int:
    """Converts human readable size into bytes.

    :param size: human readable size
    :returns: size in bytes
    :raise TypeError: can't convert
    """
    if( size.endswith("Kb") ):
        return int(size[:-2], 0) * (2**7)
    elif( size.endswith("KB") ):
        return int(size[:-2], 0) * (2**10)
    elif( size.endswith("Mb") ):
        return int(size[:-2], 0) * (2**17)
    elif( size.endswith("MB") ):
        return int(size[:-2], 0) * (2**20)
    else:
        return int(size, 0)

