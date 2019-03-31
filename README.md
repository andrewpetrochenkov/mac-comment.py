<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-comment.svg?longCache=True)](https://pypi.org/project/mac-comment/)
[![](https://img.shields.io/pypi/v/mac-comment.svg?maxAge=3600)](https://pypi.org/project/mac-comment/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-comment.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-comment.py/)

#### Installation
```bash
$ [sudo] pip install mac-comment
```

#### Functions
function|`__doc__`
-|-
`mac_comment.read(path)` |return string with Finder comment
`mac_comment.write(path, comment=None)` |write Finder comment

#### CLI
usage|`__doc__`
-|-
`python -m comment path [comment]` |read/write Finder comment

#### Examples
```python
>>> import mac_comment
>>> mac_comment.write(__file__,"comment")
>>> mac_comment.read(__file__)
'comment'
```

```bash
$ python -m mac_comment ~ "CLI works too"
$ python -m mac_comment ~
CLI works too
```

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>