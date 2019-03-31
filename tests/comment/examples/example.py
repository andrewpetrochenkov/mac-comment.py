#!/usr/bin/env python
import mac_comment

path = __file__
mac_comment.write(path, "comment")
print(mac_comment.read(path))
