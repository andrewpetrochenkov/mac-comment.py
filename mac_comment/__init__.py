#!/usr/bin/env python
import xattr
import public

kMDItemFinderComment = "kMDItemFinderComment"


@public.add
def read(path):
    """return string with Finder comment"""
    try:
        comment = xattr.getxattr(path, kMDItemFinderComment)
        return comment.decode("utf-8")
    except OSError:
        pass


@public.add
def write(path, comment=None):
    """write Finder comment"""
    if comment is None:
        xattr.removexattr(path, kMDItemFinderComment)
        return
    old = read(path)
    if comment != old:
        if comment is not None and hasattr(comment, "encode"):
            comment = comment.encode("utf-8")  # str/bytes required
        xattr.setxattr(path, kMDItemFinderComment, comment)

